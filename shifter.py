import pyautogui
width, height = pyautogui.size()

for i in range(10000):
      pyautogui.moveTo(100, 100, duration=0.25)

