from search.patternSearch import PatternSearch


class Force(PatternSearch):
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def search(self):
        patternLen = len(self.pattern)
        for itr in range(len(self.text) - patternLen):
            self.numberOfLoops += 1
            if self.text[itr:itr + patternLen] == self.pattern:
                return itr;
        return 'NaN'
