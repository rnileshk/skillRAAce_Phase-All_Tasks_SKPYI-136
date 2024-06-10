import tkinter as tk
import time

def start_timer():
    try:
        total_time = int(entry.get())
    except ValueError:
        display_label.config(text="Please enter a valid number.")
        return

    for remaining in range(total_time, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        display_label.config(text=timer)
        root.update()
        time.sleep(1)
    
    display_label.config(text="Time's up!")

root = tk.Tk()
root.title("Countdown Timer")

entry_label = tk.Label(root, text="Enter time in seconds:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack()

display_label = tk.Label(root, font=('Helvetica', 48))
display_label.pack()

root.mainloop()