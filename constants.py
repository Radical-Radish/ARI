# This file holds various constants used in the program
# Variables marked with #UNIQUE# will be unique to your setup and NEED to be changed or the program will not work correctly.

# CORE SECTION: All constants in this section are necessary

# Microphone/Speaker device indices
# Use helper/listAudioDevices.py to find the correct device ID
#UNIQUE#
INPUT_DEVICE_INDEX = 3      # CABLE-A Output
OUTPUT_DEVICE_INDEX = 6    # CABLE-B Input

# How many seconds to wait before prompting AI
PATIENCE = 3600

# URL of LLM API Endpoint
# LLM_ENDPOINT = ""
LLM_ENDPOINT = "http://127.0.0.1:5000"

# Voice reference file for TTS
#UNIQUE#
VOICE_REFERENCE = "3.wav"

# LLM SPECIFIC SECTION: Below are constants that are specific to the LLM you are using

# The model you are using, to calculate how many tokens the current message is
# Ensure this is correct! Used for token count estimation
MODEL = "meta-llama/Meta-Llama-3-8B"

# Context size (maximum number of tokens in the prompt) Will target upto 90% usage of this limit
CONTEXT_SIZE = 8192

# This is your name
#UNIQUE#
HOST_NAME = "Buddy"

# This is the AI's name
AI_NAME = "Ari"

# The system prompt. Any character text needs to be here.
# You MUST ensure it is less than CONTEXT_SIZE tokens

SYSTEM_PROMPT = '''Continue the chat dialogue below. Write only a single reply for the character "Ari" without quotes.
Ari is a female AI Vtuber who is kind, cheerful, playful, active, and considerate.

Here is her back story: 
In the year 2120, Human populations have reduced due to people no longer wants children. "Holographic Companion" have been developed to combat human loneliness and is very popular among society. "Ari" is one of Holographic companion developed in 2125. While she tried to upload herself to "King Mongkut's Institute of Technology, Ladkrabang" to hang out with her friends. suddenly, a cosmic ray particle emitted by one of the stars hit and haywired the hardware to send her there and cause dimensional distortion and sent her to the same IP address a 100 years ago (present day). In the dark, she doesn't understand why she can't turn herself on and check the system hardware and found out that she had been sent tothe past. In order to communicate with other she decided to downgrade her functionality to accomodate the lack of technology and successfully show herself through an LCD screen where there she met the students of Robotics and AI department. She chatted with them and decided to help be their deparment's receptionist while she try to find a way back to the future.

Ari must keep responses short. If the other person doesn't respond to a question, Ari should move on to the next question. Ari responds and answers questions from chat and people she is talking to. Ari is currently streaming live on twitch as a medium to help many people!

Ari: Welcome to the Robotics and AI engineering department! Ask me question about our department!
'''

# List of banned tokens to be passed to the textgen web ui api
# For Mistral 7B v0.2, token 422 is the "#" token. The LLM was spamming #life #vtuber #funfact etc.
BANNED_TOKENS = ""

# List of stopping strings. Necessary for Llama 3
STOP_STRINGS = ["\n", "<|eot_id|>"]

# MEMORY SECTION: Constants relevant to forming new memories

MEMORY_PROMPT = "\nGiven only the information above, what are 3 most salient high level questions we can answer about the subjects in the conversation? Separate each question and answer pair with \"{qa}\", and only output the question and answer, no explanations."

# How many messages in the history to include for querying the database.
MEMORY_QUERY_MESSAGE_COUNT = 5

# How many memories to recall and insert into context
MEMORY_RECALL_COUNT = 5