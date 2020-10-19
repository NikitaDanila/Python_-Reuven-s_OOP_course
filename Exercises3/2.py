class Loan(object):
    total_money = 1000

    def __init__(self, loan_money):
        if loan_money < Loan.total_money:
            self.loan_money = loan_money
            Loan.total_money -= loan_money
            print(
                f"You borrowed {loan_money} Total amount: {Loan.total_money}")
        else:
            print(f"No money Bro\nTotal amount {Loan.total_money}")

    def repay(self, amount):
        self.loan_money -= amount
        Loan.total_money += amount
        print(f"You repaid {amount} Total amount: {Loan.total_money}")


l1 = Loan(500)
l2 = Loan(200)
l3 = Loan(700)  # raises an exception -- ValueError to indicate no money
l1.repay(500)
l3 = Loan(700)
