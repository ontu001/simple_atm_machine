# Simple ATM Machine program in Python

class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def check_balance(self):
        print("Your current balance is: " + str(self.balance))

    def deposit(self, amount):
        self.balance += amount
        print("You have deposited: " + str(amount))

    def check_withdrawal_list(self):
        for withdrawal in self.withdrawals_list:
            print(withdrawal)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("You have withdrawn: " + str(amount))
            self.withdrawals_list.append("You withdrew: " + str(amount) + " on " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")))
        else:
            print("Insufficient balance")

balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Barclays")
atm2 = ATM(balance2, "HSBC")

atm1.check_balance()
atm1.deposit(100)
atm1.check_balance()
atm1.withdraw(200)
atm1.check_balance()
atm1.check_withdrawal_list()

atm2.check_balance()
atm2.withdraw(200)
atm2.check_balance()
atm2.withdraw(1500)
atm2.check_balance()


#md rohanur rahman ontu