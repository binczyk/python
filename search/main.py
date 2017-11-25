import time

from search.dictionary import Dictionary
from search.force import Force
from search.sunday import Sunday
from decimal import getcontext, Decimal

getcontext().prec = 50

text = 'jakiabs tekst cabbc dbe efg cos abtam dalej'
pattern = 'abbc'

start = time.perf_counter()
# force = Force(text, pattern)
force = Force(Dictionary.LONG_TEXT.value, Dictionary.MEDIUM_PATTERN.value)
print('Force')
print(str(force.search()) + ' number of comparison: ' + str(force.numberOfLoops))
end = time.perf_counter()
print('took: ' + str(Decimal(end - start)))

start = time.perf_counter()
# sunday = Sunday(text, pattern)
sunday = Sunday(Dictionary.LONG_TEXT.value, Dictionary.MEDIUM_PATTERN.value)
print('Sunday')
print(str(sunday.search()) + ' number of comparison: ' + str(sunday.numberOfLoops))
end = time.perf_counter()
print('took: ' + str(Decimal(end - start)))
