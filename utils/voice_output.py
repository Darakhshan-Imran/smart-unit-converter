
# import pyttsx3

# def speak_text(text):
#     """Speak text directly without saving an MP3 file."""
#     engine = pyttsx3.init()
#     engine.setProperty('rate', 150)  # Adjust speed (default is 200)
#     engine.setProperty('volume', 1.0)  # Set volume level
#     engine.say(text)
#     engine.runAndWait()

from gtts import gTTS
import streamlit as st
import io
import base64

def speak_text(text):
    """Convert text to speech and play it without displaying an audio player."""
    tts = gTTS(text=text, lang="en")
    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)
    
    # Convert audio to base64
    audio_base64 = base64.b64encode(audio_stream.read()).decode("utf-8")
    audio_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
    """
    
    # Play audio using JavaScript
    st.markdown(audio_html, unsafe_allow_html=True)
