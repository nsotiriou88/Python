import sys
import termios
import atexit
from select import select

# save the terminal settings
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# new terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

# switch to normal terminal
def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

# switch to unbuffered terminal
def set_curses_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

def putch(ch):
    sys.stdout.write(ch)

def getch():
    return sys.stdin.read(1)

def getche():
    ch = getch()
    putch(ch)
    return ch

def kbhit():
    dr,dw,de = select([sys.stdin], [], [], 0)
    #    return dr <> []
    return dr

# if __name__ == '__main__':
#     atexit.register(set_normal_term)
#     set_curses_term()
#     while 1:
#         if kbhit():
#             ch = getch()
#             break
#         sys.stdout.write('Hello! \n')

atexit.register(set_normal_term)
set_curses_term()
for i in range(0, 4):

    while 1:
        if kbhit():
            ch = getch()
            break
        sys.stdout.write('Hello! \n')

print('done')

########################################

####### Olli's Solution #######

# import tty
# import sys
# import termios
#
# orig_settings = termios.tcgetattr(sys.stdin)
#
# tty.setraw(sys.stdin)
# x = 0
# while x != chr(27): # ESC
#     x = sys.stdin.read(1)[0]
#     print("You pressed", x)
#
# termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
