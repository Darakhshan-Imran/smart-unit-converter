
import os
import whisper
import speech_recognition as sr
import streamlit as st


# Load the Whisper model
model = whisper.load_model("base")

def record_audio(filename="audio/user_input.wav"):
    """Record audio using SpeechRecognition and save it as WAV."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        # Save recorded audio
        os.makedirs("audio", exist_ok=True)
        with open(filename, "wb") as f:
            f.write(audio.get_wav_data())
    print(f"Audio saved to {filename}")  # Debugging line  
    return filename

def transcribe_audio(filename="audio/user_input.wav"):
    """Transcribe recorded audio using Whisper."""
    if not os.path.exists(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")

    # Transcribe the WAV file directly
    result = model.transcribe(filename)
    print(f"Transcription: {result['text']}")  # Debugging line
    return result["text"]

