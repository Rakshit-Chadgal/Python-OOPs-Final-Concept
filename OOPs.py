#Q1 Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.
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

#Q2: Create Account class with 2 attributes - balance & account no.


#Q3: Create methods for debit, credit & printing the balance.