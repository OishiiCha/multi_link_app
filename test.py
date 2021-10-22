from tkinter import *

setwindow = Tk()
setwindow.geometry("700x300")
setwindow.title("Settings")
setwindow.configure(background='light grey')
setwindow.resizable(width=False, height=False)
setwindow.iconbitmap('data/links.ico')

frame1 = LabelFrame(setwindow, text="test frame", bg='light grey', font=('arial', 15, 'bold'), padx=5, pady=5)
frame1.pack(padx=10, pady=10)

b = Button(frame1, text="click me")
b.pack()


if __name__ == '__main__':
    setwindow.mainloop()