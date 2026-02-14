name_list = ["krutoy"]
surname_list = ["sigma"]
age_list = [10] 

class Person:
    def __init__(self, birthyear1, name1, surname1, pol1):
        self.birthyear = birthyear1
        self.name = name1
        self.surname = surname1
        self.pol = pol1
        self.hobbies = []

krutoy = Person(2011, "Fkrutoy", "sigma", "M")


class Student:
    def __init__(self, name1, surname1, birthyear1, avg_grade1, course1 = "MKA"):
        self.name = name1
        self.surname = surname1
        self.birthyear = birthyear1
        self.course = course1
        self.hobbies = []
        self.avg_grade = avg_grade1

    def study(self):
        print(f"{self.name} is studying")

    def show_info(self):
        print(f"{self.name} {self.surname} : {self.course}")
        print(f"avg_grade: {self.avg_grade}")
        print(f"age: {2026 - self.birthyear}")
        print(f"hobbies: {self.hobbies}")

Emil = Student("krutoy", "sigma", 2016, 9.3, "PKO")
Emil.show_info()
Emil.study()