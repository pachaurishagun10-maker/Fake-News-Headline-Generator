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


# Text/chat area
SELECT_START_X = 329
SELECT_START_Y = 97

SELECT_END_X = 1189
SELECT_END_Y = 669

# IMPORTANT:
# Put the coordinates of the message/reply input box here
INPUT_X = 600
INPUT_Y = 700

def aiProcess(command_text):

    completion = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are Juhu, an Indian engineer who naturally speaks "
                    "Hindi and English. Analyze the provided chat and reply "
                    "naturally like Juhu. Keep the response conversational "
                    "and respond to the latest incoming message."
                )
            },
            {
                "role": "user",
                "content": command_text
            }
        ]
    )

    return completion.choices[0].message.content


def getChatText():

    # Click/select the chat area
    pyautogui.click(SELECT_START_X, SELECT_START_Y)

    time.sleep(0.3)

    # Select text
    pyautogui.moveTo(
        SELECT_START_X,
        SELECT_START_Y,
        duration=0.2
    )

    pyautogui.dragTo(
        SELECT_END_X,
        SELECT_END_Y,
        duration=0.8,
        button="left"
    )

    time.sleep(0.2)

    pyautogui.hotkey("ctrl", "c")

    time.sleep(0.4)

    return pyperclip.paste()


def sendResponse(response):


    pyautogui.click(INPUT_X, INPUT_Y)

    time.sleep(0.2)


    pyperclip.copy(response)


    pyautogui.hotkey("ctrl", "v")

    time.sleep(0.2)

    pyautogui.press("enter")


print("Juhu Bot started...")
print("Waiting for Rio's message...")


last_text = ""

while True:

    try:

        text = getChatText()


        if not text.strip():
            time.sleep(2)
            continue


        if text != last_text:

            print("\nNew message detected!")
            print("Chat:", text)


            response = aiProcess(text)

            print("\nJuhu:", response)


            # Send response automatically
            sendResponse(response)

            last_text = text

            print("\nWaiting for next message...")


        # Check again after 2 seconds
        time.sleep(2)


    except KeyboardInterrupt:

        print("\nJuhu Bot stopped.")
        break


    except Exception as e:

        print("\nError:", e)

        time.sleep(5)