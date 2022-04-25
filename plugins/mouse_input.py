import os
import time
import json
from pynput import mouse

data_store = []

total_recordings = 0
n_recordings = 0

def on_click(x, y, button, pressed):
    global total_recordings
    if pressed:
            data_store.append({
                "x": x,
                "y": y,
                "button": str(button),
                "time": time.time()
            })
            print(x, y)

            total_recordings+=1
        # Stop listener
            if n_recordings:
                if total_recordings >= n_recordings:
                    return False

def on_scroll(x, y, dx, dy):
    save()
    return False


def save():
    data = json.dumps(data_store)
    with open('data/data.json', 'w+') as file:
        file.write(data)

# Collect events until released
with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
