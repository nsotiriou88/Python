#!/usr/bin/env python
import sqlite3
import os
import fnmatch
from PIL import Image, ImageTk

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter



def tag_refresh():
    tagsList.delete(0, tkinter.END)

    for tag in conn.execute("SELECT tags.tag FROM tags ORDER BY tags.tag"):
        tagsList.insert(tkinter.END, tag[0])


def get_anchors(event):
    lb = event.widget
    index = lb.curselection()[0]
    tag_name = lb.get(index)

    # Get the anchor list from the database row
    alist = []
    for row in conn.execute("SELECT anchor FROM \"" + tag_name + "\" ORDER BY anchor"):
        alist.append(row[0])

    # # ===== Import PNG Images =====#REVIEW
    i = 1
    for anchor in alist:
        j = 1
        for key in measurements:
            path = conn.execute("SELECT \"" + key + "\" FROM \"" + tag_name + "\" WHERE anchor = \"" + anchor +"\"").fetchone()[0]
            photo = ImageTk.PhotoImage(Image.open(path))
            label = tkinter.Label(mainWindow, relief="sunken", image=photo)
            label.image = photo  # Keeping reference is needed!!!
            label.grid(row=i, column=j, sticky='nsew')
            j += 1
        i += 1


if __name__ == '__main__':
    measurements = ["dist", "rssi", "rssi2", "tqf", "tqf2"]
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

    # print(f for f in os.listdir(desktop + "/plots_data/") if fnmatch.fnmatch(f, '*.sqlite'))
    for f in os.listdir(desktop + "/plots_data/"):
        if fnmatch.fnmatch(f, '*.sqlite'):
            file = f
            print(file)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    conn = sqlite3.connect(desktop + '/plots_data/tag_plots.sqlite')
    print("Connected to database")

    # Main Window Loop for TKinter
    mainWindow = tkinter.Tk()
    mainWindow.title('Debug Tool')
    mainWindow.geometry('1600x1000')  #FIXME Possibly needs to optimise resolution at the end
    
    #DEBUG testing for Window Scroll
    # scbar = tkinter.Scrollbar(mainWindow)
    # scbar.grid(row=1, column=6, sticky='nsew', rowspan=10)
    # scbar.config( command = mainWindow.winfo_y )
    # mainWindow['yscrollcommand'] = scbar.set
    # scbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    #DEBUG testing ===== MAYBE ADDD EVERYTHING WITHIN ANOTHER FRAME, which is going to be
    #  the only one inside the window. Frames support Grid Structure.

    mainWindow.columnconfigure(0, weight=1)  # Tags column
    mainWindow.columnconfigure(1, weight=8)  # Distance column
    mainWindow.columnconfigure(2, weight=8)  # RSSI column
    mainWindow.columnconfigure(3, weight=8)  # RSSI2 column
    mainWindow.columnconfigure(4, weight=8)  # TQF column
    mainWindow.columnconfigure(5, weight=8)  # TQF2 column
    mainWindow.columnconfigure(6, weight=1)  # spacer column on right

    mainWindow.rowconfigure(0, weight=2)  # Row for the labels 
    mainWindow.rowconfigure(1, weight=8)  
    mainWindow.rowconfigure(2, weight=8)
    mainWindow.rowconfigure(3, weight=8)
    mainWindow.rowconfigure(4, weight=8)
    mainWindow.rowconfigure(5, weight=8)
    mainWindow.rowconfigure(6, weight=8)
    mainWindow.rowconfigure(7, weight=8)
    mainWindow.rowconfigure(8, weight=8)
    mainWindow.rowconfigure(9, weight=8)
    mainWindow.rowconfigure(10, weight=8)  # Up to 17 rows for the Master + 16 Anchors
    mainWindow.rowconfigure(11, weight=8)
    mainWindow.rowconfigure(12, weight=8)
    mainWindow.rowconfigure(13, weight=8)
    mainWindow.rowconfigure(14, weight=8)
    mainWindow.rowconfigure(15, weight=8)
    mainWindow.rowconfigure(16, weight=8)
    mainWindow.rowconfigure(17, weight=8)
    mainWindow.rowconfigure(18, weight=1)  # Row for the buttons

    # ===== labels =====
    tkinter.Label(mainWindow, text="Live Tags").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Distances").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="RSSI").grid(row=0, column=2)
    tkinter.Label(mainWindow, text="RSSI2").grid(row=0, column=3)
    tkinter.Label(mainWindow, text="TQF").grid(row=0, column=4)
    tkinter.Label(mainWindow, text="TQF2").grid(row=0, column=5)

    # ===== Live Tags Listbox =====
    # tagsList = DataListBox(mainWindow, conn, "tags", "tag", sort_order=("tag",), background='yellow')
    tagsList = tkinter.Listbox(mainWindow, background='yellow')
    tagsList.grid(row=1, column=0, sticky='nsew', rowspan=8, padx=(10, 0))
    tagsList.config(border=2, relief='sunken')

    for tag in conn.execute("SELECT tags.tag FROM tags ORDER BY tags.tag"):
        tagsList.insert(tkinter.END, tag[0])

    # Scrolling feature (Removed from Class)
    tagScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=tagsList.yview)
    tagScroll.grid(row=1, column=0, sticky='nse', rowspan=8)
    tagsList['yscrollcommand'] = tagScroll.set

    tagsList.bind('<<ListboxSelect>>', get_anchors)

    # ===== Adding a refresh Button for Tags =====#TODO
    tagRefresh_button = tkinter.Button(mainWindow, text="Refresh List", command=tag_refresh)
    tagRefresh_button.grid(row=9, column=0, sticky='ew', padx=(10, 0))

    # Stop Main Window Loop
    mainWindow.mainloop()

    conn.close()
    print("closing database connection")
