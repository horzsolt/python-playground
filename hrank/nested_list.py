import unittest

class Testing(unittest.TestCase):

    def get_Second(self, inputList):
        inputList.sort(key=lambda l: l[1])
        scores = [x[1] for x in inputList]
        return list(set(scores))[1]

    def test_Create_Nested_List(self):
        # Create nested list from scratch

        nested = []
        for x in range(5):
            nested.append(['a', x])

        self.assertEqual(nested[0], ['a',0])

    def test_Sort(self):
        # Given the names and grades for each student in a class of students, store them in a nested list and print the name(s) of
        # any student(s) - in alphabetical order - having the second lowest grade.

        students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
        score = self.get_Second(students)
        names = [x[0] for x in students if x[1] == score]
        names.sort()
        self.assertEqual(names, ['Berry', 'Harry'])

        students = [['Harsh', 20], ['Beria', 20], ['Varun', 19], ['Kakunami', 19], ['Vikas', 21]]
        score = self.get_Second(students)
        names = [x[0] for x in students if x[1] == score]
        names.sort()
        self.assertEqual(names, ['Beria', 'Harsh'])



if __name__ == '__main__':
    unittest.main()
