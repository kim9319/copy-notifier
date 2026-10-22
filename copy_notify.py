from tkinter import *
import keyboard
import pyperclip
import pystray
from PIL import Image
import threading
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
count =0
last_copy =''
def show_window(icon, item):
    window.deiconify()

def hide_window(icon, item):
    window.withdraw()

def quit_app(icon, item):
    print("App closed")
    icon.stop()
    window.quit()
    window.destroy()
window = Tk()#initialize window
window.title("Notify window")
icon = PhotoImage(file=resource_path('save.png'))
window.iconphoto(True,icon)
window.config(background="#141313")
window.overrideredirect(True)
window.withdraw()#hide
image = Image.open(resource_path("save.png"))

tray_icon = pystray.Icon(
    "ClipboardNotifier",
    image,
    "Clipboard Notifier",
    menu=pystray.Menu(
        pystray.MenuItem("Show", show_window),
        pystray.MenuItem("Hide", hide_window),
        pystray.MenuItem("Exit", quit_app)
    )
)
frame = Frame(window, bg="#141313")
frame.pack(fill="x", padx=10, pady=10)

label = Label(
    frame,
    font=("Arial", 12),
    fg="#00ff48",
    bg="#141313",
    anchor="w"
)

label.pack(side=LEFT)

label2 = Label(
    frame,
    font=("Arial", 10, "bold"),
    fg="#141313",
    bg="#00ff48",
    padx=8,
    pady=2
)

label2.pack(side=RIGHT)

def delay_copy():
    window.after(200,copy_control)

def copy_control():
    clipboard_content = pyperclip.paste()
    clipboard_content=clipboard_content.strip()
    clipboard_content=clipboard_content.replace("\n", "")
    if len(clipboard_content) >20:
        clipboard_content = clipboard_content[:20] + "..."
    else:
        clipboard_content = clipboard_content
    print(clipboard_content)
    window.withdraw()
    window.lift()
    window.deiconify()
    window.attributes("-topmost", True)
    global count
    global last_copy
    if clipboard_content == last_copy:
        
        count = count+1
        print(count)
    else:
        count =0
        last_copy = clipboard_content
        print(count)
    label2.config(text=f"+{count}")
    label.config(text=f"📋Copied :{clipboard_content}")
    print(clipboard_content)
    window.after(3000,window.withdraw)


keyboard.add_hotkey("ctrl+c",delay_copy)

window.geometry("300x50+60-90") 
threading.Thread(target=tray_icon.run, daemon=True).start()
window.mainloop()#show window 