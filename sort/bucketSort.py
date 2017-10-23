class BucketSort:
    _buckets = []

    def __init__(self):
        pass

    def _getMaxNumber(self, inputList):
        maximum = inputList[0]
        for itr in inputList:
            if itr > maximum:
                maximum = itr
        return maximum

    def _prepareBuckets(self, numberOfBuckets):
        for itr in range(numberOfBuckets):
            self._buckets.append([])

    def sort(self, inputList):
        outputList = []
        self._prepareBuckets(self._getMaxNumber(inputList) + 1)
        for itr in inputList:
            self._buckets[itr].append(itr)

        for itr in self._buckets:
            outputList.extend(itr)
        return outputList
