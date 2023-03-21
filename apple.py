# restaurant
class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

    def __str__(self):
        return f'{self.name}, {self.cuisine}, {self.menu}'


class FastFood(Restaurant):
    def __init__(self, name: str, cuisine: str, menu: dict, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

        def __str__(self):
            return f'{self.name}, {self.cuisine}, {self.menu}, {self.drive_thru}'


class Menu:
    def __init__(self):
        self.dishes = {}

    def add_dish(self, dish, price, quantity=1):
        self.dishes[dish] = {'price': price, 'quantity': quantity}

    def remove_dish(self, dish):
        if dish in self.dishes:
            del self.dishes[dish]

    def get_menu(self):
        return self.dishes

    def order(self, dish: str, quantity: int):
        if dish not in self.dishes:
            return f'{dish} is not served in this restaurant'
        if quantity > self.dishes[dish]['quantity']:
            return f'There is not enough {dish} available for order'
        price = self.dishes[dish]['price']
        total_sum = price * quantity
        self.dishes[dish]['quantity'] -= quantity
        return f'Total cost of your order: {total_sum}'


# bank

class Account:
    def __init__(self, number: int, balance: float):
        self.number = number
        self.balance = float
    
    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def __str__(self):
        return f'{self.number}:{self.balance}'

class SavingsAccount(Account):
    def __init__(self, number: int, balance: float, interest_rate: float)
        super().__init__(number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest

    def __str__(self):
        return f'{self.number}:{self.balance} with {self.interest_rate} interest'

class CurrentAccount(Account):
    def __init__(self, number: str, balance: float, overdraft: float)
        super().__init__(number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if self.overdraft < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def __str__(self):
        return f'{self.number}:{self.balance} with {self.overdraft} as max overdraft limit'


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account):
        self.accounts.append(account)

    def close_account(self, number):
        for account in self.accounts:
            if account.number == number:
                self.accounts.remove(account)
                print (f'Account {number} has been closed')
                return
            else:
                print (f'Account {number} has not been found')

    def upd(self):
        for account in self.accounts:
            if isinstance (account, SavingsAccount):
                account.add_interest
            if isinstance (account, CurrentAccount) and account.balance < 0:
                print (f'Your account {account.number} is in overdraft of {account.overdraft}')

    def pay_dividend(self, dividend):
        for account in self.accounts:
            account.deposit(dividend)
            print(f'{dividend} has been paid to the account {account.number}')

    def __str__(self):
        return f'Opened accounts:{self.accounts}'
    

account_1 = SavingsAccount("123", 1000, 1.5)
account_2 = SavingsAccount("124", 1500, 1.7)
account_3 = SavingsAccount("125", 9000, 1.9)
account_4 = CurrentAccount ("126", 200, 2000)
account_5 = CurrentAccount ("127", 55, 600)

bank = Bank()
bank.open_account(account_1)
bank.open_account(account_2)
bank.open_account(account_3)
bank.open_account(account_4)
bank.open_account(account_5)