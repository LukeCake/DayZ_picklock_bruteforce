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
hold_time = 0.2
# print(list)

def hold_key(key, hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.keyDown(key)

def one_loop():
    # print(loop_nuber_1)
    # print("Testuji 0 - 9 na kruhu")
    one_loop_count = 0
    list[3] = 0
    for i in range(0, 10):
        print(list)
        list[3] = list[3] + 1
        # print("ring_4: ", one_loop_count)
        Fone_loop_count = one_loop_count + 1
        hold_key('F', hold_time)
        # list[loop_nuber_1] = i+1
        # print(list)
        #for tesyt
        key = "-"
        keyboard.press(key)
        keyboard.release(key)

def change_loop(loop_numer_2):
    # print("mením císlo kruhu o - 1")
    list[2] = list[2] + 1
    # print(loop_numer_2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    for i in range(0,loop_numer_2+1):
        print("press F")
        key = "f"
        keyboard.press(key)
        keyboard.release(key)

    hold_key('F', hold_time)
    print("hold F")

    for i in range(loop_numer_2, 3):
        key = "f"
        keyboard.press(key)
        keyboard.release(key)
        print("press F")

def basic_change_loop(loop_number_3):
    for i in range (loop_number_3, 3):
        key = "f"
        keyboard.press(key)
        keyboard.release(key)
    hold_key('F', hold_time)

    for i in range (0, loop_number_3+1):
        key = "f"
        keyboard.press(key)
        keyboard.release(key)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def basic_change_loop_2():
    for i in range (0, 2):
        key = "f"
        keyboard.press(key)
        keyboard.release(key)
    hold_key('F', hold_time)

    for i in range (0, 2):
        key = "f"
        keyboard.press(key)
        keyboard.release(key)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def basic_change_loop_1():
    key = "f"
    keyboard.press(key)
    keyboard.release(key)
    hold_key('F', hold_time)

    for i in range (0, 2):
        key = "f"
        keyboard.press(key)
        keyboard.release(key)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

time.sleep(4)
loop_number = 0
counter = 0
loop_number_2 = 0

ring_1 = 0
# print("ring_1:", ring_1)
for i in range (0, 10):
    ring_2 = 0
    list[1] = 0
    # otestovat 10 číslic na kruhu x-9-x-x
    for i in range (0, 10):
        # print("ring_2:", ring_2)
        print(list)

        ring_3 = 0
        list[2] = 0
        # otestovat 10 číslic na kruhu x-x-9-9
        for i in range (0, 10):
            print(list)
            # print("ring_3:", ring_3)
            #otestovat 10 číslic na kruhu (4) x-x-x-9
            one_loop()
            #posun kruh (3) o jedno a vrt zpět na (4)
            basic_change_loop(counter)
            ring_3 = ring_3 + 1
            list[2] = list[2]+1
        basic_change_loop_2()
        # counter = counter +1
        ring_2 = ring_2 + 1
        list[1] = list[1]+1
    basic_change_loop_1()
    list[0] = list[0] + 1




# for i in range (0,9):
#     for i in range(0, 9):
#         for i in range(0, 9):
#             for i in range(0, 9):
#                 one_loop()




# for i in range (0,4):
#     loop_number = i
#     for i in range(0, 9):
#         #-0-0-0-X
#         loop_number = loop_number - 1
#         one_loop(loop_number)
#         #-0-0-X-0
#         change_loop(loop_number_2)
#         print("mením kruh na: ", i)
#         # change_loop(counter)
#         counter = counter + 1
#     loop_number_2 = loop_number_2 + 1



