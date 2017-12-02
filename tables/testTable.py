import random
import time
from decimal import getcontext, Decimal

from tables.abstractTable import AbstractTable


class TestTable(AbstractTable):
    _list = []
    _find = []

    def prepare(self):
        for _ in range(self.listRange):
            self._list.append(random.randrange(self.randomRange))

        for _ in range(self.findRange):
            self._find.append(random.randrange(self.randomRange))

    def __init__(self, abstractTable, listRange, findRange, randomRange):
        getcontext().prec = 100
        self.abstractTable = abstractTable
        self.listRange = listRange
        self.findRange = findRange
        self.randomRange = randomRange
        self.prepare()
        print('---Start---')
        print(type(abstractTable))

    def test(self):
        self.testAdd()
        self.testExists()
        self.testRemove()
        print('---End---')

    def testRemove(self):
        start = time.perf_counter()
        for i in self._find:
            self.abstractTable.remove(i)
        end = time.perf_counter()
        print('Removing time: ', Decimal(end - start))

    def testExists(self):
        start = time.perf_counter()
        for i in self._find:
            self.abstractTable.exists(i)
        end = time.perf_counter()
        print('Checking if exists time: ', Decimal(end - start))

    def testAdd(self):
        start = time.perf_counter()
        for i in self._list:
            self.abstractTable.add(i)
        end = time.perf_counter()
        print('Adding time: ', Decimal(end - start))
