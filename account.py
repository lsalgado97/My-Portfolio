# In this code, I'm defining a class to emulate bank accounts. An Account object holds the
# account number, the account holder's name, the account's balance, and a negative balance
# limit, which is set by standard as R$1000, but can be changed via a setter.

# This code was written in the context of a python learning course, and has the purpose of
# introducing object oriented programming, by defining classes and objects with their
# constructor, attributes, methods and properties. Also, this code shows encapsulation and
# defining private attributes and methods.

class Account:

    # This is the Account object constructor. It's attributes are defined as private
    # (by using the '__'), which means someone using the class should not access them
    # directly, but rather via the getters and setters defined later in the code.
    def __init__(self, number, holder, balance, limit=1000.00):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def statement(self):
        print("{}'s account balance: R${:.2f}".format(self.__holder, self.__balance))

    def deposit(self, value):
        self.__balance += value

    # This method checks if the account holder can withdraw a given value. It is a private
    # method, meant to be used internally by the class, not by the user.
    def __check_limit(self, value):
        available = self.__balance + self.__limit
        return value <= available

    def withdraw(self, value):
        if self.__check_limit(value):
            self.__balance -= value
        else:
            print("This withdraw of R${:0.2f} surpasses your limit".format(value))

    def transfer(self, value, destination):
        self.withdraw(value)
        destination.deposit(value)

    # The following properties are getters, and are the way an user may access the
    # attributes of an account object (but not change them!)
    @property
    def balance(self):
        return self.__balance

    @property
    def number(self):
        return self.__number

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    # This is a setter for the limit property. It is used should the user wish to
    # change the limit of a given account object.
    @limit.setter
    def limit(self, value):
        self.__limit = value

    # This is a small example of a static method: all accounts in this class are
    # in a bank with code 001
    @staticmethod
    def bank_code():
        return "001"
