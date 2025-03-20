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

# Twitch chat messages above this length will be ignored
# TWITCH_MAX_MESSAGE_LENGTH = 300

# Twitch channel for bot to join
#UNIQUE#
# TWITCH_CHANNEL = "kmitlraicapstone2024"

# Voice reference file for TTS
#UNIQUE#
VOICE_REFERENCE = "3.wav"

# MULTIMODAL SPECIFIC SECTION: Not needed when not using multimodal capabilities

# MULTIMODAL_ENDPOINT = ""

# MULTIMODAL_MODEL = "openbmb/MiniCPM-Llama3-V-2_5-int4"

# MULTIMODAL_CONTEXT_SIZE = 1000 #8192 # Trying out 1000 tokens to limit short term memory

# This is the multimodal strategy (when to use multimodal/text only llm) that the program will start with.
# Runtime changes will not be saved here.
# Valid values are: "always", "never"
# MULTIMODAL_STRATEGY = "never"

# This is the monitor index that screenshots will be taken. THIS IS NOT THE MONITOR NUMBER IN DISPLAY SETTINGS
# Monitor 0 is a "virtual" monitor contains all monitor screens.
# PRIMARY_MONITOR = 0

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

# VTUBE STUDIO SECTION: Configure & tune model & prop positions here.
# The defaults are for the Hiyori model on a full 16 by 9 aspect ratio screen
'''
VTUBE_MODEL_POSITIONS = {
    "chat": {
        "x": 0.4,
        "y": -1.4,
        "size": -35,
        "rotation": 0,
    },
    "screen": {
        "x": 0.65,
        "y": -1.6,
        "size": -45,
        "rotation": 0,
    },
    "react": {
        "x": 0.7,
        "y": -1.7,
        "size": -48,
        "rotation": 0,
    },
}

VTUBE_MIC_POSITION = {
    "x": 0.52,
    "y": -0.52,
    "size": 0.22,
    "rotation": 0,
}
'''