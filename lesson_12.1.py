"""не закончено"""
import uuid

class Bank:

    """Банковский счет"""
    def __init__(self, name, balance, transaction=[100], id=uuid.uuid4()):
        self.name = name
        self.balance = balance
        self.transaction = transaction
        self.id = id

    """депозит средств"""
    def deposit(self):
        dep = str(input('введите сумму на депозит - '))
        return dep
        print('ваш баланс ', str(self.balance - dep), 'на депозите - ' + str(dep))


    """вывод средств"""
    def withdrawal_of_funds(self):
        w_t = input('введите сумму на депозит - ')
        bal = self.balance - w_t
        return w_t, bal
        print('снято - ' + w_t + 'остаток на балансе - ' + bal)


    """получить баланс"""
    def get_balance(self):
        g_b = self.balance
        return g_b

    """банковские комиссии"""
    def commission(self):
        com = self.transaction * 0.01
        print('комиссия банка составила - ' + float(com))

operation_1 = Bank('Omega Bank', 10000, 100, uuid.uuid4())
print(operation_1.name)
print(operation_1.balance)
print(operation_1.id)
print(operation_1.transaction)

print(operation_1.deposit())
operation_1.get_balance()