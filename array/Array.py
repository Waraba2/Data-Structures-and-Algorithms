class Array(object):
    """Implement an Array data structure as a simplified type of list."""
    def __init__(self, initialSize): # Constructor
        self.__a = [None] * initialSize # The array strored as a list
        self.__nItems = 0 # No items in the array initially

    def __len__(self): 
        """Special def for len() function"""
        return self.__nItems # Return number of items

    def get(self, n):
        """Return value at index n"""
        if 0 <= n and n < self.__nItems: # Check if n is in the bounds, and
            return self.__a[n]                # only return item if in bounds

    def set(self, n, value):
        """Set the value at index n"""
        if 0 <= n and n < self.__nItems: # Check if n is in the bounds, and
            self.__a[n] = value          # only set items if in bounds
    
    def insert(self, item):
        """Insert item at the end"""
        self.__a[self.__nItems] = item # Item goes at current end
        self.__nItems += 1             # Icrement the number of items

    def find(self, item):
        """Find index for item"""
        for j in range(self.__nItems): # Among current items
            if self.__a[j] == item:    # If found,
                return j               # then return index to item
        return -1                      # Not found -> -1

    def search(self, item):
        """Search for item return item if found"""
        return self.get(self.find(item)) 

    def delete(self, item):
        """Delete first occurrence of an item"""
        for j in range(self.__nItems):
            if self.__a[j] == item: # Found item
                self.__nItems -= 1  # One fewer at the end
                for k in range(j, self.__nItems): # Move items from
                    self.__a[k] = self.__a[k + 1] # right over 1
                return True                       # Return success flag

        return False # Made it here, so couldn't find the item

    def traverse(self, function=print):
        """Traverse all items"""
        for j in range(self.__nItems):
            function(self.__a[j])
