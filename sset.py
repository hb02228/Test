import bisect

class SSet:
    def __init__(self):
        '''Initializes member variables.

        >>> sset = SSet()
        '''
        self._list = []

    def __str__(self):
        '''Returns a string representation of an object for printing.

        >>> sset = SSet()
        >>> print(sset)  # prints sset.__str__()
        '''
        return str(self._list)

    def add(self, key, val):
        '''Adds the pair (key, val) to the SSet if no pair with key
        already exists in the SSet, and returns True. Returns False if a
        pair with key already exists in the SSet.

        >>> sset = SSet()
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.add(2, 30)
        False
        '''
        if (len(self._list) == 0):
            self._list.append((key, val))
        else:
            if self.find(key) != None:               
                return False
            else:
                index = 0
                inserted = False
                while (key > self._list[index][0] and not inserted):
                    index += 1
                    if (index == len(self._list)):
                        self._list.append((key, val))
                        inserted = True
                if (not inserted):
                    self._list.insert(index, (key, val))
        return True

    def remove(self, key):
        '''Removes the pair with key from the SSet and returns it.
        Returns None if no such pair exsits.

        >>> sset = SSet()
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.remove(1)
        (1, 10)
        >>> sset.remove(10)
        >>>
        '''
        val = self.find(key)
        if val != None and val[0] == key:
            self._list.remove(val)
            return val
        else:
            return None 

    def find(self, key):
        '''Returns the pair from the SSet that contains key. If no such
        pair exists, returns the pair from the SSet that contains the
        successor of key. Returns None if no such pair exists.

        >>> sset = SSet()
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.find(1)
        (1, 10)
        >>> sset.find(1.5)
        (2, 20)
        >>> sset.find(3)
        >>> 
        '''
        if (self.size() != 0):
            keyList = self.keys()
            index = bisect.bisect_left(keyList, key)
            if index < len(self._list):
                if (self._list[index][0] >= key): 
                    return self._list[index]
        return None

    def size(self):
        '''Returns the number of pairs currently in the SSet.
        
        >>> sset = SSet()
        >>> sset.size()
        0
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.size()
        2
        >>> sset.add(2, 30)
        False
        >>> sset.size()
        2
        '''
        return len(self._list)

    def keys(self):
        '''Returns a list of keys in the SSet.
        
        >>> sset = SSet()
        >>> sset.keys()
        []
        >>> sset.add(1, 10)
        True
        >>> sset.add(2, 20)
        True
        >>> sset.keys()
        [1, 2]
        >>> sset.add(2, 30)
        False
        >>> sset.keys()
        [1, 2]
        '''
        keyList = []
        for item in self._list:
            keyList.append(item[0])
        return keyList