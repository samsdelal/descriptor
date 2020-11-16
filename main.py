class Value():

    def __init__(self, amount=0):
        self.amount = amount

    def __set__(self, instance, value):
        self.amount = int((1-instance.commission)*value)

    def __get__(self, instance, owner):
        return self.amount


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)
