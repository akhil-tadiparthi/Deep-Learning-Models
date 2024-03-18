import datetime
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(f"You said: {said}")
        except Exception as e:
            print("Exception:", str(e))
    return said.lower()

def get_time():
    return datetime.datetime.now().strftime("%H:%M")

def personal_assistant():
    speak("Hello, I'm your personal assistant. How can I help you today?")
    while True:
        user_input = get_audio()
        print(user_input)
        if 'time' in user_input:
            current_time = get_time()
            speak(f"The current time is {current_time}")
        elif 'bye' in user_input:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to help with that.")

if __name__ == "__main__":
    personal_assistant()
