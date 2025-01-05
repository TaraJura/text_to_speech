import pyttsx3

def text_to_speech_cz_local(text, filename="output.mp3"):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    for voice in voices:
        if "czech" in voice.name.lower():
            engine.setProperty("voice", voice.id)
            break
    engine.setProperty("rate", 150)  # Adjust speaking rate if needed
    engine.save_to_file(text, filename)  # Save output to an MP3 file
    engine.runAndWait()
    print(f"Audio saved as {filename}")

if __name__ == "__main__":
    text = input("Enter text to convert to speech: ")
    text_to_speech_cz_local(text)
