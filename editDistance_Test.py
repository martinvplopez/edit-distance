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

    def test_distance2(self):
        result1= editDistance.editDistanceMemo("cat", "gato")
        result2= editDistance.editDistanceTabu("cat", "gato")

        self.assertEqual(result1,result2)

        result1= editDistance.editDistanceMemo("", "")
        result2= editDistance.editDistanceTabu("", "")
        self.assertEqual(result1,result2)

        result1= editDistance.editDistanceMemo("","man")
        result2= editDistance.editDistanceTabu("","man")
        self.assertEqual(result1,result2)

        result1= editDistance.editDistanceMemo("Hello", "hello")
        result2= editDistance.editDistanceTabu("Hello", "hello")
        self.assertEqual(result1,result2)

# if __name__ == '__main__':
#     unittest.main()
