import tkinter
from tkinter import Menu
from tkinter import filedialog
from tkinter import messagebox

Window = tkinter.Tk()

def AskForMap():
    a = filedialog.askopenfile(filetypes=[("Map Files", "*.szs")])
    messagebox.showinfo(title="Succses", message=a.name + "Has been opened!")

Window.title("Shroom")
Window.geometry("1200x800")
small_icon = tkinter.PhotoImage(file=r"UI/Icon.png")
large_icon = tkinter.PhotoImage(file=r"UI/Icon.png")
Window.iconphoto(False, large_icon, small_icon)
menubar= Menu(Window)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label="New", command=None)
file.add_command(label="Open Map", command=AskForMap)
file.add_command(label="Save", command=None)
file.add_separator()
file.add_command(label="Exit", command= Window.destroy)
Window.config(menu=menubar)

tkinter.mainloop()