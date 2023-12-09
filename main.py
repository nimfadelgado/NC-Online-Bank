import random
import tkinter as tk
from tkinter import messagebox, simpledialog

class Bank:
    def __init__(self):
        self.accounts = {}
        self.transactions = {}

    def create_account(self, name, initial_balance):
        account_number = random.randint(1000, 9999)
        self.accounts[account_number] = {'name': name, 'balance': initial_balance}
        self.transactions[account_number] = []
        messagebox.showinfo("Account Created", f"Account created successfully! Account Number: {account_number}")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            self.transactions[account_number].append(f"Deposit: +{amount}")
            messagebox.showinfo("Deposit Successful", f"Deposit successful. New balance: {self.accounts[account_number]['balance']}")
        else:
            messagebox.showerror("Error", "Invalid account number.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]['balance']
            transactions = "\n".join(self.transactions[account_number])
            receipt = f"Account Balance: {balance}\nTransaction History:\n{transactions}"
            messagebox.showinfo("Account Balance", receipt)
        else:
            messagebox.showerror("Error", "Invalid account number.")

    def get_transaction_history(self, account_number):
        return "\n".join(self.transactions.get(account_number, []))

    def save_transaction_history_to_file(self, account_number, filename):
        transactions = self.transactions.get(account_number, [])
        with open(filename, 'w') as file:
            file.write("\n".join(transactions))

class BankingApp(tk.Tk):
    def __init__(self, bank):
        super().__init__()
        self.bank = bank
        self.title("NC Online Bank")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Banking System Menu")
        label.pack(pady=10)

        button_create = tk.Button(self, text="Create Account", command=self.create_account)
        button_create.pack()

        button_deposit = tk.Button(self, text="Deposit Money", command=self.deposit_money)
        button_deposit.pack()

        button_balance = tk.Button(self, text="Check Balance", command=self.check_balance)
        button_balance.pack()

        button_view_history = tk.Button(self, text="View Transaction History", command=self.view_transaction_history)
        button_view_history.pack()

        button_save_to_file = tk.Button(self, text="Save Transaction History to File", command=self.save_transaction_history_to_file)
        button_save_to_file.pack()

        button_quit = tk.Button(self, text="Quit", command=self.quit_app)
        button_quit.pack()

    def create_account(self):
        name = simpledialog.askstring("Input", "Enter your name:")
        initial_balance = simpledialog.askfloat("Input", "Enter initial balance:")
        if name and initial_balance is not None:
            self.bank.create_account(name, initial_balance)

    def deposit_money(self):
        account_number = simpledialog.askinteger("Input", "Enter account number:")
        amount = simpledialog.askfloat("Input", "Enter deposit amount:")
        if account_number is not None and amount is not None:
            self.bank.deposit(account_number, amount)

    def check_balance(self):
        account_number = simpledialog.askinteger("Input", "Enter account number:")
        if account_number is not None:
            self.bank.check_balance(account_number)

    def view_transaction_history(self):
        account_number = simpledialog.askinteger("Input", "Enter account number:")
        if account_number is not None:
            transaction_history = self.bank.get_transaction_history(account_number)
            messagebox.showinfo("Transaction History", f"Transaction History for Account {account_number}:\n{transaction_history}")

    def save_transaction_history_to_file(self):
        account_number = simpledialog.askinteger("Input", "Enter account number:")
        if account_number is not None:
            filename = simpledialog.askstring("Input", "Enter filename (including extension):")
            if filename:
                self.bank.save_transaction_history_to_file(account_number, filename)
                messagebox.showinfo("File Saved", f"Transaction history for Account {account_number} saved as {filename}")

    def quit_app(self):
        self.destroy()

def main():
    bank = Bank()
    app = BankingApp(bank)
    app.mainloop()

if __name__ == "__main__":
    main()
