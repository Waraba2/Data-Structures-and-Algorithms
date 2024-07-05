class Array(object):

    def __init__(self, initialSize): # constructor
        self.__a = [None] * initialSize          # The array stored as a list
        self.nItems = 0 # No items in array initially

    def insert(self, item):
        """Insert item at the end"""
        self.__a[self.nItems] = item # Item goes at current end
        self.nItems += 1 # Increment the number of items

    def search(self, item):
        """Search among current"""
        for j in range(self.nItems):
            if self.__a[j] == item: # If found
                return self.__a[j] # The return items

        return None # Not found -> None

    def delete(self, item):
        """Delete the first occurence"""
        for j in range(self.nItems):
            if self.__a[j] == item: # Found item
                for k in range(j, self.nItems):   # Move items from
                    self.__a[k] = self.__a[k + 1] # right over 1
                self.nItems -= 1                  # One fewer in array now
                return True                       # Return success flag
        return False                              # Made it here, so couldn't find item

    def traverse(self, function=print): # Traverse all items
        for j in range(self.nItems):    # and apply a function
            function(self.__a[j])
