import random
import string

from search.force import Force
from search.graph import Graph
from search.patternSearchTest import PatternSearchTest
from search.sunday2charCustom import Sunday2charCustom
from search.sunday2charOriginal import Sunday2charOriginal
from search.sundayCustom import SundayCustom
from search.sundayOriginal import SundayOriginal

text_length = 100000
numberOfCompersion = {}
algorithmTime = {}

text = ''.join(random.choice(string.ascii_letters) for _ in range(text_length))
pattern = text[99000:100000]

patternSearchTest = PatternSearchTest(Force(text, pattern))
# patternSearchTest.test()
numberOfCompersion['Force'] = patternSearchTest.test()
algorithmTime['Force'] = patternSearchTest.time

patternSearchTest = PatternSearchTest(SundayCustom(text, pattern))
numberOfCompersion['SundayCustom'] = patternSearchTest.test()
algorithmTime['SundayCustom'] = patternSearchTest.time

patternSearchTest = PatternSearchTest(Sunday2charCustom(text, pattern))
numberOfCompersion['Sunday2charCustom'] = patternSearchTest.test()
algorithmTime['Sunday2charCustom'] = patternSearchTest.time

patternSearchTest = PatternSearchTest(SundayOriginal(text, pattern))
numberOfCompersion['SundayOriginal'] = patternSearchTest.test()
algorithmTime['SundayOriginal'] = patternSearchTest.time

patternSearchTest = PatternSearchTest(Sunday2charOriginal(text, pattern))
numberOfCompersion['Sunday2charOriginal'] = patternSearchTest.test()
algorithmTime['Sunday2charOriginal'] = patternSearchTest.time

graph = Graph(algorithmTime, numberOfCompersion)
graph.draw()
