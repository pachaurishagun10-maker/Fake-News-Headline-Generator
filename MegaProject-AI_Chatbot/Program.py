import pyautogui
import pyperclip
import time
pyautogui.FAILSAFE = False
# 1. Click the icon
pyautogui.click(329,97)

# Give the UI a moment to respond
time.sleep(1)

# 2. Drag 
pyautogui.moveTo(329,97, duration=0.2)
pyautogui.dragTo(1189,669 , duration=0.8, button="left")

# 3. Copy the selected text
pyautogui.hotkey("ctrl", "c")
pyautogui.click(1189,669)
# Give the clipboard time to update
time.sleep(0.3)

# 4. Get the copied text into a variable
text = pyperclip.paste()

print(text)