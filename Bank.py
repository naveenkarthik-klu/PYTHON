class Bank_Account:
    def __init__(self):
        self.balance = 15000
        print("Welcome Shenbu")
        print("Available balance", self.balance)

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=", self.balance)


s = Bank_Account()
while True:
    print("Press 1 to Deposite\nPress 2 to Withdraw\nPress 3 to exit")
    ch = int(input())
    if ch == 1:
        s.deposit()
        s.display()
    if ch == 2:
        s.withdraw()
        s.display()
    if ch == 3:
        break
