import json
import os
import tkinter as tk
from tkinter import messagebox, ttk


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Expense Tracker")
        self.root.geometry("600x450")

        self.filename = "expenses.json"
        self.expenses = self.load_data()
        self.selected_index = None

        self.create_widgets()
        self.update_list()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.expenses, file)

    def create_widgets(self):
        # Input Form
        form_frame = tk.Frame(self.root, pady=10)
        form_frame.pack()

        tk.Label(form_frame, text="Item:").grid(row=0, column=0, padx=5, pady=5)
        self.item_entry = tk.Entry(form_frame)
        self.item_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Amount:").grid(row=0, column=2, padx=5, pady=5)
        self.amount_entry = tk.Entry(form_frame)
        self.amount_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(form_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
        self.categories = ["Food", "Transport", "Bills", "Shopping", "Other"]
        self.category_cb = ttk.Combobox(form_frame, values=self.categories, state="readonly")
        self.category_cb.grid(row=1, column=1, padx=5, pady=5)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        self.save_btn = tk.Button(btn_frame, text="Add Expense", command=self.save_expense)
        self.save_btn.grid(row=0, column=0, padx=5)
 
        tk.Button(btn_frame, text="Edit Selected", command=self.load_selected).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete Selected",command=self.delete_expense).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Clear Form", command=self.clear_form).grid(row=0, column=3, padx=5)

        table_frame = tk.Frame(self.root, pady=10)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        self.tree = ttk.Treeview(table_frame, columns=("Item", "Amount", "Category"), show="headings")
        self.tree.heading("Item", text="Item")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Category", text="Category")

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.total_label = tk.Label(self.root, text="Total Spent: 0.00", font=("Arial", 12, "bold"), pady=10)
        self.total_label.pack()
    def save_expense(self):
        item = self.item_entry.get().strip()
        amount_text = self.amount_entry.get().strip()
        category = self.category_cb.get()

        if not item or not amount_text:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Amount must be a positive number.")
            return

        record = {"item": item, "amount": amount, "category": category}

        if self.selected_index is None:
            self.expenses.append(record)
        else:
            self.expenses[self.selected_index] = record

        self.save_data()
        self.update_list()
        self.clear_form()

    def load_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Row")
            return

        index = self.tree.index(selected[0])
        self.selected_index = index
        data = self.expenses[index]

        self.item_entry.delete(0, tk.END)
        self.item_entry.insert(0, data["item"])

        self.amount_entry.delete(0, tk.END)
        self.amount_entry.insert(0, str(data["amount"]))

        self.category_cb.set(data["category"])
        self.save_btn.config(text="Update Expense")

    def delete_expense(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Select Row", "Please select an item to delete.")
            return

        index = self.tree.index(selected[0])
        del self.expenses[index]

        self.save_data()
        self.update_list()
        self.clear_form()

    def clear_form(self):
        self.selected_index = None
        self.item_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)
        self.category_cb.set("Food")
        self.save_btn.config(text="Add Expense")

    def update_list(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        total = 0.0
        for exp in self.expenses:
            self.tree.insert("", tk.END, values=(exp["item"], f"{exp['amount']:.2f}", exp["category"]))
            total += exp["amount"]

        self.total_label.config(text=f"Total Spent: {total:,.2f}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()