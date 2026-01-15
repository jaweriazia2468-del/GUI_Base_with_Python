import tkinter as tk
from tkinter import messagebox
from abc import ABC, abstractmethod

# Account classes with abstraction and polymorphism
class Account(ABC):
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance

class SavingsAccount(Account):
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds in Savings Account.")
        self.balance -= amount

class CheckingAccount(Account):
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        # Allow overdraft up to PKR 500
        if amount > self.balance + 500:
            raise ValueError("Overdraft limit exceeded in Checking Account.")
        self.balance -= amount

# Main GUI Application
class BankApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account Management System")
        self.accounts = {}

        self.create_widgets()

    def create_widgets(self):
        frame_create = tk.LabelFrame(self.root, text="Create Account", padx=10, pady=10)
        frame_create.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(frame_create, text="Owner Name:").grid(row=0, column=0, sticky="w")
        self.owner_entry = tk.Entry(frame_create)
        self.owner_entry.grid(row=0, column=1)

        tk.Label(frame_create, text="Account Type:").grid(row=1, column=0, sticky="w")
        self.account_type_var = tk.StringVar(value="Savings")
        tk.Radiobutton(frame_create, text="Savings", variable=self.account_type_var, value="Savings").grid(row=1, column=1, sticky="w")
        tk.Radiobutton(frame_create, text="Checking", variable=self.account_type_var, value="Checking").grid(row=1, column=2, sticky="w")

        tk.Button(frame_create, text="Create Account", command=self.create_account).grid(row=2, column=0, columnspan=3, pady=5)

        frame_transact = tk.LabelFrame(self.root, text="Transactions", padx=10, pady=10)
        frame_transact.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(frame_transact, text="Owner Name:").grid(row=0, column=0, sticky="w")
        self.trans_owner_entry = tk.Entry(frame_transact)
        self.trans_owner_entry.grid(row=0, column=1)

        tk.Label(frame_transact, text="Amount:").grid(row=1, column=0, sticky="w")
        self.amount_entry = tk.Entry(frame_transact)
        self.amount_entry.grid(row=1, column=1)

        tk.Button(frame_transact, text="Deposit", command=self.deposit).grid(row=2, column=0, pady=5)
        tk.Button(frame_transact, text="Withdraw", command=self.withdraw).grid(row=2, column=1, pady=5)
        tk.Button(frame_transact, text="Check Balance", command=self.check_balance).grid(row=3, column=0, columnspan=2, pady=5)

    def create_account(self):
        owner = self.owner_entry.get().strip()
        if not owner:
            messagebox.showerror("Error", "Owner name cannot be empty.")
            return
        if owner in self.accounts:
            messagebox.showerror("Error", "Account already exists for this owner.")
            return
        acc_type = self.account_type_var.get()
        if acc_type == "Savings":
            self.accounts[owner] = SavingsAccount(owner)
        else:
            self.accounts[owner] = CheckingAccount(owner)
        messagebox.showinfo("Success", f"{acc_type} Account created for {owner}.")
        self.owner_entry.delete(0, tk.END)

    def deposit(self):
        owner = self.trans_owner_entry.get().strip()
        if owner not in self.accounts:
            messagebox.showerror("Error", "Account not found.")
            return
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")
            return
        try:
            self.accounts[owner].deposit(amount)
            messagebox.showinfo("Success", f"Deposited PKR {amount:.2f} to {owner}'s account.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def withdraw(self):
        owner = self.trans_owner_entry.get().strip()
        if owner not in self.accounts:
            messagebox.showerror("Error", "Account not found.")
            return
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount entered.")
            return
        try:
            self.accounts[owner].withdraw(amount)
            messagebox.showinfo("Success", f"Withdrew PKR {amount:.2f} from {owner}'s account.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def check_balance(self):
        owner = self.trans_owner_entry.get().strip()
        if owner not in self.accounts:
            messagebox.showerror("Error", "Account not found.")
            return
        balance = self.accounts[owner].get_balance()
        messagebox.showinfo("Balance", f"Balance for {owner}'s account: PKR {balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BankApp(root)
    root.mainloop()
