# ARI

ARI: AI-Driven Digital Persona Receptionist is our team capstone project to develop our Robotics and AI department's mascot that can help give informations to current students, prospective students and visitors, with the vision to make interacting with AI unintimidating for less tech-savvy person.


## Features

- Realtime STT for natural voice input
- Realtime TTS for natural voice output
- Memory: Can be added by RAG or manually added.


## Architecture

- [LLM](https://github.com/oobabooga/text-generation-webui)
- [STT](https://github.com/KoljaB/RealtimeSTT)
- [TTS](https://github.com/KoljaB/RealtimeTTS)
- [RAG](https://github.com/pixegami/rag-tutorial-v2)


## External Installation

Install VTube Studio from Steam.

Install [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui), and download an LLM model to use (I used [LLAMA 3 8B Instruct EXL2 4.0bpw](https://huggingface.co/turboderp/Llama-3-8B-Instruct-exl2/tree/4.0bpw)).On the ExLlamav2_HF loader with cache_8bit turned on. The openai api extension (Can be found on the last tab) must be turned on, as this is how we interact with the LLM.

Install a virtual audio cable like [VB-Audio](https://vb-audio.com/Cable/) (I use the VB-Audio cable A+B) to give the TTS output directly into Vtube Studio and Discord. Also, get STT input from Discord.

(RAG) Download [Ollama](https://ollama.com/download). In your Powershell type "ollama pull llama2" to pull a model (Can choose your own model).


## Preparation

Make a virtual environment (Python 3.11).

Install the CUDA 11.8 version of pytorch 2.2.2. with
`pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu118`

Install requirements-ari.txt (Some dependencies will be unused, so, installing according to imports is another option). Use `pip list` to confirm that the CUDA is still the 2.2.2+cu118 version of torch and torchaudio still installed. If it got overridden, use the first command to install it again.

DeepSpeed (For TTS) will need to be installed separately. I used instructions from [AllTalkTTS](https://github.com/erew123/alltalk_tts?#-deepspeed-installation-options), and used their [provided wheels](https://github.com/erew123/alltalk_tts/releases/tag/DeepSpeed-14.0).

If there are trouble with dependency conflicts, see piplist.txt and change to that specific version.

Create an .env file using .env.example as reference. You need your Huggingface token if you use a gated model (like Llama 3).

Place a voice reference wav file in the voice_template directory. It should be 5-30 seconds long. For details see the RealtimeTTS repository.

Find the desired microphone and speaker device numbers by running helper/listAudioDevices.py and note its numbers.

Configure constants.py. Make sure to configure every value marked as UNIQUE, these are specific to you and must be changed or confirmed.

(VB-Audio Cable) For INPUT_DEVICE_INDEX and OUTPUT_DEVICE_INDEX, choose the same cable in Discord's "Voice Setting". Example, Cable-A output for INPUT_DEVICE_INDEX, then, in Discord choose Cable-A input for output device.

(RAG) Make another virtual environment to avoid dependencies conflict and install requirements-rag.txt. In Powershell, type "ollama serve". Return to VScode and run memory/RAG.py. However, if you want to use the manual input memory, you have to run the main.py before using RAG.py.


## Running

Go to text-generation-webui folder (On desktop not vscode), click on the batch file "start_windows". After the "text-generation-webui" starts go to "http://127.0.0.1:7860" to load model. Load the "turboderp_Llama-3-8B-Instruct-exl2_4.0bpw" model in the "Model" tab.

Open "VTube Studio" from Steam.

In the terminal, navigate to ./ARI (or the folder with the "main.py" file) and type "python main.py" to start. Wait until the message "ARI is Ready" to show up.

Open Discord and join into a voice channel. In the camera option, use the VTube Studio virtual camera.

Join the same channel with a different Discord's account and start talking to Ari.


# DISCLAIMER

This project is a derivative works of [kimjammer/Neuro](https://github.com/kimjammer/Neuro) with modification to suits the vision of our team capstone project and is for educational purpose only.