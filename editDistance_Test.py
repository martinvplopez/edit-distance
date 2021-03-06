import unittest
import editDistance

class TestEdit(unittest.TestCase):

    def test_distance1(self):
        result,_= editDistance.editDistanceMemo("cat", "gato")
        self.assertEqual(result,2)

        result,_= editDistance.editDistanceMemo("", "")
        self.assertEqual(result,0)

        result,_= editDistance.editDistanceMemo("","man")
        self.assertEqual(result,3)

        result,_= editDistance.editDistanceMemo("Hello", "hello")
        self.assertEqual(result,1)

    def test_distance2(self):
        result1,_= editDistance.editDistanceMemo("cat", "gato")
        result2,_= editDistance.editDistanceTabu("cat", "gato")
        self.assertEqual(result1,result2)

        result1,_= editDistance.editDistanceMemo("", "")
        result2,_= editDistance.editDistanceTabu("", "")
        self.assertEqual(result1,result2)

        result1,_= editDistance.editDistanceMemo("","man")
        result2,_= editDistance.editDistanceTabu("","man")
        self.assertEqual(result1,result2)

        result1,_= editDistance.editDistanceMemo("Hello", "hello")
        result2,_= editDistance.editDistanceTabu("Hello", "hello")
        self.assertEqual(result1,result2)

if __name__ == '__main__':
    unittest.main()
