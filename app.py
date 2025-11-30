import edge_tts
import asyncio
from io import BytesIO

# VOICE = "en-IN-PrabhatNeural"
# VOICE = "en-IN-NeerjaNeural"
# VOICE = "en-IN-NeerjaExpressiveNeural"

VOICES = [
    "en-IN-PrabhatNeural",
    "en-IN-NeerjaNeural",
    "en-IN-NeerjaExpressiveNeural"
]

TEXT = "Hello this is the demonstrtion of the tts app in test mode"



async def tts_generate(TEXT , VOICE ,rate="+0%"):
    tts = edge_tts.Communicate(TEXT , VOICE , rate=rate)
    audio_buffer = BytesIO()
    
    async for chunk in tts.stream():
        if chunk["type"] == "audio":
            audio_buffer.write(chunk["data"])
    audio_buffer.seek(0)
    print("done")
    return audio_buffer

async def main():
    
    print("Select your Voice")
    for i in range(3):
        print(f"Select {i+1} for {VOICES[i]}")
    voice = input("Enter the number:")
    voice = int(voice)

    
    await tts_generate(TEXT, VOICES[voice-1])

if __name__ == "__main__":
    asyncio.run(main())