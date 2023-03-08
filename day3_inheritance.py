#this script uses more modern string formatting 

#person class
class Person:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def printFullName(self):
        print( f"Full Name: {self.firstName} {self.lastName}")
#end class

# student class
class Student(Person):
    def __init__(self,firstName,lastName,subject):
        Person.__init__(self,firstName,lastName)
        self.subject = subject
        
    def printFullNameAndSubject(self):
        print(f"Full Name: {self.firstName} {self.lastName} Subject: {self.subject}")
#end class

#teacher class
class Teacher(Person):
    def __init__(self, firstName, lastName, courseName):
        Person.__init__(self,firstName,lastName)
        self.courseName = courseName
    
    def printNameAndCourse(self):
        print(f"Full Name: {self.firstName} {self.lastName} Course: {self.courseName}")
#end class       
        
#testing the classe by crating objects
p1=Person("Bob","Ross")
p1.printFullName()

s1=Student("Rob","Smith","chemistry")
s1.printFullNameAndSubject()

t1=Teacher("Nick","Payge","electromagnetismI")
t1.printNameAndCourse()