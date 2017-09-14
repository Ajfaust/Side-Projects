import unittest
from gradebook import Student, Course

class TestStudentMethods(unittest.TestCase):
    def setUp(self):
        self.s = Student('Andrew', [56, 78, 98, 90, 94, 87])

    def testAvg(self):
        self.assertAlmostEqual(self.s.avg, 83.83, places=2)
    
    def testScores(self):
        self.failUnless(self.s.scores == [56, 78, 98, 90, 94, 87])
    
    def testGrade(self):
        self.s.calcGrade(-1, -1)
        self.failUnless(self.s.grade == "B")
    
    def testAddScore(self):
        self.s.addScore(67)
        self.failUnless(self.s.scores == [56, 78, 98, 90, 94, 87, 67])
        self.assertAlmostEqual(self.s.avg, 81.43, places=2)

class TestCourseMethods(unittest.TestCase):
    def setUp(self):
        self.c = Course("Biology", 48364, 
                {'Andrew': Student("Andrew", [56, 78, 98, 90, 94, 87]),
                 'Mary': Student("Mary", [48, 91, 76, 86, 77, 95]),
                 'John': Student("John", [67, 56, 65, 45, 76, 55])
                })
        self.c.updateGrades()
    
    def testGrades(self):
        self.failUnless(self.c.students['Andrew'].grade == "B")
        self.failUnless(self.c.students['Mary'].grade == "C")
        self.failUnless(self.c.students['John'].grade == "D")

    def testStats(self):
        stats = self.c.getStats()
        self.assertAlmostEqual(stats[0], 74.44, places=2)
        self.assertAlmostEqual(stats[1], 12.19, places=2)

    def testBellCurve(self):
        self.c.updateGrades("bell")
        self.failUnless(self.c.students['Andrew'].grade == "C")
        self.failUnless(self.c.students['Mary'].grade == "C")
        self.failUnless(self.c.students['John'].grade == "D")
        

def main():
    unittest.main()

if __name__ == '__main__':
    main()
