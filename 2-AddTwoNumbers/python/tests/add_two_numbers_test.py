import unittest
from python.src import add_two_numbers_1

class Test_Add2Numbers(unittest.TestCase):
    def setUp(self) -> None:
        self.list1 = [2,4,3]
        self.list2 = [5,6,4]
        self.solution = [7,0,8]
        self.s = add_two_numbers_1.Solution()

    def runTest(self):
        result = self.s.addTwoNumbers(self.list1, self.list2)
        self.assertIn(result, self.solution)

if __name__ == '__main__':
    unittest.main()