import tkinter as tk
from tkinter import ttk

from utils.Solver import EqSolver


def solve():
    Eq1 = Eq1_entry.get()
    Eq2 = Eq2_entry.get()
    solutions = EqSolver(Eq1, Eq2).solution()
    print(f"x = {solutions[0]}")
    print(f"y = {solutions[1]}")

    string = f"x = {solutions[0]}, y= {solutions[1]}"
    solution.configure(text=string)


#styling
field_font = ("Times New Roman", "20")
entry_font = ("Times New Roman", "20")
button_font = ("Times New Roman", "20")

app = tk.Tk()
app.geometry("800x800")
app.title("Automate my homework")

Eq1 = ttk.Label(app, text="Equation 1: ", font=field_font)
Eq2 = ttk.Label(app, text="Equation 2: ", font=field_font)

Eq1.grid(row=0, column=0, sticky="W", pady= 2)
Eq2.grid(row=1, column=0, sticky="W", pady=2)

Eq1_entry = ttk.Entry(app, width=15, font=entry_font)
Eq2_entry = ttk.Entry(app, width=15, font=entry_font)

Eq1_entry.grid(row=0, column=1, pady=2)
Eq2_entry.grid(row=1, column=1, pady=2)

Eq1_entry.insert(0, "3x+2y=10")
Eq2_entry.insert(0, "2x+4y=8")


solve_button = tk.Button(app, text="Solve!", command=solve, font=button_font)
solve_button.grid(row=2,column=0, pady=2)

quit_button = tk.Button(app, text="Quit", command=app.destroy, font=button_font)
quit_button.grid(row=2, column=1, pady=2)

solution = tk.Label(app, text="", font=field_font)
solution.grid(row=3, column=0)

app.mainloop()
