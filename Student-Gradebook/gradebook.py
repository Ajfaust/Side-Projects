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
        self.scores = scores
        self.avg = 0.0 if scores == [] else self.calcAvg()
        self.grade = "N/A"

    def __str__(self):
        return 'Name: ' + self.name\
                + '\nAverage: {:.2f}'.format(self.avg)\
            + '\nRecent scores: ' + ', '.join(
                    [str(s) for s in reversed(self.scores[-5:])])\
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
    
    def calcGrade(self, mean, std_dev):
        # Calculate grade based on typical percent range if no stats are given
        if mean < 0:
            if self.avg >= 90: self.grade = "A"
            elif self.avg >= 80: self.grade = "B"
            elif self.avg >= 70: self.grade = "C"
            elif self.avg >= 60: self.grade = "D"
            else: self.grade = "F"
            return
        
        # Otherwise, grade on a bell curve, with the average being a C
        if self.avg >= mean + 2 * std_dev: self.grade = "A"
        elif self.avg >= mean + std_dev: self.grade = "B"
        elif self.avg >= mean - std_dev: self.grade = "C"
        elif self.avg >= mean - 2 * std_dev: self.grade = "D"
        else: self.grade = "F"

# Course class
# @subj: Course subject
# @crn: Course crn
# @students: Dictionary of student names mapped to appropriate Student classes
class Course:
    def __init__(self, subj, crn, students={}):
        self.subject = subj
        self.crn = crn
        self.students = students

    # Printing out a course will print out info for all registered students
    def __str__(self):
        output = ""
        for student in self.students.values():
            output += str(student) + '\n'\
                      + '-' * 20 + '\n'
        return output

    def addStudent(self, name):
        self.students[name] = Student(name)
    
    # Calculates student statistics for bell curve grading.
    # Returns [mean, standard deviation]
    def getStats(self):
        sum_avgs = sum([s.avg for s in self.students.values()])
        mean = sum_avgs / len(self.students)
        stdev_num = 0.0
        for student in self.students.values():
            stdev_num += pow((student.avg - mean), 2)
        stdev_sq = stdev_num / (len(self.students) - 1)
        return mean, sqrt(stdev_sq)
    
    # Updates grades for all students on a normal scale or a bell curve
    def updateGrades(self, scale="norm"):
        stats = self.getStats() if scale == "bell" else [-1, -1]
        for student in self.students.values():
            student.calcGrade(stats[0], stats[1])
