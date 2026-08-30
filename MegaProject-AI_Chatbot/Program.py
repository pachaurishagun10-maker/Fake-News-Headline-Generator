import os
import time
import pyautogui
import pyperclip

from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
pyautogui.FAILSAFE = False
pyautogui.PAUSE=0
# 1. Click the icon
pyautogui.click(329,97)

# Give the UI a moment to respond
time.sleep(0.5)

# 2. Drag 
pyautogui.moveTo(329,97, duration=0.2)
pyautogui.dragTo(1189,669 , duration=0.8, button="left")

# 3. Copy the selected text
pyautogui.hotkey("ctrl", "c")
pyautogui.click(1189,669)
# Give the clipboard time to update
time.sleep(0.5)

# 4. Get the copied text into a variable
text = pyperclip.paste()

print("Copied Text:",text)

def aiProcess(command_text):
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system","content": "You are a person named Juhu who speaks hindi and english.He is from India and is a engineer.You analyze chat history and respond like Juhu"},
            
            {"role": "user","content":command_text}
        ]
    )

    return completion.choices[0].message.content
response=aiProcess(text) 
print("AI Response:",response)