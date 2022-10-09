#0,9 hold F
#left pres F
# hold 1 time
# left 3 times FFF
# 0,9
#
#
#


import pyautogui
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

list = [0, 0, 0, 0]
print(list)

def hold_key(key, hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.keyDown(key)

def one_loop(loop_nuber_1):
    print(loop_nuber_1)
    print("Testuji 0 - 9 na kruhu")
    for i in range(0, 9):
        hold_key('A', 0.2)
        # list[loop_nuber_1] = i+1
        print(list)
        #for tesyt
        key = "x"
        keyboard.press(key)
        keyboard.release(key)

def change_loop(loop_numer_2):
    print("mením císlo kruhu o - 1")
    list[2] = list[2] + 1
    print(loop_numer_2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    for i in range(0,loop_numer_2+1):
        print("press F")
        key = "f"
        keyboard.press(key)
        keyboard.release(key)

    hold_key('F', 0.2)
    print("hold F")

    for i in range(loop_numer_2, 3):
        key = "f"
        keyboard.press(key)
        keyboard.release(key)
        print("press F")

time.sleep(5)
loop_number = 0
counter = 0
loop_number_2 = 0

for i in range (0,4):
    loop_number = i
    for i in range(0, 9):
        #-0-0-0-X
        loop_number = loop_number - 1
        one_loop(loop_number)
        #-0-0-X-0
        change_loop(loop_number_2)
        print("mením kruh na: ", i)
        # change_loop(counter)
        counter = counter + 1
    loop_number_2 = loop_number_2 + 1



