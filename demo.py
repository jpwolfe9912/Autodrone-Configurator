import tkinter as tk
from tkinter import ttk

import serial
from serial.tools import list_ports

root = tk.Tk()
msg = tk.StringVar()


def greet():
    print(msg.get())

    serial.Serial()


def main():
    root.title("Autodrone Configurator")

    # frames
    mainframe = tk.Frame(root)
    mainframe.pack()

    tk.Entry(mainframe, textvariable=msg).grid(row=0, column=0)
    ttk.Button(mainframe, text="Click Me!", command=greet).grid(row=0, column=1)

    choicesvar = tk.StringVar(value=list_ports.comports())
    l = tk.Listbox(mainframe, listvariable=choicesvar)
    l.grid(row=1, column=0, columnspan=2)

    if(l.selection_includes(2)):
        print("Selected 2!")

    root.mainloop()


if __name__ == '__main__':
    main()
