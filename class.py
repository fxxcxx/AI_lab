class Employee:
empCount = 0

def __init__(self, name, salary):
  self.name = name
  self.salary = salary
  Employee.empCount += 1
  
def displayCount(self):
  print("Total Employee %d" % Employee.empCount)

def displayEmployee(self):
  print("Name : ", self.name, ", Salary: ", self.salary)
  
emp1 = Employee("zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
#Name : Zara, salary: 2000
emp2.displayEmployee()
#Name : Manni, salary: 5000

emp1.salary= 7000
emp1.name = 'xyz'
del emp1.salary

hasattr(emp1, 'salary')
False #속성이 존재하면 true 아니면 false

getattr(emp1, 'salary')
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    getattr(emp1, 'salary')
AttributeError: 'Employee' object has no attribute 'salary'
#객체 값을 return, 현재는 없으므로 err
  

setattr(emp1, 'salary', 7000) 
#객체 값을 설정


getattr(emp1, 'salary')
7000 #값 return

delattr(emp1, 'salary') #delete

getattr(emp1, 'salary')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    getattr(emp1, 'salary')
AttributeError: 'Employee' object has no attribute 'salary'
#err again lol
