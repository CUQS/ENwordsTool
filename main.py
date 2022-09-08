import tkinter as tk
from tkinter import ttk
import keyboard, time
import win32clipboard
import pyautogui
import requests
from bs4 import BeautifulSoup


SEARCH_NUM = 30


def getHTMLText(url, headers=None, params=None):
	if headers is None:
		headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17'}
	try:
		r = requests.get(url, timeout=10, headers=headers, params=params)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "error"

def get_clipboard_text():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return data

def get_mouse_pos():
    pos = pyautogui.position()
    return "800x400+"+str(pos[0]-800)+"+"+str(pos[1]-15)


def main():
    text = get_clipboard_text()
    print("searching %s..." % text)
    position=get_mouse_pos()

    html_text = getHTMLText("https://www.wordhippo.com/what-is/another-word-for/%s.html" % text)

    soup = BeautifulSoup(html_text, 'html.parser')
    count = 0

    syn_words = ['' for i in range(SEARCH_NUM)]
    for div in soup.find_all("div", class_="relatedwords"):
        for a in div.find_all("div", class_="wb"):
            syn_words[count] = a.text
            count += 1
            if count == SEARCH_NUM:
                break
        if count == SEARCH_NUM:
            break

    root = tk.Tk()
    root.title("Synonyms")
    root.wm_attributes('-topmost',1)
    root.geometry(position)

    for idx, word in enumerate(syn_words):
        ent = tk.Entry(root, state='readonly', font=("Arial", 15))
        var = tk.StringVar()
        var.set(word)
        ent.config(textvariable=var, relief='flat')
        ent.grid(row=idx//3, column=idx%3, sticky="nsew")

    # frame = tk.Frame(root)
    # tree = ttk.Treeview(frame, columns=(1, 2, 3), show='headings', height=4)

    # tree.heading(1, text="")
    # tree.heading(2, text="")
    # tree.heading(3, text="")

    # for idx, row in enumerate(table):
    #     tree.insert(parent='', index=idx, iid=idx, values=row)

    # style = ttk.Style()
    # style.theme_use("default")
    # style.map("Treeview")
    # scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    # tree.configure(yscroll=scrollbar.set)

    # frame.pack()
    # tree.pack(side=tk.LEFT)
    # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    root.mainloop()

    # top = tk.Tk()
    # top.wm_attributes('-topmost',1)
    # top.geometry(position)
    # e=tk.Text(font=("Arial", 15))
    # e.insert(1.0,tabulate(table))
    # e.pack()
    # top.mainloop()

    return


if __name__ == "__main__":
    while True:
        a = keyboard.read_event()
        if a.name == "esc": break
        elif a.event_type == "down":
            if a.name == "ctrl":
                t = time.time()
                b = keyboard.read_event()
                if b.name == "c":
                    c = keyboard.read_event()
                    while not c.event_type == "up":
                        c = keyboard.read_event()
                        dura = time.time() - t
                        if dura > 1:
                            main()
                            break
