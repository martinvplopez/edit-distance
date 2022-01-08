import unittest
import editDistance

class TestEdit(unittest.TestCase):

    def test_distance1(self):
        result= editDistance.editDistanceMemo("cat", "gato")
        self.assertEqual(result,2)

        result= editDistance.editDistanceMemo("", "")
        self.assertEqual(result,0)

        result= editDistance.editDistanceMemo("","man")
        self.assertEqual(result,3)

        result= editDistance.editDistanceMemo("Hello", "hello")
        self.assertEqual(result,1)

if __name__ == '__main__':
    unittest.main()