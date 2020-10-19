class Person(object):
    def __init__(self, name='', email='', phone=''):
        self.name = name
        self.email = email
        self.phone = phone
        self.account = []

    def add_account(self, *args):
        self.account += args

    def all_balances(self):
        all_money = []
        for money in range(len(self.account)):
            all_money += self.account[money].transactions

        return all_money

    def avg_trans_amount(self):
        total_sum = 0
        avg = 0
        total_trans = 0

        for money in range(len(self.account)):
            total_sum += sum(self.account[money].transactions)
            total_trans += len(self.account[money].transactions)

        return (total_sum / total_trans)

    def current_total_balance(self):
        total = 0

        for money in range(len(self.account)):
            total += sum(self.account[money].transactions)

        return total


class BankAccount(object):
    def __init__(self):
        self.transactions = []

    def add_money(self, *args):
        self.transactions += args


p1 = Person()

acc1 = BankAccount()
acc2 = BankAccount()

acc1.add_money(100, 20, -50, 83)
acc2.add_money(20, 30, -75, 32, -34)

p1.add_account(acc1, acc2)
# p1.all_balances()
print(f"all_balance: {p1.all_balances()}\n")
print(f"current_total: {p1.current_total_balance()}\n")
print(f"avg_balance: {p1.avg_trans_amount()}\n")
