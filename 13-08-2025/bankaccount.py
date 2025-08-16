import random

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_number = self.generate_accountnumber()
        self.account_holder_name = account_holder
        self.balance = balance

    @staticmethod
    def generate_accountnumber():
        return str(random.randint(10**15, (10**16) - 1))

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Current balance: {self.balance}")


class SavingAccount(BankAccount):
    interest_rate = 0.04

    def apply_interest(self):
        interest = self.balance * SavingAccount.interest_rate
        self.balance += interest
        print(f"Interest of {interest:.2f} applied with 4% rate")
        self.display_balance()


class CurrentAccount(BankAccount):
    overdraft_limit = 30000

    def withdraw(self, amount):
        if amount <= self.balance + CurrentAccount.overdraft_limit:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Withdrawal exceeds overdraft limit")


def main():
    print("Welcome to the Bank")
    type_account = input("Enter type of account (saving/current): ").strip().lower()
    name = input("Enter account holder name: ")
    balance = float(input("Enter initial balance: "))

    if type_account == "saving":
        account = SavingAccount(name, balance)
        print("Your Saving Account created successfully.")
        print("Interest rate (fixed) is 4%")
        print(f"Your account number is {account.account_number}")
    elif type_account == "current":
        account = CurrentAccount(name, balance)
        print("Your Current Account created successfully.")
        print(f"Account number is {account.account_number}")
        print("Overdraft limit: 30,000")
    else:
        print("Invalid type of account")
        return

    while True:
        print("\nChoose an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        if type_account == "saving":
            print("4. Apply Interest")
            print("5. Exit")
        else:
            print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.display_balance()
        elif type_account == "saving" and choice == "4":
            account.apply_interest()
        elif (type_account == "saving" and choice == "5") or (type_account == "current" and choice == "4"):
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice")

main()