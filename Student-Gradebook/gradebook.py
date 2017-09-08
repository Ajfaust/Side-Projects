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
class Student:
    def __init__(self, name, avg, scores):
        self.name = name
        self.avg = avg
        self.scores = scores

    def __str__(self):
        return 'Name: ' + self.name\
            + '\nAverage: ' + str(self.avg)\
            + '\nRecent scores: ' + ', '.join([str(s) for s in
                self.scores[-5:]])

    def addScore(self, score):
        self.scores.append(score)

    def calcAvg(self):
        self.avg = sum(self.scores) / (100 * len(self.scores))

# Class class
# @subj: class subject
# @crn: class crn
# @students: Dictionary of student names mapped to appropriate Student classes
class Class:
    def __init__(self, subj, crn, students):
        self.subject = subj
        self.crn = crn
        self.students = students

    def addStudent(self, name):
        self.students[name] = Student(name, 0, [])

    def printStudentInfo(self, students):
        for student in self.students:
            return str(student)
