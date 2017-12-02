from tables.openHashTable import OpenHashTable
from tables.hashTable import HashTable
from tables.sortedTable import SortedTable
from tables.table import Table
from tables.testTable import TestTable

listRange = 1000
findRange = 100
randomRange = 999999

tableTest = TestTable(Table(), listRange, findRange, randomRange)
tableTest.test()

sortedTableTest = TestTable(SortedTable(), listRange, findRange, randomRange)
sortedTableTest.test()

hashTable = TestTable(HashTable(listRange), listRange, findRange, randomRange)
hashTable.test()

chainedTable = TestTable(OpenHashTable(listRange), listRange, findRange, randomRange)
chainedTable.test()
