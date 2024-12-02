import pyautogui
import time
import tkinter as tk
import threading

# The message you want to send
message = "Hello, this is an automated message!"

def write_message():
    time.sleep(3)  # Wait 3 seconds before starting to write the message
    while True:
        pyautogui.typewrite(message + '\n', interval=0.05)  # Write the message slower
        time.sleep(1)  # Wait 1 second between messages

def on_click():
    # Start a new thread
    threading.Thread(target=write_message, daemon=True).start()

# Creating a Tkinter GUI
root = tk.Tk()
root.title("Mesaj Yazıcı")

# Create a button
send_button = tk.Button(root, text="Run", command=on_click)
send_button.pack(pady=20)

# Run the GUI
root.mainloop()
