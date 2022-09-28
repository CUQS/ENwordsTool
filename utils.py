import pyperclip
import pyautogui
from datetime import datetime

def get_clipboard_text():
    data = pyperclip.paste()
    return data

def get_mouse_pos():
    pos = pyautogui.position()
    return "800x400+"+str(pos[0]-800)+"+"+str(pos[1]-15)

def copy_to_clipboard(text):
    pyperclip.copy(text)

def copy_time_to_clipboard():
    paste_time()
    # remove_newline()

def paste_time():
    now = datetime.now()
    # YYYY/mm/dd/ H:M:S
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
    copy_to_clipboard("**" + dt_string + "**")

def remove_newline():
    data = get_clipboard_text()
    copy_to_clipboard(data.replace("\n","").replace("-\r", "").replace("\r", " "))