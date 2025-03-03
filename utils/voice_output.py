
# from gtts import gTTS
# import os
# import platform

# def speak_text(text, filename="audio/output.mp3"):
#     """Convert text to speech using gTTS and play the audio."""
#     os.makedirs("audio", exist_ok=True)

#     tts = gTTS(text=text, lang="en")
#     tts.save(filename)

#     # Play audio based on OS
#     if platform.system() == "Windows":
#         os.system(f"start {filename}")  # Windows
#     elif platform.system() == "Darwin":
#         os.system(f"afplay {filename}")  # macOS
#     else:
#         os.system(f"mpg321 {filename} &")  # Linux (ensure mpg321 is installed)
import pyttsx3

def speak_text(text):
    """Speak text directly without saving an MP3 file."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Adjust speed (default is 200)
    engine.setProperty('volume', 1.0)  # Set volume level
    engine.say(text)
    engine.runAndWait()
