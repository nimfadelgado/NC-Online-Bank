import random

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance):
        account_number = random.randint(1000, 9999)
        self.accounts[account_number] = {'name': name, 'balance': initial_balance}
        print(f"Account created successfully! Account Number: {account_number}")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print(f"Deposit successful. New balance: {self.accounts[account_number]['balance']}")
        else:
            print("Invalid account number.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]['balance']:
                self.accounts[account_number]['balance'] -= amount
                print(f"Withdrawal successful. New balance: {self.accounts[account_number]['balance']}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid account number.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account Balance: {self.accounts[account_number]['balance']}")
        else:
            print("Invalid account number.")

def main():
    bank = Bank()

    while True:
        print("\n***Welcome to NC Online Bank***")
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter your name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(name, initial_balance)

        elif choice == '2':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == '3':
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == '4':
            account_number = int(input("Enter account number: "))
            bank.check_balance(account_number)

        elif choice == '5':
            print("Thank you for using the banking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()