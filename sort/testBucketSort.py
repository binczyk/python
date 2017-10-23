import random
import unittest

from sort.bucketSort import BucketSort


class TestBucketSort(unittest.TestCase):
    testList = []
    outputList = []
    testListRange = 1000
    randomRange = 10000

    @classmethod
    def setUpClass(cls):
        bs = BucketSort()

        for itr in range(cls.testListRange):
            cls.testList.append(random.randrange(cls.randomRange))
        cls.outputList = bs.sort(cls.testList)

    def test_checkCorrectSize(cls):
        cls.assertTrue(cls.testListRange, len(cls.outputList))

    def test_checkCorrectOrder(cls):
        for itr in range(len(cls.outputList) - 1):
            cls.assertTrue(cls.outputList[itr] <= cls.outputList[itr + 1])

    def test_outputListContainsTheSameNumbers(cls):
        cls.assertTrue(cls.returnNotMatches(cls.outputList, cls.testList))

    def returnNotMatches(cls, list_a, list_b):
        list_a = set(list_a)
        list_b = set(list_b)
        return [list(list_b - list_a), list(list_a - list_b)]


if __name__ == '__main__':
    unittest.main()
