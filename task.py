# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.

from statistics import mean
import random

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.grades = dict()
        self.average = dict()
        self.attendance = []

    def add_grade(self, grade, subject):
        if(subject not in self.grades):
            self.grades[subject] = []
        self.grades[subject].append(grade)
        

    def count_average_grade(self):
        for i in self.grades:
            self.average[i] = round(mean(self.grades[i]), 2)
        total = 0
        count = 0
        for i in self.grades:
            total += sum(self.grades[i])
            count += len(self.grades[i])
        self.average["TOTAL"] = round(total / count, 2)

    def add_attendance(self, if_present):
        self.attendance.append("  {}  ".format(if_present))
    
    def if_present(self):
        return random.randint(0,1)


class Diary:
    def __init__(self, class_name, class_teacher_name = 'Brak'):
        self.class_name = class_name
        self.class_teacher_name = class_teacher_name
        self.students = []
        self.attendance_date = []

    def add_student(self, student):
        self.students.append(student)
    
    def check_attendance(self, current_date):
        self.attendance_date.append(current_date)
        for s in self.students:
            s.add_attendance(s.if_present())
    
    def get_average_grade(self):
        return round(mean(i.average["TOTAL"] for i in self.students), 2)

    def print_attendance(self):
        print(self.attendance_date)
        for i in self.students:
            print(i.attendance)



    




if __name__ == "__main__":
    diary = Diary("Klasa A", "Anna Nowak")

    marek = Student("Marek", "Nowak")
    adam = Student("Adam", "Kowalski")

    diary.add_student(marek)
    diary.add_student(adam)

    #Grades
    marek.add_grade(5, "Matematyka")
    marek.add_grade(3, "Matematyka")

    marek.add_grade(2, "Przyroda")
    marek.add_grade(3, "Przyroda")

    marek.add_grade(6, "Muzyka")

    adam.add_grade(1, "Matematyka")
    adam.add_grade(2, "Matematyka")

    adam.add_grade(3, "Przyroda")
    adam.add_grade(3, "Przyroda")

    adam.add_grade(6, "Muzyka")

    marek.count_average_grade()
    adam.count_average_grade()

    print("Oceny {} {}:".format(marek.name, marek.surname))
    print(marek.average)
    print("Oceny {} {}:".format(adam.name, adam.surname))
    print(adam.average)
    print("Average grade for class {} is: {}".format(diary.class_name, diary.get_average_grade()))

    #attendance:
    print("Attendance:")
    diary.check_attendance("31.03")
    diary.check_attendance("01.03")
    diary.check_attendance("02.03")

    diary.print_attendance()
