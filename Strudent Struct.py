class Student:
    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


# Create student object
s1 = Student(101, "Nishant", 19, 85)

# Display student details
s1.display()
