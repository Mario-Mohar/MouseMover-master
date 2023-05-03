import pyautogui
import time
import tkinter as tk
import threading

def move_mouse(stop_moving):
    for i in range(10):
        pyautogui.moveRel(10, 0, duration=0.25)
        pyautogui.moveRel(0, 10, duration=0.25)
        pyautogui.moveRel(-10, 0, duration=0.25)
        pyautogui.moveRel(0, -10, duration=0.25)
        if stop_moving():
            break

def start_moving(stop_moving, interval):
    start_button.config(state='disabled')
    stop_button.config(state='normal')
    while not stop_moving():
        move_mouse(stop_moving)
        time.sleep(interval)
    start_button.config(state='normal')
    stop_button.config(state='disabled')

def stop_moving():
    root.quit()

def start_button_clicked():
    interval = int(interval_entry.get())
    stop_moving_flag = lambda: stop_moving
    threading.Thread(target=start_moving, args=(stop_moving_flag, interval)).start()
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_button_clicked():
    stop_moving()

root = tk.Tk()
root.title("Mouse Mover")

interval_label = tk.Label(root, text="Interval (seconds):")
interval_label.grid(row=0, column=0)

interval_entry = tk.Entry(root)
interval_entry.grid(row=0, column=1)

start_button = tk.Button(root, text="Start", command=start_button_clicked)
start_button.grid(row=1, column=0)

stop_button = tk.Button(root, text="Stop with command + C", command=stop_button_clicked, state='disabled')
stop_button.grid(row=1, column=1)

root.protocol("WM_DELETE_WINDOW", stop_moving)

root.mainloop()
