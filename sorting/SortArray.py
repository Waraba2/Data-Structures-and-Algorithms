# Implement a sortable Array data structure
class Array(object):
    def __init__(self, initialSize):    # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0                # No items in array initially

    def __len__(self): # Special def for len() func
        return self.__nItems # Return number of items

    def get(self, n):
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
            return self.__a[n]            # only return item if in bounds

    def set(self, n, value):            # Set the value at index n
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
            self.__a[n] = value           # only set item if in bounds

    def swap(self, j, k):
        if (0 <= j and j < self.__nItems 
                and 0 <= k and k < self.__nItems):
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def swap(self, j, k):               # Swap the values at 2 indices
        if (0 <= j and j < self.__nItems and # Check if indices are in
            0 <= k and k < self.__nItems): # bounds, before processing
            self.__a[j], self.__a[k] = self.__a[k], self.__a[j]

    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
        return -1

    def search(self, item):
        return self.get(self.find(item)) # and return item if found

    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                self.__nItems -= 1
            for k in range(j, self.__nItems):  # Move items from
                self.__a[k] = self.__a[k+1]     # right over 1
            return True                # Return success flag
        return False     # Made it here, so couldn’t find the item 
        
    def traverse(self, function=print): # Traverse all items
        for j in range(self.__nItems):   # and apply a function
            function(self.__a[j])

    def __str__(self):
      ans = "["
      for i in range(self.__nItems):
         if len(ans) > 1:
            ans += ", "
         ans += str(self.__a[i])
      ans += "]"
      return ans

    # YOUTUBE: Interesting implementation of bubbleSort 
    def bubbleSort(self):
        for last in range(self.__nItems - 1, 0, -1):
            for inner in range(last):
                if self.__a[inner] > self.__a[inner + 1]:
                    self.swap(inner, inner + 1)

    def selectionSort(self):
        for outer in range(self.__nItems - 1):
            min = outer
            for inner in range(outer + 1, self.__nItems):
                if self.__a[inner] < self.__a[min]:
                    min = inner
            self.swap(outer, min)
    
    def insertionSort(self):
        for outer in range(1, self.__nItems):
            temp = self.__a[outer]
            inner = outer
            while inner > 0 and temp < self.__a[inner - 1]:
                self.__a[inner] = self.__a[inner - 1]
                inner -= 1
            self.__a[inner] = temp


arr = Array(10)

arr.insert(5)
arr.insert(0)
arr.insert(33)
arr.insert(7)
arr.insert(70)

print(arr)

# arr.bubbleSort()
# arr.selectionSort()
arr.insertionSort()


print(arr)


