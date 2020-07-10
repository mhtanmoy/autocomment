import pyautogui
import time

comment = ["wow","cool capture","Rating 10/10","Winner here","Nice picture","Best yammy food","so good you are the best"]

time.sleep(5)

for i in range(10):
    pyautogui.typewrite(comment[1%7])
    pyautogui.typewrite("\n")
    time.sleep(2)