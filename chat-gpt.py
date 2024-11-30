import speech_recognition as sr
import pyttsx3
import openai
from datetime import datetime

# Initializing pyttsx3
engine = pyttsx3.init()

# Set your OpenAI API key and customize ChatGPT role
openai.api_key = "xyz"
messages = [{"role": "system", "content": "Your name is Rocky and give answers in 2 lines"}]

# Function to get response from OpenAI
def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    assistant_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply

# Function to listen and process user input
def listen_and_respond():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5.0)
            user_input = recognizer.recognize_google(audio)
            print(f"User: {user_input}")

            if "rocky" in user_input.lower():
                assistant_reply = get_response(user_input)
                print(f"Rocky: {assistant_reply}")
                engine.setProperty('rate', 120)
                engine.setProperty('volume', 1.0)
                engine.say(assistant_reply)
                engine.runAndWait()
            else:
                print("Didn't recognize 'Rocky' in the input.")
        except sr.UnknownValueError:
            print("Didn't understand the audio.")
        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
        except Exception as e:
            print(f"Error: {e}")

# Main loop for continuous listening
if __name__ == "__main__":
    print("Say 'Rocky' to interact with the assistant. Press Ctrl+C to exit.")
    try:
        while True:
            listen_and_respond()
    except KeyboardInterrupt:
        print("\nExiting... Goodbye!")
