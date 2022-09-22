import unittest
from filename.py import sort_square

class TestProgram(unittest.TestCase):

    def test_square(self):
        arr = [1,2,3,5,6,8,9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        self.compare(expected, output)



    if __name__ == '__main__':
        main()