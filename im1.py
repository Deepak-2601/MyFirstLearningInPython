try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

main_window = tkinter.Tk()
main_window.title("Hello world")
main_window.geometry("800x400+788+290")
label = tkinter.Label(main_window, text="Hello world")
label.pack(side="top")
canvas = tkinter.Canvas(main_window, relief='raised', borderwidth=10)
canvas.pack (side="right", fill=tkinter.Y)
main_window.mainloop()
