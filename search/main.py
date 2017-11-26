import time
from decimal import getcontext, Decimal

from search.force import Force
from search.sunday import Sunday
from search.sunday2char import Sunday2char

getcontext().prec = 50

text = 'bcbcaba2bbcab'
pattern = '2bbcab'

start = time.perf_counter()
force = Force(text, pattern)
# force = Force(Dictionary.LONG_TEXT.value, Dictionary.MEDIUM_PATTERN.value)
print('Force')
print(str(force.search()) + ' number of comparison: ' + str(force.numberOfLoops))
end = time.perf_counter()
print('took: ' + str(Decimal(end - start)))

start = time.perf_counter()
sunday = Sunday(text, pattern)
# sunday = Sunday(Dictionary.LONG_TEXT.value, Dictionary.MEDIUM_PATTERN.value)
print('Sunday')
print(str(sunday.search()) + ' number of comparison: ' + str(sunday.numberOfLoops))
end = time.perf_counter()
print('took: ' + str(Decimal(end - start)))

start = time.perf_counter()
sunday2char = Sunday2char(text, pattern)
# sunday2char = Sunday2char(Dictionary.LONG_TEXT.value, Dictionary.MEDIUM_PATTERN.value)
print('Sunday2char')
print(str(sunday2char.search()) + ' number of comparison: ' + str(sunday2char.numberOfLoops))
end = time.perf_counter()
print('took: ' + str(Decimal(end - start)))
