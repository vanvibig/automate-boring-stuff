import pyautogui
import pyperclip
from PIL import ImageGrab
import time

unikey_icon = 'unikey-taskbar-vi.png'

box = None
while not box:
    try:
        box = pyautogui.locateOnScreen(unikey_icon)
        center = pyautogui.center(box)
        pyautogui.click(center)
    except (IndexError, TypeError):
        unikey_icon = 'unikey-taskbar-en.png'
