#!usr/bin/python

# Author: Andrew Faust
# Date: September 7, 2017

# Student Gradebook
# A simple student gradebook that allows the user to add students to a class and
# record grades and averages.
from math import sqrt

# Student class
# @name: Student name
# @avg: Student's running average
# @scores: List of student's scores per assignment
# @grade: Student grade
class Student:
    def __init__(self, name, scores=[]):
        self.name = name
        self.avg = 0.0 if scores == [] else self.calcAvg()
        self.scores = scores
        self.grade = "N/A"

    def __str__(self):
        return 'Name: ' + self.name\
                + '\nAverage: {:.2f}'.format(self.avg)\
            + '\nRecent scores: ' + ', '.join([str(s) for s in
                self.scores[-5:]])\
            + '\nCurrent grade: ' + self.grade
    
    # Calculates student avg based on current scores
    def calcAvg(self):
        return float(sum(self.scores)) / len(self.scores)
    
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
    def __init__(self, subj, crn, students={}):
        self.subject = subj
        self.crn = crn
        self.students = students

    def addStudent(self, name):
        self.students[name] = Student(name)

    def printStudentInfo(self):
        for student in self.students.values():
            return str(student)
    
    # Calculates student statistics for bell curve grading.
    # Returns [mean, standard deviation]
    def get_stats(self):
        sum_avgs = sum([s.avg for s in self.students.values()])
        mean = sum_avgs / len(self.students)
        stdev_num = 0.0
        for student in self.students.values():
            stdev_num += pow((student.avg - mean), 2)
        stdev_sq = stdev_num / (len(self.students) - 1)
        return mean, sqrt(stdev_sq)
    
    # Assigns all students a letter grade based on their avg score assuming
    # a typical grade range.
    def assign_grades_norm(self):
        for student in self.students.values():
            if len(student.scores) is 0:
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
