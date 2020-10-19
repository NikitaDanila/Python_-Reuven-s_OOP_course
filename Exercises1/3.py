class BankAccount(object):
    def __init__(self):
        self.transactions = []


acc1 = BankAccount()
acc2 = BankAccount()


def add_money():
    acc = input('Select an account: ')
    trans = ''
    if acc == '1':
        while True:
            trans = input('Enter a sum of money: ')
            if not trans:
                next = input("Add to another account? (y/n)\n")
                if next == 'y':
                    add_money()
                break
            else:
                acc1.transactions.append(float(trans))
    else:
        while True:
            trans = (input('Enter a sum of money: '))
            if not trans:
                next = input("Add to another account? (y/n)")
                if next == 'y':
                    add_money()
                break
            else:
                acc2.transactions.append(float(trans))


add_money()
print(f"acc 1 len: {len(acc1.transactions)}")
print(f"acc 2 len: {len(acc2.transactions)}")

print(f"acc 1 balance: {sum(acc1.transactions)}")
print(f"acc 2 balance: {sum(acc2.transactions)}")

print(
    f"acc 1 avg: {int(sum(acc1.transactions)) / int(len(acc1.transactions))}")
print(
    f"acc 2 avg: {int(sum(acc2.transactions)) / int(len(acc1.transactions))}")
