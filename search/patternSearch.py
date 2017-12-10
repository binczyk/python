class PatternSearch(object):
    numberOfLoops = 0
    _patternLen = 0

    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self._patternLen = len(pattern)

    def search(self):
        raise Exception("NotImplementedException")

    def matchesAt(self, text, position, pattern):
        for itr in range(len(pattern)):
            self.numberOfLoops += 1
            if pattern[itr] != text[itr + position]:
                return False
        return True
