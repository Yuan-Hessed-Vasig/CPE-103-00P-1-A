import tkinter as tk

def click(event):
    text = event.widget["text"]
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Colorful Calculator")


entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.SUNKEN, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")


buttons = [
    ["C"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-;"],
    ["0", ".", "+"],
    ["="]
]


for i, row in enumerate(buttons):
    col = 0
    for text in row:
        if text == "C":
            btn = tk.Button(root, text=text, font="Arial 18", bd=5, relief=tk.RAISED,
                            bg="black", fg="white", activebackground="darkred")
            btn.grid(row=i+1, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
            btn.bind("<Button-1>", click)
            break  # Skip remaining columns
        elif text == "=":
            btn = tk.Button(root, text=text, font="Arial 18", bd=5, relief=tk.RAISED,
                            bg="black", fg="white", activebackground="darkgreen")
            btn.grid(row=i+1, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
            btn.bind("<Button-1>", click)
            break
        elif text == "0":
            btn = tk.Button(root, text=text, font="Arial 18", bd=5, relief=tk.RAISED,
                            bg="black", fg="white")
            btn.grid(row=i+1, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
            btn.bind("<Button-1>", click)
            col += 2
        else:
            bg_color = "black" if text in {"+", "-", "*", "/"} else "lightgray"
            fg_color = "white" if text in {"+", "-", "*", "/"} else "black"
            btn = tk.Button(root, text=text, font="Arial 18", bd=5, relief=tk.RAISED,
                            bg=bg_color, fg=fg_color)
            btn.grid(row=i+1, column=col, sticky="nsew", padx=2, pady=2)
            btn.bind("<Button-1>", click)
            col += 1


for i in range(7):  # total rows including entry
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # total columns
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
