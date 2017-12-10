import time
from decimal import getcontext, Decimal

from search.patternSearch import PatternSearch


class PatternSearchTest(PatternSearch):

    def __init__(self, algorithm):
        getcontext().prec = 100
        self.algorithm = algorithm

    def test(self):
        print('-----START-----')
        print(type(self.algorithm))
        start = time.perf_counter()
        print('Found at: ', self.algorithm.search())
        end = time.perf_counter()
        print('Number of comparison: ' + str(self.algorithm.numberOfLoops))
        print('took: ' + str(Decimal(end - start)))
        print('------END------')
        return self.algorithm.numberOfLoops
