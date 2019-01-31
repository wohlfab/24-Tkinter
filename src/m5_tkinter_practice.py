"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Brandon Wohlfarth.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    window = tkinter.Tk()
    window.title("Classwork")


    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    frame1 = ttk.Frame(window, padding= 20)
    frame1.grid()

    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    bohdan_button = ttk.Button(frame1, text = 'Bohdan')
    bohdan_button.grid(row = 0, column = 0)

    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    bohdan_button['command'] = (lambda: print('Hello'))

    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    entry = ttk.Entry(frame1)
    entry.grid()
    button2 = ttk.Button(frame1, text = 'Print')
    button2['command'] = (lambda: print_box(entry.get()))
    button2.grid()
    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    entry2 = ttk.Entry(frame1)
    entry2.grid()
    button3 = ttk.Button(frame1, text='times')
    button3['command'] = (lambda: print_box_times(entry.get(), entry2.get()))
    button3.grid()
    # -------------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------
    window.mainloop()

def print_box(m):
    if m == "ok":
        print('Goodbye')
    else:
        print('Hello')
def print_box_times(m, n):
    for k in range(int(n)):
        print(m)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
