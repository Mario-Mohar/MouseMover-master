import pyautogui
import time
import tkinter as tk
import keyboard
import threading
import signal

def move_mouse():
    i=0
    try:
        while i<10:
            pyautogui.moveRel(10, 0, duration=0.25)
            pyautogui.moveRel(0, 10, duration=0.25)
            pyautogui.moveRel(-10, 0, duration=0.25)
            pyautogui.moveRel(0, -10, duration=0.25)
            i+=1
    except KeyboardInterrupt:  # If CTRL+C is pressed, exit cleanly:
        global stop_moving
        stop_moving = True

def start_moving():
    global stop_moving
    start_button.config(state='disabled')
    stop_button.config(state='normal')
    interval = int(interval_entry.get())
    while not stop_moving:
        move_mouse()
        time.sleep(interval)
    start_button.config(state='normal')
    stop_button.config(state='disabled')
    stop_moving = False
    
def signal_handler(sig, frame):
    global stop_moving
    stop_moving = True
    pyautogui.alert('Mouse mover stopped')
    sys.exit(0)
    
signal.signal(signal.SIGINT, signal_handler)

root = tk.Tk()
root.title("Mouse Mover")
stop_moving = False

interval_label = tk.Label(root, text="Interval (seconds):")
interval_label.grid(row=0, column=0)

interval_entry = tk.Entry(root)
interval_entry.grid(row=0, column=1)

start_button = tk.Button(root, text="Start", command=lambda:threading.Thread(target=start_moving).start())
start_button.grid(row=1, column=0)

stop_button = tk.Button(root, text="Stop with command + C", state='disable')
stop_button.grid(row=1, column=1)

root.mainloop()