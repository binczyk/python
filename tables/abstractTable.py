class AbstractTable:
    def __init__(self):
        self.table = []

    def add(self, value):
        raise Exception("NotImplementedException")

    def exists(self, value):
        raise Exception("NotImplementedException")

    def remove(self, value):
        raise Exception("NotImplementedException")
