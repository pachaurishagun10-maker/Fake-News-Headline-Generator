import pyautogui
import pyperclip
import time

# 1. Click the icon
pyautogui.click(678, 591)

# Give the UI a moment to respond
time.sleep(1)

# 2. Drag from (842, 749) to (1304, 673) to select the text
pyautogui.moveTo(846, 584, duration=0.2)
pyautogui.dragTo(1045, 618, duration=0.8, button="left")

# 3. Copy the selected text
pyautogui.hotkey("ctrl", "c")

# Give the clipboard time to update
time.sleep(0.3)

# 4. Get the copied text into a variable
text = pyperclip.paste()

print(text)