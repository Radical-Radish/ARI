# Python Module Imports
import signal
import sys
import time
import threading
import asyncio

# Class Imports
from signals import Signals
from prompter import Prompter
from llm_helper.llmState import LLMState
from llm_helper.textLLMWrapper import TextLLMWrapper
from stt import STT
from tts import TTS
from memory.memory import Memory
from socketioServer import SocketIOServer


async def main():
    print("Ari is waking up...")

    # Register signal handler so that all threads can be exited.
    def signal_handler(sig, frame):
        print('Received CTRL + C, See you later')
        signals.terminate = True
        stt.API.shutdown()

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # CORE FILES

    # Singleton object that every module will be able to read/write to
    signals = Signals()

    # MODULES
    # Modules that start disabled CANNOT be enabled while the program is running.
    modules = {}
    module_threads = {}

    # Create STT
    stt = STT(signals)
    # Create TTS
    tts = TTS(signals)
    # Create LLMWrappers
    llmState = LLMState()
    llms = {
        "text": TextLLMWrapper(signals, tts, llmState, modules)
    }
    # Create Prompter
    prompter = Prompter(signals, llms, modules)
    # Create Memory module
    modules['memory'] = Memory(signals, enabled=True)

    # Create Socket.io server
    # The specific llmWrapper it gets doesn't matter since state is shared between all llmWrappers
    sio = SocketIOServer(signals, stt, tts, llms["text"], prompter, modules=modules)

    # Create threads (As daemons, so they exit when the main thread exits)
    prompter_thread = threading.Thread(target=prompter.prompt_loop, daemon=True)
    stt_thread = threading.Thread(target=stt.listen_loop, daemon=True)
    sio_thread = threading.Thread(target=sio.start_server, daemon=True)
    # Start Threads
    sio_thread.start()
    prompter_thread.start()
    stt_thread.start()

    # Create and start threads for modules
    for name, module in modules.items():
        module_thread = threading.Thread(target=module.init_event_loop, daemon=True)
        module_threads[name] = module_thread
        module_thread.start()

    while not signals.terminate:
        time.sleep(0.1)
    print("TERMINATING ======================")

    # Wait for child threads to exit before exiting main thread

    # Wait for all modules to finish
    for module_thread in module_threads.values():
        module_thread.join()

    sio_thread.join()
    print("SIO EXITED ======================")
    prompter_thread.join()
    print("PROMPTER EXITED ======================")
    # stt_thread.join()
    # print("STT EXITED ======================")

    print("All threads exited, shutdown complete")
    sys.exit(0)

if __name__ == '__main__':
    asyncio.run(main())
