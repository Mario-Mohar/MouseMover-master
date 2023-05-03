import pyautogui
import time
import tkinter as tk
import keyboard
import threading

def move_mouse():
    i=0
    while i<10:
        pyautogui.moveRel(10, 0, duration=0.25)
        pyautogui.moveRel(0, 10, duration=0.25)
        pyautogui.moveRel(-10, 0, duration=0.25)
        pyautogui.moveRel(0, -10, duration=0.25)
        i+=1
        if keyboard.is_pressed('ctrl+c'):  # if key 'ctrl+c' is pressed 
            break  # finishing the loop

def start_moving():
    global stop_moving
    start_button.config(state='disabled')
    stop_button.config(state='normal')
    interval = int(interval_entry.get())
    while not stop_moving:
        move_mouse()
        time.sleep(interval)
    start_button.config(state='normal')
    stop_button.config(state='disable')
    stop_moving = False
    


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