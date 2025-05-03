import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

class BirthdateSelector:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Birthdate Information')
        self.window.geometry('450x500')
        self.window.configure(bg="#f0f8ff")  # Alice blue background
        
        # Create main frame with padding
        self.main_frame = ttk.Frame(self.window, padding=40)
        self.main_frame.pack(pady=20)
        
        # Initialize variables
        self.month_var = tk.StringVar()
        self.day_var = tk.StringVar()
        self.year_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title_style = ttk.Style()
        title_style.configure("Title.TLabel", font=("Arial", 16, "bold"), foreground="#2c3e50")
        
        title = ttk.Label(self.main_frame, text="Enter Your Birth Information", 
                         style="Title.TLabel")
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Month selection
        self.create_label("Month:", 1)
        months = ('January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December')
        self.create_combobox(self.month_var, months, 1)
        
        # Day selection
        self.create_label("Day:", 2)
        self.create_combobox(self.day_var, tuple(range(1, 32)), 2)
        
        # Year selection
        self.create_label("Year:", 3)
        self.create_combobox(self.year_var, tuple(range(1900, 2025)), 3)
        
        # Gender selection
        self.create_label("Gender:", 4)
        self.create_gender_radio_buttons(4)
        
        # Submit button
        button_style = ttk.Style()
        button_style.configure("Submit.TButton", font=("Arial", 12), padding=10)
        
        submit_btn = ttk.Button(self.main_frame, text="Submit Information", 
                              command=self.show_info, style="Submit.TButton")
        submit_btn.grid(row=5, column=0, columnspan=2, pady=20)
        
    def create_label(self, text, row):
        label = ttk.Label(self.main_frame, text=text, font=("Arial", 11))
        label.grid(row=row, column=0, sticky="w", pady=5)
        
    def create_combobox(self, var, values, row):
        combo = ttk.Combobox(self.main_frame, width=25, textvariable=var, state='readonly')
        combo['values'] = values
        combo.grid(row=row, column=1, pady=5)
        
    def create_gender_radio_buttons(self, row):
        gender_frame = ttk.Frame(self.main_frame)
        gender_frame.grid(row=row, column=1, pady=5)
        
        ttk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, 
                       value="Male").pack(side="left", padx=10)
        ttk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, 
                       value="Female").pack(side="left", padx=10)
        
    def show_info(self):
        month = self.month_var.get()
        day = self.day_var.get()
        year = self.year_var.get()
        gender = self.gender_var.get()
        
        if all([month, day, year, gender]):
            message = f"Birth Information:\n\nDate: {month} {day}, {year}\nGender: {gender}"
            showinfo("Birth Information", message)
        else:
            showinfo("Error", "Please fill in all fields.")
            
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = BirthdateSelector()
    app.run() 