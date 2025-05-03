from tkinter import *

window = Tk()
window.title("Using grid manager")
window.geometry("1920x1080")


yscrollbar = Scrollbar(window, orient=VERTICAL)


listbox = Listbox(window, height=30, width=80, yscrollcommand=yscrollbar.set)


listbox.grid(row=1, column=0, padx=10, pady=10, sticky="w")
yscrollbar.grid(row=1, column=1, sticky="ns")  # Place scrollbar next to the listbox


yscrollbar.config(command=listbox.yview)


for i in range(201):
    listbox.insert(END, f"Gold {i}")

window.mainloop()