import pyautogui
import threading
import keyboard
import random
import time
event = threading.Event()
def stop():
    event.set()
    print("stop")
keyboard.add_hotkey("ctrl+esc", stop)
while not event.is_set():
    flag = random.randint(0, 1)
    if flag:
        x = random.randint(400, 800)
        y = random.randint(300, 500)
        pyautogui.click(x,y)
    time.sleep(1)
    if keyboard.is_pressed('s'):
        break
    if flag:
        pyautogui.hotkey("alt", "tab")
        time.sleep(1)
    pyautogui.scroll(10)
    pyautogui.scroll(10)
    pyautogui.scroll(10)
    pyautogui.scroll(10)
    time.sleep(1)