def identity(x): # The identity function
    return x

class OrderedRecordArray(object):
    """ Implement an ordered array data structure """
    def __init__(self, initialSize, key=identity):
        """ Contructor """
        self.__a = [None] * initialSize # The array stored as a list
        self.__nItems = 0               # No items in array initially
        self.__key = key                # Key function gets record key

    def __len__(self):
        """ Special def for len() function """
        return self.__nItems # Return the number of items

    def get(self, n):
        """ Return the value at index n """
        if 0 <= n and n < self.__nItems: # Check if n in bounds
            return self.__a[n]           # only return item if in bounds
        raise IndexError("Index" + str(n) + "is out of range")
    
    def traverse(self, function=print):
        """ Traverse all the items and apply a function """
        for j in range(self.__nItems):
            function(self.__a[j])

    def __str__(self):
        """ Special def for str() function """
        ans = "["                       # Surroud with square brackets

        for i in range(self.__nItems):  # Loop through items
            if len(ans) > 1:            # Except for left bracket
                ans += ", "             # Seprate items with comma
            
            ans += str(self.__a[i]) # Add string form of item

        ans += "]"                      # Close with right bracket

        return ans
    
    def find(self, key):
        """ Find index at or just below it """
        lo = 0                         # Item in ordered list
        hi = self.__nItems - 1         # Look between lo and hi

        while lo <= hi:
            mid = (lo + hi) // 2       # Select the midpoint

            if self.__key(self.__a[mid]) == key:  # Did we find it at midpoint
                return mid                    # Return the location of the item
            elif self.__key(self.__a[mid]) < key:        # Is item in upper half?
                lo = mid + 1           # Yes, raise to low boundarie
            else: 
                hi = mid - 1           # No, but could be in lower half

        return lo                      # Item not found, return insertion point
        
    def search(self, key):
        """ Search for item and return the item if found """
        idx = self.find(key)
        if idx < self.__nItems and self.__key(self.__a[idx]) == item:
            return self.__a[idx] # Return the item if found
    
    def insert(self, item):
        """ Insert item into correct position """
        if self.__nItems >= len(self.__a):    # If array if full
            raise Exception("Array overflow") # raise exception

        j = self.find(self.__key(item))       # Find index where item should go
        for k in range(self.__nItems, j, -1): # Move bigger items
            self.__a[k] = self.__a[k - 1]     # to the right

        self.__a[j] = item                    # Insert the item
        self.__nItems += 1                    # Increment the number of items

    def delete(self, item):
        """ Delete any occurence """
        j = self.find(self.__key(item))               # Try to find the item
        if j < self.__nItems and self.__a[j] == item: # If found,
            self.__nItems -= 1                        # One fewer item at end
            for k in range(j, self.__nItems):         # Move bigger items to the left
                self.__a[k] = self.__a[k + 1]
            return True                               # Return success flag
        return False                                  # Made it here, item not found

