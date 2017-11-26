class PatternSearch(object):
    numberOfLoops = 0
    _patternLen = 0

    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self._patternLen = len(pattern)

    def search(self):
        raise Exception("NotImplementedException")
