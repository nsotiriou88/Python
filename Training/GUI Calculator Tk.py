try:
    import tkinter   # python 3
except ImportError:  # python 2
    import Tkinter as tkinter

import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = 8

label= tkinter.Label(mainWindow, text="Tkinter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='groove')
for zone in os.listdir('/usr/bin'): # '/Windows/System32'
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set

# frame for the radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky='ne')

rbValue = tkinter.IntVar()
rbValue.set(2)
# Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')


# Widget to display the result
resultLabel = tkinter.Label(mainWindow, text="Result")
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')

# Frame for the time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky='new')
# Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0, 24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
secondSpinner = tkinter.Spinbox(timeFrame, width=2, from_=0, to=59)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)
timeFrame['padx'] = 36

# Frame for the date spinners
dateFrame = tkinter.Frame(mainWindow)
dateFrame.grid(row=4, column=0, sticky='new')
# Date labels
dayLabel = tkinter.Label(dateFrame, text="Day")
monthLabel = tkinter.Label(dateFrame, text="Month")
yearLabel = tkinter.Label(dateFrame, text="Year")
dayLabel.grid(row=0, column=0, sticky='w')
monthLabel.grid(row=0, column=1, sticky='w')
yearLabel.grid(row=0, column=2, sticky='w')
# Date spinners
daySpin = tkinter.Spinbox(dateFrame, width=5, from_=1, to=31)
monthSpin = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
yearSpin = tkinter.Spinbox(dateFrame, width=5, from_=2000, to=2099)
daySpin.grid(row=1, column=0)
monthSpin.grid(row=1, column=1)
yearSpin.grid(row=1, column=2)

# Buttons
okButton = tkinter.Button(mainWindow, text="OK")
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.destroy)
okButton.grid(row=4, column=3, sticky='e')
cancelButton.grid(row=4, column=4, sticky='w')

mainWindow.mainloop()

print(rbValue.get())


# =========== CHALLENGE ===========
# # Write a GUI program to create a simple calculator
# # layout that looks like the screenshot.
# #
# # Try to be as Pythonic as possible - it's ok if you
# # end up writing repeated Button and Grid statements,
# # but consider using lists and a for loop.
# #
# # There is no need to store the buttons in variables.
# #
# # As an optional extra, refer to the documentation to
# # work out how to use minsize() to prevent your window
# # from being shrunk so that the widgets vanish from view.
# #
# # Hint: You may want to use the widgets .winfo_height() and
# # winfo_width() methods, in which case you should know that
# # they will not return the correct results unless the window
# # has been forced to draw the widgets by calling its .update()
# # method first.
# #
# # If you are using Windows you will probably find that the
# # width is already constrained and can't be resized too small.
# # The height will still need to be constrained, though.


# keys = [[('C', 1), ('CE', 1)],
#         [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
#         [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
#         [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
#         [('0', 1), ('=', 1), ('/', 1)],
#         ]

# mainWindowPadding = 8

# mainWindow = tkinter.Tk()
# mainWindow.title("Calculator")
# mainWindow.geometry('640x480-8-200')
# mainWindow['padx'] = mainWindowPadding

# result = tkinter.Entry(mainWindow)
# result.grid(row=0, column=0, sticky='nsew')

# keyPad = tkinter.Frame(mainWindow)
# keyPad.grid(row=1, column=0, sticky='nsew')

# row = 0
# for keyRow in keys:
#     col = 0
#     for key in keyRow:
#         tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
#         col += key[1]
#     row += 1

# mainWindow.update()
# # Creating a window with a certain Max and Min size. If they are the same, we have one size.
# mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())
# mainWindow.maxsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())

# mainWindow.mainloop()
