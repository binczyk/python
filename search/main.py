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
numberOfCompersion = []

text = ''.join(random.choice(string.ascii_letters) for _ in range(text_length))
pattern = text[99000:100000]

patternSearchTest = PatternSearchTest(Force(text, pattern));
numberOfCompersion.append(patternSearchTest.test())

patternSearchTest = PatternSearchTest(SundayCustom(text, pattern));
numberOfCompersion.append(patternSearchTest.test())

patternSearchTest = PatternSearchTest(Sunday2charCustom(text, pattern));
numberOfCompersion.append(patternSearchTest.test())

patternSearchTest = PatternSearchTest(SundayOriginal(text, pattern));
numberOfCompersion.append(patternSearchTest.test())

patternSearchTest = PatternSearchTest(Sunday2charOriginal(text, pattern));
numberOfCompersion.append(patternSearchTest.test())

graph = Graph(numberOfCompersion)
graph.draw()
