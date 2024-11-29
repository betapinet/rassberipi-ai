import speech_recognition as sr
import pyttsx3
import openai
import pyodbc
from datetime import datetime

# Initializing pyttsx3
listening = True
engine = pyttsx3.init()

# Set your OpenAI API key and customizing the chatGPT role
openai.api_key = "xyz"
messages = [{"role": "system", "content": "Your name is Rocky and give answers in 2 lines"}]

# Database connection to SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=192.168.43.2;'
    'DATABASE=ChatLogs;'
    'UID=sa;'
    'PWD=123456;'
)
cursor = conn.cursor()

# Function to get response from OpenAI
def get_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    # Store the conversation in the database
    save_conversation(user_input, ChatGPT_reply)

    return ChatGPT_reply

# Function to save conversation to SQL Server
def save_conversation(user_input, assistant_response):
    try:
        query = """
        INSERT INTO Conversations (UserInput, AssistantResponse, Timestamp)
        VALUES (?, ?, ?)
        """
        timestamp = datetime.now()
        cursor.execute(query, user_input, assistant_response, timestamp)
        conn.commit()
        print("Conversation saved to database.")
    except Exception as e:
        print(f"Error saving conversation: {e}")

# Listening and processing user input
while listening:
    with sr.Microphone() as source:
        recognizer = sr.Recognizer()
        recognizer.adjust_for_ambient_noise(source)
        recognizer.dynamic_energy_threshold = 3000

        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5.0)
            response = recognizer.recognize_google(audio)
            print(response)

            if "rocky" in response.lower():
                response_from_openai = get_response(response)
                engine.setProperty('rate', 120)
                engine.setProperty('volume', 1.0)
                engine.say(response_from_openai)
                engine.runAndWait()
            else:
                print("Didn't recognize 'Rocky'.")
        except sr.UnknownValueError:
            print("Didn't recognize anything.")
        except Exception as e:
            print(f"Error: {e}")
