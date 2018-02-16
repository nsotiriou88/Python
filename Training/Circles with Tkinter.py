import math

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

import time


# def parablola(x):
#     y = x * x / 100
#     return y
def parabola(page, size):
    for x in range(size):
        y = x * x / size
        # In this way, we have a smaller loop
        plot(page, x, y)
        plot(page, -x, y)


# Xc and Yc are the coordinates of the circle's centre(x, y)->(Xc, Yc)
def circle(page, radius, Xc, Yc, colour="red"):
    page.create_oval(Xc + radius, Yc + radius, Xc - radius, Yc - radius, outline=colour, width=2)

    # # This is for the circle function, but it leaves spaces at the sides of the circle.
    # # We can also try to do it better manually, by multipling and dividing with 100
    # # afterwards, so that we take more samples and the circle is better difined. It is slow.
    # for x in range(Xc * 100, (Xc + radius) * 100): # using this for better cirlces, but slow
    # for x in range(Xc, Xc + radius):
    #     y = Yc + (math.sqrt(radius ** 2 - ((x-Xc) ** 2)))
    #     # Top right, bottom right, top left and bottom left quadrants of the circle
    #     plot(page, x, y)
    #     plot(page, x, 2 * Yc - y)
    #     plot(page, 2 * Xc - x, y)
    #     plot(page, 2 * Xc - x, 2 * Yc  - y)


def draw_axes(page):
    page.update()
    # The values of the origin for setting it later
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    # Setting up the origin (-x, -y, x, y). Two diagonal conrers/edges
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    # Setting up the horizontal and vertical lines (4 quadrants)
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    # Printing local values for debugging
    print(locals())

def plot(canvasf, x, y):
    # We place -y because the Canvas starts its values from top (therefore all negative).
    # We also need another point to draw the line, so, we add +1 to the given point
    canvasf.create_line(x, -y, x + 1, -y + 1, fill="red")
    # This is for drawing in slow motion
    time.sleep(0.001)
    canvasf.update()


mainWindow = tkinter.Tk()

mainWindow.title("Parabola")
mainWindow.geometry("640x480")

# canvas = tkinter.Canvas(mainWindow, width=320, height=480)
canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
# canvas2.grid(row=0, column=1)

# print(repr(canvas), repr(canvas2))
print(repr(canvas))
draw_axes(canvas)
# draw_axes(canvas2)

# for x in range(-100, 101):
#     y = parablola(x)
#     plot(canvas, x, y)
parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100, "green")
circle(canvas, 100, 100, -100, "yellow")
circle(canvas, 100, -100, 100, "black")
circle(canvas, 100, -100, -100, "blue")
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)

mainWindow.mainloop()
