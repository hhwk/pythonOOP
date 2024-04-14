class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print("Создан новый счет:", account_number)
        else:
            print("Номер счета уже существует.")

    def make_deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print("Внесено", amount, "на счет", account_number)
        else:
            print("Номер счета не существует.")

    def make_withdrawal(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print("Снято", amount, "со счета", account_number)
            else:
                print("Недостаточно средств.")
        else:
            print("Номер счета не существует.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print("Баланс счета", account_number, ":", self.accounts[account_number])
        else:
            print("Номер счета не существует.")

bank = Bank()
acno1 = "SB-123"
damt1 = 1000
print("Новый номер счета:", acno1, "Начальный депозит:", damt1)
bank.create_account(acno1, damt1)

acno2 = "SB-124"
damt2 = 1500
print("Новый номер счета:", acno2, "Начальный депозит:", damt2)
bank.create_account(acno2, damt2)

wamt1 = 600
print("\nСумма депозита:", wamt1, "на счет", acno1)
bank.make_deposit(acno1, wamt1)

wamt2 = 350
print("Сумма снятия:", wamt2, "со счета", acno2)
bank.make_withdrawal(acno2, wamt2)

print("Номер счета:", acno1)
bank.check_balance(acno1)

print("Номер счета:", acno2)
bank.check_balance(acno2)

wamt3 = 1200
print("Сумма снятия:", wamt3, "со счета", acno2)
bank.make_withdrawal(acno2, wamt3)

acno3 = "SB-134"
print("Номер счета", acno3)
bank.check_balance(acno3)
