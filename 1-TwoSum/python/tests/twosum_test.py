import unittest
from src import twosum_2

class Test_TwoSum(unittest.TestCase):
    def setUp(self):
        self.s = twosum_2.Solution()
    
    def test1(self):
        solutions = [[0,1], [1,0]]
        answer = self.s.twoSum([2,7,11,15], 9)
        self.assertIn(answer, solutions)

if __name__ == '__main__':
    unittest.main()