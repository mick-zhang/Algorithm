class Student:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + "@company.com"
    
    def getName(self):
        return self.first + " " + self.last
    
    def __str__(self):
        return self.first + " " + self.last
    
    def __repr__(self):
        return self.first + " " + self.last    

class Staff(Student):
    
    def __init__(self, first, last, pay):
        super(Staff, self).__init__(first, last)
        
        self.pay = pay

    def getSalary(self):
        return self.first + " " + self.last + "'s Salary is: " + str(self.pay)
    
class Faculty(Staff):
    
    def __init__(self, first, last, pay):
        super(Faculty,self).__init__(first, last, pay)
    
    def changePay(self):
        newpay = input("Please enter updated pay for " + self.first + " " + self.last + ": ")
        self.pay = newpay
        return self.first + " " + self.last + "'s Updated Salary is: " + str(self.pay)
    
def main():
    john = Student("John", "Smith")
    larry = Staff("Larry", "Wilson", 50000)
    michael = Faculty("Michael", "Thompson", 50000)
    
    result = [john.getName(), john.email,
              larry.getName(), larry.email, larry.getSalary(),
              michael.getName(), michael.email, michael.getSalary(), michael.changePay()]
    
    for results in result:
        print(results)
        
main()
