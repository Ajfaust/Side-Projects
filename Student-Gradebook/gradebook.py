#!usr/bin/python

# Author: Andrew Faust
# Date: September 7, 2017

# Student Gradebook
# A simple student gradebook that allows the user to add students to a class and
# record grades and averages.

# Student class
# @name: Student name
# @avg: Student's running average
# @scores: List of student's scores per assignment
# @grade: Student grade
class Student:
    def __init__(self, name, scores=[]):
        self.name = name
        self.avg = 0.0 if scores == [] else self.calcAvg(scores)
        self.scores = scores
        self.grade = "N/A"

    def __str__(self):
        return 'Name: ' + self.name\
            + '\nAverage: ' + str(self.avg)\
            + '\nRecent scores: ' + ', '.join([str(s) for s in
                self.scores[-5:]])\
            + '\nCurrent grade: ' + self.grade

    def calcAvg(self, scores):
        return sum(self.scores) / (100 * len(self.scores))
    
    # Adds a new score to the Student's list of scores and calculates the new
    # average.
    def addScore(self, score):
        self.scores.append(score)
        n = len(self.scores)
        self.avg = ((n - 1) * self.avg + score) / n

# Class class
# @subj: Class subject
# @crn: Class crn
# @students: Dictionary of student names mapped to appropriate Student classes
class Class:
    def __init__(self, subj, crn, students):
        self.subject = subj
        self.crn = crn
        self.students = students

    def addStudent(self, name):
        self.students[name] = Student(name)

    def printStudentInfo(self, students):
        for student in self.students:
            return str(student)

    def assign_grades_norm(self, students):
        for student in student:
            if student.scores == []:
                student.grade = "N/A"
            elif student.avg >= 90:
                student.grade = "A"
            elif student.avg >= 80:
                student.grade = "B"
            elif student.avg >= 70:
                student.grade = "C"
            elif student.avg >= 60:
                student.grade = "D"
            else:
                student.grade = "F"
