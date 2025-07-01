
import speech_recognition as sr

def listen_to_user():
    r = sr.Recognizer()
    r.pause_threshold = 1.2       # Wait a bit longer before assuming user is done speaking
    r.energy_threshold = 300      # Adjust if it's missing quiet voices; higher = less sensitive

    with sr.Microphone() as source:
        print("Listening patiently... please speak.")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)  # waits up to 5s to start speaking, allows 10s speech
        except sr.WaitTimeoutError:
            return "Sorry, I didn't hear anything."

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError:
        return "Sorry, there was a problem with the recognition service."