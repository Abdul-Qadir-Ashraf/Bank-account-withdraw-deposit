from os import system
class Person():
    def __init__(self,first,last):
        self.first = first
        self.last = last

class Customer(Person):
    def __init__(self,first,last,balance,account):
        self.account = account
        self.balance = balance
        super().__init__(first,last)

    def __str__(self):
        return (f'Name = {self.first}  {self.last}\nAccount no. = {self.account}\nAccount balance = {self.balance}')
    def deposit(self,amount):
        self.balance+=amount
        print('Balance accepted')
    def withdraw(self,draw):
        if draw>self.balance:
            print("\ninsufficient fund!!!!!!!!!!\n")
        else:
            self.balance = self.balance-draw
            system('cls')

def asking():
    a = input("Enter your first name: ")
    b = input('Enter your last name: ')
    c = int(input("Enter Your Account no: "))
    d = int(input("Enter Your Account balance: "))
    return a,b,c,d

def deposit():
    a = int(input("Enter the amount you want to deposit: "))
    return a

def withdraw():
    a = int(input("Enter the amount you want to withdraw: "))
    return a
def start():
    a,b,c,d = asking()
    details = Person(a,b)
    account = Customer(a,b,d,c)
    system("cls")
    bank = 0
    while bank!=1:
        print(account)
        A = int(input('Choose from the following option:\n1. Deposit Money\n2. Withdraw Money\n3. Exit\n'))

        if A==1:
            m = deposit()
            account.deposit(m)
            system('cls')

        elif A==2:
            n = withdraw()
            account.withdraw(n)
        elif A==3:
            print("bye")
            bank = 1
        else:
            continue

start()

