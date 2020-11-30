import tkinter.messagebox
from tkinter import *
from system_info import sysinfo



sysdata = sysinfo.sysInfo
  
root = Tk()


root.title("Minerva Custom Utility") 
root.geometry("350x400")
root.resizable(False, False)
root.iconbitmap('icon.ico')

menu = Menu(root)
root.config(menu=menu)

def abt():
    tkinter.messagebox.showinfo("About", '''
Author : Shravan Kumar Yadav
''')
    pass

menu1 = Menu(menu)
menu.add_cascade(label="File", menu=menu1)
menu1.add_command(label="Exit", command=root.destroy)

menu2 = Menu(menu)
menu.add_cascade(label="Options", menu=menu2)
menu2.add_command(label="About", command=abt())

manu_label = Label(root, text="Manufacturer")
manu_label.config(font=("Arial", 12), pady=5)

manu_text = Text(root, height=1, width=50, font="Arial", pady=2)
manu_text.insert(END, f"{sysdata['Manufacturer']}")
manu_text.config(state="disabled")

mod_label = Label(root, text="Model")
mod_label.config(font=("Arial", 12))

mod_text = Text(root, height=1, width=50, font="Arial", pady=2)
mod_text.insert(END, f"{sysdata['Model']}")
mod_text.config(state="disabled")

cpu_label = Label(root, text="Processor")
cpu_label.config(font=("Arial", 12))

cpu_text = Text(root, height=1, width=50, font="Arial", pady=2)
cpu_text.insert(END, f"{sysdata['Processor']}")
cpu_text.config(state="disabled")

ram_label = Label(root, text="RAM")
ram_label.config(font=("Arial", 12))

ram_text = Text(root, height=1, width=50, font="Arial", pady=2)
ram_text.insert(END, f"{sysdata['Ram_Size']} {sysdata['Ram_Type']}")
ram_text.config(state="disabled")

hdd_label = Label(root, text="HDD")
hdd_label.config(font=("Arial", 12))

hdd_text = Text(root, height=1, width=50, font="Arial", pady=2)
hdd_text.insert(END, f"{sysdata['HD Size']}")
hdd_text.config(state="disabled")

sr_label = Label(root, text="Serial Number")
sr_label.config(font=("Arial", 12))

sr_text = Text(root, height=1, width=50, font="Arial", pady=2)
sr_text.insert(END, f"{sysdata['Serial_Number']}")
sr_text.config(state="disabled")


manu_label.pack()
manu_text.pack()
mod_label.pack()
mod_text.pack()
cpu_label.pack()
cpu_text.pack()
ram_label.pack()
ram_text.pack()
hdd_label.pack()
hdd_text.pack()
sr_label.pack()
sr_text.pack()


mainloop()