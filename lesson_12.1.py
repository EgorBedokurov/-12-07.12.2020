import uuid
from datetime import date

class Bank:
    comission = 0.01

    """Банковский счет"""
    def __init__(self, name_bank):
        self.name_bank = name_bank #название банка
        self._balance = 0
        self._transactions = []
        self.bank_account = uuid.uuid4() # id банка

    # """учет операцй"""
    @property
    def current_balance(self):
        deposit = 0
        withdrawal = 0
        for transaction in self._transactions:
            if transaction[1] == 'deposit funds ':
                deposit += transaction[0]
            else:
                withdrawal += transaction[0]
        return deposit - withdrawal

    """депозит средств"""
    def deposit(self, amount):
        self._balance += amount*0.99
        self._transactions.append((amount, 'deposit funds ', str(date.today())))

    """вывод средств"""
    def withdrawal_of_funds(self, amount): #если за лемитом все равно считает
        if amount < self._balance:
            self._balance -= amount*1.01
        else:
            print('not enough funds on the deposit ', str(self._balance))
        self._transactions.append((amount, 'withdrawal funds ', str(date.today())))


operation = Bank('Omega Bank')
print('Bank - ', operation.name_bank)
print('Bank account - ', operation.bank_account)
operation.deposit(3000)
print('deposit of funds - ', operation._balance)
operation.withdrawal_of_funds(2000)
print('deposit of funds - ', operation._balance)
operation.withdrawal_of_funds(700)
print('Withdrawal of funds - ', operation._balance)
print('archive of transactions - ', operation._transactions)
print('current balance - ', operation._balance)