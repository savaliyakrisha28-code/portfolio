# Project 5: All-in-One Python Portfolio Hub (Projects 1 to 4)
import tkinter as tk
from tkinter import ttk

class PortfolioHubApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Fundamentals Portfolio Hub")
        self.geometry("600x680")
        self.minsize(520, 620)
        self.configure(bg="#f4f7fb")

        # Variables initialized inside __init__ to avoid RuntimeError
        self.project_choice = tk.StringVar(value="Project 1: Basic Calculator")
        self.output_text = tk.StringVar(value="Select a project and click Run")
        self.memory_var = tk.StringVar(value="")

        # Dynamic Input Variables
        self.val1 = tk.StringVar()
        self.val2 = tk.StringVar()
        self.val3 = tk.StringVar()
        self.val4 = tk.StringVar()

        self._build_ui()
        self._update_fields()

    def _build_ui(self):
        outer = ttk.Frame(self, padding=24)
        outer.pack(fill="both", expand=True)

        ttk.Label(outer, text="Portfolio Hub", font=("Segoe UI", 22, "bold")).pack(anchor="w")
        ttk.Label(outer, text="Projects 1 to 4 Unified Application", font=("Segoe UI", 10), foreground="#60708d").pack(anchor="w", pady=(2, 15))

        # Project Selector Card
        card = ttk.LabelFrame(outer, text=" Select Project ", padding=16)
        card.pack(fill="x", pady=5)

        selector = ttk.Combobox(card, textvariable=self.project_choice, values=[
            "Project 1: Basic Calculator",
            "Project 2: Tip & Bill Splitter",
            "Project 3: Unit & Currency Converter",
            "Project 4: Interest & Age Calculator"
        ], state="readonly", font=("Segoe UI", 11))
        selector.pack(fill="x", pady=(5, 10))
        selector.bind("<<ComboboxSelected>>", lambda _e: self._update_fields())

        # Dynamic Inputs Frame
        self.inputs_frame = ttk.LabelFrame(outer, text=" Inputs ", padding=16)
        self.inputs_frame.pack(fill="x", pady=10)

        # Labels & Entry setup references
        self.lbl1 = ttk.Label(self.inputs_frame, font=("Segoe UI", 10, "bold"))
        self.ent1 = ttk.Entry(self.inputs_frame, textvariable=self.val1, font=("Segoe UI", 11))
        
        self.lbl2 = ttk.Label(self.inputs_frame, font=("Segoe UI", 10, "bold"))
        self.ent2 = ttk.Entry(self.inputs_frame, textvariable=self.val2, font=("Segoe UI", 11))

        self.lbl3 = ttk.Label(self.inputs_frame, font=("Segoe UI", 10, "bold"))
        self.ent3 = ttk.Entry(self.inputs_frame, textvariable=self.val3, font=("Segoe UI", 11))

        self.lbl4 = ttk.Label(self.inputs_frame, font=("Segoe UI", 10, "bold"))
        self.ent4 = ttk.Entry(self.inputs_frame, textvariable=self.val4, font=("Segoe UI", 11))

        # Buttons
        btn_frame = ttk.Frame(outer)
        btn_frame.pack(fill="x", pady=12)
        
        tk.Button(btn_frame, text="Run Program", bg="#f26b38", fg="#ffffff", font=("Segoe UI", 11, "bold"), relief="flat", padx=15, pady=8, command=self.run_project).pack(side="left", expand=True, fill="x", padx=(0, 6))
        tk.Button(btn_frame, text="Clear", bg="#edf1f7", fg="#31415f", font=("Segoe UI", 11, "bold"), relief="flat", padx=15, pady=8, command=self.clear_fields).pack(side="left", expand=True, fill="x", padx=(6, 0))

        # Result Box
        res_frame = tk.Frame(outer, bg="#14213d", padx=16, pady=16)
        res_frame.pack(fill="x", pady=8)

        tk.Label(res_frame, textvariable=self.output_text, bg="#14213d", fg="#ffffff", font=("Segoe UI", 12, "bold"), anchor="w", wraplength=520).pack(fill="x", pady=4)
        tk.Label(res_frame, textvariable=self.memory_var, bg="#14213d", fg="#4ade80", font=("Segoe UI", 10, "bold"), anchor="w").pack(fill="x", pady=2)

    def _update_fields(self):
        for widget in self.inputs_frame.winfo_children():
            widget.grid_forget()

        choice = self.project_choice.get()
        self.clear_fields()

        if "Project 1" in choice:
            self.inputs_frame.configure(text=" Basic Calculator Inputs ")
            self._grid_field(0, self.lbl1, self.ent1, "Number 1:")
            self._grid_field(1, self.lbl2, self.ent2, "Number 2:")
        elif "Project 2" in choice:
            self.inputs_frame.configure(text=" Tip & Bill Splitter Inputs ")
            self._grid_field(0, self.lbl1, self.ent1, "Total Bill Amount (Rs):")
            self._grid_field(1, self.lbl2, self.ent2, "Tip Percentage (%):")
            self._grid_field(2, self.lbl3, self.ent3, "Number of People:")
        elif "Project 3" in choice:
            self.inputs_frame.configure(text=" Unit/Currency Converter Inputs ")
            self._grid_field(0, self.lbl1, self.ent1, "Type (1:C->F, 2:F->C, 3:Km->Mi, 4:INR->USD):")
            self._grid_field(1, self.lbl2, self.ent2, "Value to Convert:")
        elif "Project 4" in choice:
            self.inputs_frame.configure(text=" Interest & Age Inputs ")
            self._grid_field(0, self.lbl1, self.ent1, "Principal (Rs):")
            self._grid_field(1, self.lbl2, self.ent2, "Rate (%):")
            self._grid_field(2, self.lbl3, self.ent3, "Time (Years):")
            self._grid_field(3, self.lbl4, self.ent4, "Birth Year (for Age):")

    def _grid_field(self, row, label, entry, text):
        label.configure(text=text)
        label.grid(row=row, column=0, sticky="w", pady=5, padx=5)
        entry.grid(row=row, column=1, sticky="ew", pady=5, padx=5)
        self.inputs_frame.columnconfigure(1, weight=1)

    def run_project(self):
        choice = self.project_choice.get()
        try:
            if "Project 1" in choice:
                n1 = float(self.val1.get())
                n2 = float(self.val2.get())
                res = n1 + n2
                self.output_text.set(f"Sum = {res} | Type: {type(n1)}")
                self.memory_var.set(f"Memory id: {id(res)}")

            elif "Project 2" in choice:
                bill = float(self.val1.get())
                tip_pct = float(self.val2.get())
                people = int(self.val3.get())
                total = bill + (bill * tip_pct / 100)
                per_person = total / people
                self.output_text.set(f"Total Bill: Rs.{total:.2f} | Per Person: Rs.{per_person:.2f}")
                self.memory_var.set(f"Memory id: {id(per_person)}")

            elif "Project 3" in choice:
                opt = int(self.val1.get())
                val = float(self.val2.get())
                if opt == 1:
                    res = (val * 9/5) + 32
                    unit = "°F"
                elif opt == 2:
                    res = (val - 32) * 5/9
                    unit = "°C"
                elif opt == 3:
                    res = val * 0.621371
                    unit = "Miles"
                else:
                    res = val / 83.0
                    unit = "USD"
                self.output_text.set(f"Converted Result = {res:.2f} {unit}")
                self.memory_var.set(f"Memory id: {id(res)}")

            elif "Project 4" in choice:
                p = float(self.val1.get())
                r = float(self.val2.get())
                t = float(self.val3.get())
                by = int(self.val4.get())
                si = (p * r * t) / 100
                age = 2026 - by
                self.output_text.set(f"Simple Interest = Rs.{si:.1f} | Age in 2026 = {age} yrs")
                self.memory_var.set(f"Types - P:{type(p)}, AgeYr:{type(by)}")

        except Exception:
            self.output_text.set("Please enter valid numeric values in all fields!")
            self.memory_var.set("")

    def clear_fields(self):
        self.val1.set("")
        self.val2.set("")
        self.val3.set("")
        self.val4.set("")
        self.output_text.set("Select fields and run project")
        self.memory_var.set("")

if __name__ == "__main__":
    PortfolioHubApp().mainloop()