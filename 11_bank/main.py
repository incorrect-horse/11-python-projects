
class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance


    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry, not enough funds!")


    def statement(self):
        print(f"Account Balance: ${self.balance}")


class Current(Account):
    def __init__(self, name,balance):
        super().__init__(name, balance, min_balance = -1000)


    def __str__(self):
        return f"{self.name}'s Current Account : Balance ${self.balance}"


class Savings(Account):
    def __init__(self, name,balance):
        super().__init__(name, balance, min_balance = 0)


    def __str__(self):
        return f"{self.name}'s Savings Account : Balance ${self.balance}"


X = Current("\John Wick", 5000)
print(X)
X.deposit(5000)
X.statement()
X.withdraw(200)
X.statement()
X.withdraw(10800)
X.statement()
X.withdraw(1)
X.statement()

T = Savings("\nRobert McCall", 200)
print(T)
T.withdraw(200)
T.statement()
T.withdraw(200)
T.statement()

try:
    pass
except KeyboardInterrupt:
    print("\n[-] Detected CTRL+C ... terminating app, please wait.")

print("\nGoodbye!")
