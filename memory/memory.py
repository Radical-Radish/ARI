from helper.module import Module
from constants import *
from chromadb.config import Settings
import chromadb
import requests
import json
import uuid
import asyncio
import copy


class Memory(Module):

    def __init__(self, signals, enabled=True):
        super().__init__(signals, enabled)

        self.API = self.API(self)
        self.prompt_injection.text = ""
        self.prompt_injection.priority = 60

        self.processed_count = 0

        self.chroma_client = chromadb.PersistentClient(path="./memory/chroma_db", settings=Settings(anonymized_telemetry=False))
        self.collection = self.chroma_client.get_or_create_collection(name="neuro_collection")
        print(f"MEMORY: Loaded {self.collection.count()} memories from database.")
        if self.collection.count() == 0:
            print("MEMORY: No memories found in database. Importing from manual_memory.json")
            self.API.import_json(path="./memory/manual_memory.json")

    def get_prompt_injection(self):
        # Use recent messages and twitch messages to query the database for related memories
        query = ""

        # for message in self.signals.recentTwitchMessages:
        #     query += message + "\n"

        for message in self.signals.history[-MEMORY_QUERY_MESSAGE_COUNT:]:
            if message["role"] == "user" and message["content"] != "":
                query += HOST_NAME + ": " + message["content"] + "\n"
            elif message["role"] == "assistant" and message["content"] != "":
                query += AI_NAME + ": " + message["content"] + "\n"

        memories = self.collection.query(query_texts=query, n_results=MEMORY_RECALL_COUNT)

        # Generate injection for LLM prompt

        self.prompt_injection.text = f"{AI_NAME} knows these things:\n"
        for i in range(len(memories["ids"][0])):
            self.prompt_injection.text += memories['documents'][0][i] + "\n"
        self.prompt_injection.text += "End of knowledge section\n"

        return self.prompt_injection

    async def run(self):
        # Periodically, check if at least 20 new messages have been sent, and if so, generate 3 question-answer pairs
        # to be stored into memory.
        while not self.signals.terminate:
            if self.processed_count > len(self.signals.history):
                self.processed_count = 0

            if len(self.signals.history) - self.processed_count >= 20:
                print("MEMORY: Generating new memories")

                # Copy the latest unprocessed messages
                messages = copy.deepcopy(self.signals.history[-(len(self.signals.history) - self.processed_count):])

                for message in messages:
                    if message["role"] == "user" and message["content"] != "":
                        message["content"] = HOST_NAME + ": " + message["content"] + "\n"
                    elif message["role"] == "assistant" and message["content"] != "":
                        message["content"] = AI_NAME + ": " + message["content"] + "\n"

                chat_section = ""
                for message in messages:
                    chat_section += message["content"]

                data = {
                    "mode": "instruct",
                    "max_tokens": 200,
                    "skip_special_tokens": False,  # Necessary for Llama 3
                    "custom_token_bans": BANNED_TOKENS,
                    "stop": STOP_STRINGS.remove("\n"),
                    "messages": [{
                        "role": "user",
                        "content": chat_section + MEMORY_PROMPT
                    }]
                }
                headers = {"Content-Type": "application/json"}

                response = requests.post(LLM_ENDPOINT + "/v1/chat/completions", headers=headers, json=data, verify=False)
                raw_memories = response.json()['choices'][0]['message']['content']

                # Split each Q&A section and add the new memory to the database
                for memory in raw_memories.split("{qa}"):
                    memory = memory.strip()
                    if memory != "":
                        self.collection.upsert([str(uuid.uuid4())], documents=[memory], metadatas=[{"type": "short-term"}])

                self.processed_count = len(self.signals.history)

            await asyncio.sleep(5)

    class API:
        def __init__(self, outer):
            self.outer = outer

        def import_json(self, path="./memory/memories.json"):
            with open(path, "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    print("Error decoding JSON file")
                    return

            for memory in data["memories"]:
                self.outer.collection.upsert(memory["id"], documents=memory["document"], metadatas=memory["metadata"])