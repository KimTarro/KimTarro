import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ExpensesTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Expenses Tracker")
        self.master.configure(bg="#f0f0f0")

        self.expenses = []

        self.description_label = tk.Label(master, text="Description:", bg="#f0f0f0")
        self.description_label.grid(row=0, column=0, padx=5, pady=5)
        self.description_entry = tk.Entry(master)
        self.description_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = tk.Label(master, text="Amount (₱):", bg="#f0f0f0")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)
        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.category_label = tk.Label(master, text="Category:", bg="#f0f0f0")
        self.category_label.grid(row=2, column=0, padx=5, pady=5)
        self.category_var = tk.StringVar(master)
        self.category_var.set("Select Category")
        self.categories = ["Food", "Transportation", "Housing", "Entertainment", "Utilities", "Other"]
        self.category_dropdown = ttk.Combobox(master, textvariable=self.category_var, values=self.categories, state="readonly")
        self.category_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.category_dropdown.configure(background="#ffffff", font=("Helvetica", 8), width=15)

        self.add_button = tk.Button(master, text="Add Expense", command=self.add_expense, bg="#008CBA", fg="white")
        self.add_button.grid(row=3, columnspan=2, padx=5, pady=5)

        self.expense_listbox = tk.Listbox(master, width=38)
        self.expense_listbox.grid(row=4, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.scrollbar = tk.Scrollbar(master, orient="vertical", command=self.expense_listbox.yview)
        self.scrollbar.grid(row=4, column=2, sticky="ns")
        self.expense_listbox.config(yscrollcommand=self.scrollbar.set)

        self.total_label = tk.Label(master, text="Total Expenses: ₱0.00", bg="#f0f0f0")
        self.total_label.grid(row=5, columnspan=2, padx=5, pady=5)

        self.clear_button = tk.Button(master, text="Clear All Expenses", command=self.clear_expenses, bg="#FF5733", fg="white")
        self.clear_button.grid(row=6, columnspan=2, padx=5, pady=5)

        self.master.bind("<Return>", self.add_expense)

    def add_expense(self, event=None):
        description = self.description_entry.get()
        amount = self.amount_entry.get()
        category = self.category_var.get()

        if description and amount and category != "Select Category":
            try:
                amount = float(amount)
                self.expenses.append({"description": description, "amount": amount, "category": category})
                self.update_expense_list()
                self.update_total_label()
                self.clear_fields()
            except ValueError:
                messagebox.showerror("Error", "Amount must be a number")
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def update_expense_list(self):
        self.expense_listbox.delete(0, tk.END)
        for expense in self.expenses:
            self.expense_listbox.insert(tk.END, f"{expense['description']} - ₱{expense['amount']:.2f} ({expense['category']})")

    def update_total_label(self):
        total = sum(expense['amount'] for expense in self.expenses)
        self.total_label.config(text=f"Total Expenses: ₱{total:.2f}")

    def clear_expenses(self):
        if messagebox.askyesno("Confirmation", "Clear all expenses?"):
            self.expenses = []
            self.update_expense_list()
            self.update_total_label()

    def clear_fields(self):
        self.description_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_var.set("Select Category")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpensesTracker(root)
    root.mainloop()