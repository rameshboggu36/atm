class Atm:
    def __init__(self):
        self.__pin = None
        self.__balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input('''
            Hello, how would you like to proceed:
            1. Enter 1 to Create PIN
            2. Enter 2 to Deposit
            3. Enter 3 to Withdraw
            4. Enter 4 to Check Balance
            5. Enter 5 to Exit\n''')

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print("Exiting...")
                break
            else:
                print("Invalid input")

    def create_pin(self):
        self.__pin = input("Enter your new PIN: ")
        print("ATM PIN created successfully")

    def withdraw(self):
        if self.authenticate():
            amount = self.get_amount_input("Enter the amount to withdraw: ")
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful")
            else:
                print("Not enough funds in the account")

    def deposit(self):
        if self.authenticate():
            amount = self.get_amount_input("Enter the amount to deposit: ")
            self.__balance += amount
            print("Deposit successful")

    def check_balance(self):
        if self.authenticate():
            print("Current balance:", self.__balance)

    def authenticate(self):
        temp = input("Enter your PIN: ")
        if temp == self.__pin:
            return True
        else:
            print("Incorrect PIN")
            return False

    @staticmethod
    def get_amount_input(prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount < 0:
                    print("Amount cannot be negative")
                else:
                    return amount
            except ValueError:
                print("Invalid input. Please enter a valid amount.")


# Create an instance of the Atm class
atm_instance = Atm()
