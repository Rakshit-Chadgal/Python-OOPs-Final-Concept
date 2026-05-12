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

'''
class Account:
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
acc1.debit(10000) #rent
'''

#Q3: Define a Circle class to create a circle with radius r using the constructor.
#    Define an Area() method of the class with calculates the area of the circle.
#    Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

'''
class Circle:
    def __init__(self, r):
        self.radius = r
        print("Radius is: ", self.radius)

    def Area(self, r):
        A_C = 3.14*r**2
        print("Area of circle is: ", A_C)

    def Perimeter(self, r):
        P_C = 2*3.14*r
        print("Perimeter of circle is: ", P_C)

rad = Circle(5) # Given the value of Radius of Circle
rad.Area(5) # Will Calculate the Area of the Circle with radius 5cm
rad.Perimeter(5) # Will Calculate the Perimeter of the Circle with radius 5cm
'''

#Q4: 