import pyautogui as pag
import cv2 as cv
import sys, time
import random


# moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort the program:
pag.FAILSAFE = True
time.sleep(2.5)


def mining():
    rock_location = pag.locateOnScreen('images/rock.png', confidence=0.8)
    click_count = 0

    north_rock = pag.center(rock_location)
    rock_x, rock_y = north_rock
    return pag.click(rock_x, rock_y)


def random_click():
    """
    Returns a random +/- pixel value to be attached to a xy location
    for randomization of clicks 
    """
    pass


def check_inv():
    pass


def position_camera():
    pass


mining()