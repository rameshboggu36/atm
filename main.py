class ATM:

    def __init__(self):
        self.__db = {
            '22102030': {'name': 'Suresh Meesala', 'pin': '1234', 'balance': 50000, 'contact_num': '0123456789',
                         'email': 'sureshmeesala@gamil.com'},
            '22102402': {'name': 'Navya Nirmala', 'pin': '1234', 'balance': 50000, 'contact_num': '0123456789',
                         'email': 'navyanirmala@gamil.com'},
            '22102040': {'name': 'Rajsekhar Podilapu', 'pin': '1234', 'balance': 50000, 'contact_num': '0123456789',
                         'email': 'rajsekharpodilapu@gamil.com'},
            '22102065': {'name': 'Vishnupriya Mudisetty', 'pin': '1234', 'balance': 50000, 'contact_num': '0123456789',
                         'email': 'vishnuprya@gamil.com'},
            '22102020': {'name': 'Ramyapriya Duggirala', 'pin': '1234', 'balance': 50000, 'contact_num': '0123456789',
                         'email': 'ramyapriyaduggirala@gamil.com'},
            '22102017': {'name': 'Sanjana Gade', 'pin': '1234', 'balance': 50000, 'contact_num': '0123456789',
                         'email': 'sanjanagade@gamil.com'},
            '22102041': {'name': 'Ramesh Boggu', 'pin': '1234', 'balance': 50000, 'contact_num': '0123456789',
                         'email': 'rameshboggu@gamil.com'}
        }
        self.__in_id = input("Enter the ID:\n")
        self.__run = False
        self.menu(self.__in_id)

    def get_item(self, id, key):
        return self.__db[id][key]

    def set_value(self, id, key, value):
        self.__db[id][key] = value

    def menu(self, id):
        if id in self.__db.keys():
            self.__authenticate()
            name = self.__db[id]['name']
        else:
            print("Sorry! you are not an authorized user to use this ATM!!")

        while self.__run:
            user_input = input(f'''
      Hello {name}, how would you like to proceed:
      1. Enter 1 to Update PIN
      2. Enter 2 to Deposit
      3. Enter 3 to Withdraw
      4. Enter 4 to Check Balance
      5. Enter 5 to Exit\n''')

            if user_input == '1':
                self.__update_pin()
            elif user_input == '2':
                self.__deposit()
            elif user_input == '3':
                self.__withdraw()
            elif user_input == '4':
                self.__check_balance()
            elif user_input == '5':
                print("Exiting...")
                self.__run = False
            else:
                print("Invalid input. Select from the  given options.")

    def __update_pin(self):
        if self.__authenticate():
            updated_pin = input("Enter your new PIN:\n")
            self.set_value(self.__in_id, 'pin', updated_pin)
            print("ATM PIN updated successfully")

    def __deposit(self):
        if self.__authenticate():
            amount = self.__get_amount("Enter the amount to deposit:\n")
            updated_balance = self.get_item(self.__in_id, 'balance') + amount
            self.set_value(self.__in_id, 'balance', updated_balance)
            print("Deposit successful")
            print("Current balance after you Deposit is:", self.get_item(self.__in_id, 'balance'))

    def __withdraw(self):
        if self.__authenticate():
            amount = self.__get_amount("Enter the amount to withdraw:\n")
            if amount < self.get_item(self.__in_id, 'balance'):
                updated_balance = self.get_item(self.__in_id, 'balance') - amount
                self.set_value(self.__in_id, 'balance', updated_balance)
                print("Withdrawl successful")
                print("Current balance after your withdrawl is:", self.get_item(self.__in_id, 'balance'))
            else:
                print("Not enough funds in the account")

    def __check_balance(self):
        if self.__authenticate():
            print("Current balance:", self.get_item(self.__in_id, 'balance'))

    @staticmethod
    def __get_amount(prompt):
        try:
            amount = float(input(prompt))
            if amount < 0:
                print("Amount cannot be negative")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a valid numeric amount.")

    def __authenticate(self):
        attempts = 3
        while attempts > 0:
            temp = input("Enter the PIN:\n")
            if temp == self.get_item(self.__in_id, 'pin'):
                self.__run = True
                return self.__run
            else:
                print(f'Incorrect PIN!!\n{attempts - 1} attempts remaining.')
                self.__run = False
                attempts -= 1
        else:
            print("Too many incorrect attempts.\nExiting.....")
        return self.__run


# an instance of ATM class is created
if __name__ == '__main__':
    a = ATM()
