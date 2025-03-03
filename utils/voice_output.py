
import pyttsx3

def speak_text(text):
    """Speak text directly without saving an MP3 file."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speed (default is 200)
    engine.setProperty('volume', 1.0)  # Set volume level
    engine.say(text)
    engine.runAndWait()
