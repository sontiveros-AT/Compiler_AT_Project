import fibo
import student
from package.birds import Birds

# this file
a = 1 + 2
print(a)
print("I'm in the client file")

# another file with functions
fibo.fib(1000)

# another class file
print(student.name)
nicholas = student.Student("Nicholas", "Computer Science")
nicholas.get_student_details()

# from package
myBird = Birds()
myBird.print_members()
