try:
    import tkinter   # python 3
except ImportError:  # python 2
    import Tkinter as tkinter

# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

# ============ Example with button ===========

# class Application(tk.Frame):
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master)
#         self.grid()
#         self.createWidgets()

#     def createWidgets(self):
#         self.quitButton = tk.Button(self, text='Quit', command=self.quit)
#         self.quitButton.grid()

# app = Application()
# app.master.title('Sample application')
# app.mainloop()


# =========== My Example ===========
# mainWindow = tkinter.Tk()

# mainWindow.title("Hello World")
# # 4 parameters (resolution of the screen and with '+', where you want the pixel to appear)
# mainWindow.geometry('640x480+8+400')

# label = tkinter.Label(mainWindow, text="Hello Iron Man")
# label.pack(side='top')

# leftFrame = tkinter.Frame(mainWindow)
# leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

# canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.pack(side='left', anchor='n')

# rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='right', anchor='n', expand=True)
# button1 = tkinter.Button(rightFrame, text="button1")
# button2 = tkinter.Button(rightFrame, text="button2")
# button3 = tkinter.Button(rightFrame, text="button3")
# button1.pack(side='top')
# button2.pack(side='top')
# button3.pack(side='top')

# quit_button = tkinter.Button(mainWindow, text="Quit", command=quit)
# quit_button.pack(side='bottom')

# mainWindow.mainloop()


# ============ IMPLEMENTING GRID =============
mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480-8-200')

label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')

mainWindow.mainloop()
