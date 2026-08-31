import os
import time
import pyautogui
import pyperclip

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


# 1. Click the icon
pyautogui.click(329, 97)

time.sleep(0.5)


# 2. Select the text
pyautogui.moveTo(329, 97, duration=0.2)
pyautogui.dragTo(1189, 669, duration=0.8, button="left")

time.sleep(0.2)


# 3. Copy selected text
pyautogui.hotkey("ctrl", "c")

time.sleep(0.5)


# 4. Get copied text
text = pyperclip.paste()

print("Copied Text:", text)


# 5. Send text to AI
def aiProcess(command_text):

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a person named Juhu who speaks Hindi and English. "
                    "You are from India and you are an engineer. "
                    "Analyze the chat history and respond like Juhu."
                )
            },
            {
                "role": "user",
                "content": command_text
            }
        ]
    )

    return completion.choices[0].message.content


# 6. Get AI response
response = aiProcess(text)

print("AI Response:", response)