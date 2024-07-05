class Array():
    def __init__ (self):
        self.size = 0
        self.array = []

    def append(self, item):
        """ Add """
        self.array.append(item)
        self.size += 1

    def delete(self, item):
        self.array.pop(item)
        self.size -= 1

    def insert(self, item, index):
        self.array[index] = item

    def print(self):
        print(self.array)
