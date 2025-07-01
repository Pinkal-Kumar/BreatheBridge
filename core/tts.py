import pyttsx3

def speak_text(text, lang="en"):
    engine = pyttsx3.init()

    # Try to find a voice that supports the given language
    voices = engine.getProperty('voices')
    selected_voice = None

    for voice in voices:
        voice_langs = voice.languages if hasattr(voice, 'languages') else []
        voice_langs = [v.decode().lower() if isinstance(v, bytes) else v.lower() for v in voice_langs]

        if voice_langs and (lang.lower() in voice_langs or lang.lower() in voice.name.lower()):
            selected_voice = voice.id
            break

    # Fallback: use default voice
    if selected_voice:
        engine.setProperty('voice', selected_voice)

    # Optional: slower speech for clarity
    engine.setProperty('rate', 150)

    engine.say(text)
    engine.runAndWait()