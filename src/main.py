import pyautogui as pag
import cv2 as cv
import sys, time

"""
Plan -
    record mouse movment and click location with a input listner (json file)
    replay those movements/clicks
    add variation in the x and y locatoin of every click (curb detection)
"""

# moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort the program:
pag.FAILSAFE = True
time.sleep(2.5)

#fix camera location and position (othegraphic view)
north = [1725, 74]
pag.click(north)
#arrow key down for x time


#fishing_hole = pag.locateCenterOnScreen('fishing_hole.png', confidence = 0.8)

#print(fishing_hole)
#print("x: ", fishing_hole[0], " y: ", fishing_hole[1])

#pag.click(fishing_hole[0], fishing_hole[1])