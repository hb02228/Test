import bisect

class USet:
    def __init__(self):
        '''Initializes member variables.

        >>> uset = USet()
        '''
        self._list = []

    def __str__(self):
        '''Returns a string representation of an object for printing.

        >>> uset = USet()
        >>> print(uset)  # prints uset.__str__()
        '''
        return str(self._list)

    def add(self, key, val):
        '''Adds the pair (key, val) to the USet if no pair with key
        already exists in the USet, and returns True. Returns False if a
        pair with key already exists in the USet.

        >>> uset = USet()
        >>> uset.add(1, 10)
        True
        >>> uset.add(2, 20)
        True
        >>> uset.add(2, 30)
        False
        '''
        if self.find(key) == None:
            self._list.append((key, val))
            return True
        else:
            return False

    def remove(self, key):
        '''Removes the pair with key from the USet and returns it.
        Returns None if no such pair exsits.

        >>> uset = USet()
        >>> uset.add(1, 10)
        True
        >>> uset.add(2, 20)
        True
        >>> uset.remove(1)
        (1, 10)
        >>> uset.remove(10)
        >>>
        '''
        val = self.find(key)
        if val != None:
            self._list.remove(val)
            return val
        else:
            return None        

    def find(self, key):
        '''Returns the pair from the USet that contains key; None if no
        such pair exists.

        >>> uset = USet()
        >>> uset.add(1, 10)
        True
        >>> uset.add(2, 20)
        True
        >>> uset.find(1)
        (1, 10)
        >>> uset.find(10)
        >>> 
        '''
        if (self.size() != 0):
            keyList = self.keys()
            for i in range(0, len(keyList)):
                if key == keyList[i]:
                    return self._list[i]
        return None

    def size(self):
        '''Returns the number of pairs currently in the USet.
        
        >>> uset = USet()
        >>> uset.size()
        0
        >>> uset.add(1, 10)
        True
        >>> uset.add(2, 20)
        True
        >>> uset.size()
        2
        >>> uset.add(2, 30)
        False
        >>> uset.size()
        2
        '''
        return len(self._list)

    def keys(self):
        '''Returns a list of keys in the USet.
        
        >>> uset = USet()
        >>> uset.keys()
        []
        >>> uset.add(1, 10)
        True
        >>> uset.add(2, 20)
        True
        >>> uset.keys()
        [1, 2]
        >>> uset.add(2, 30)
        False
        >>> uset.keys()
        [1, 2]
        '''
        keyList = []
        for item in self._list:
            keyList.append(item[0])
        return keyList