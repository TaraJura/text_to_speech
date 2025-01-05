from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang="en")
    os.makedirs("output", exist_ok=True)
    filepath = os.path.join("output", filename)
    tts.save(filepath)
    print(f"Audio saved as {filepath}")

if __name__ == "__main__":
    text = input("Enter text to convert to speech: ")
    text_to_speech(text)
