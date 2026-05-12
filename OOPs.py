#Q1 Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
'''
class Student:
    def __init__ (self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)
s1 = Student("Rakshit", [99, 46, 89])
s1.get_avg()

s1.name = "ironman"
s1.get_avg()
'''

#Q2: Create Account class with 2 attributes - balance & account no. also create methods for debit, credit & printing the balance.
'''class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.balance =- amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())
    
    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total Balance = ", self.get_balance())

    def get_balance(self):
        print("Your balance is Rs.", self.balance)

acc1 = Account(10000, 12345)
acc1.credit(40000) #salary
acc1.debit(1000) #shopping
acc1.credit(500) #increment
acc1.debit(10000) #rent'''

#Q3: 