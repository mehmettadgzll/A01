import pyautogui
import time
import tkinter as tk
import threading

# Göndermek istediğin mesaj
message = "Merhaba, bu otomatik bir mesaj!"

def write_message():
    time.sleep(3)  # Mesajı yazmaya başlamadan önce 3 saniye bekle
    while True:
        pyautogui.typewrite(message + '\n', interval=0.05)  # Mesajı daha yavaş yaz
        time.sleep(1)  # Mesajlar arasında 1 saniye bekle

def on_click():
    # Yeni bir thread başlat
    threading.Thread(target=write_message, daemon=True).start()

# Tkinter GUI oluşturma
root = tk.Tk()
root.title("Mesaj Yazıcı")

# Buton oluşturma
send_button = tk.Button(root, text="Tetikle", command=on_click)
send_button.pack(pady=20)

# GUI'yi çalıştırma
root.mainloop()
