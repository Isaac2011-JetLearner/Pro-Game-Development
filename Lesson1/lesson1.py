class Student:
    def __init__(self,name,age,grade,school):
        self.name = name
        self.age = age
        self.grade = grade
        self.school = school
    
    def display_data(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"grade:{self.grade}")
        print(f"school:{self.school}")

mike = Student("mike",12,"10th","jet learn")
mike.display_data()
