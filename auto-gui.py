import pyautogui
import pyperclip
from PIL import ImageGrab

box = list(pyautogui.locateAllOnScreen('unikey-taskbar.png'))[0]
center = pyautogui.center(box)
pyautogui.click(center)

pyautogui.typewrite('Hello world!')
pyautogui.scroll(200)

pyperclip.copy("Hello World!")

left, top = (1658, 1038)
right, bottom = (1684, 1067)
# left, top, right, bottom = bbox
bbox2 = (left, top, right, bottom)
im = pyautogui.screenshot()
im = im.crop(bbox2)