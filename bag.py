from uset import USet

# Adapted from Exercise 1.5 in the book.

class Bag:
    def __init__(self):
        '''Initializes member variables.

        >>> bag = Bag()
        '''
        self.uset = USet()  # this is the underlying data structure.

    def __str__(self):
        '''Returns a string representation of an object for printing.

        >>> bag = Bag()
        >>> print(bag)  # prints bag.__str__()
        '''
        return str(self.uset)

    def add(self, key, val):
        '''Adds the pair (key, val) to the Bag.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.size()
        1
        >>> bag.add(1, 10)
        >>> bag.size()
        2
        >>> bag.add(1, 20)
        >>> bag.size()
        3
        >>> bag.add(2, 20)
        >>> bag.size()
        4
        '''
        if self.uset.find(key) == None:
            val_list = [val];
            self.uset.add(key, val_list)
        else:
            val_list = self.uset.remove(key)[1]
            val_list.append(val)
            self.uset.add(key, val_list)

    def remove(self, key):
        '''Removes a pair with key from the Bag and returns it.
        Returns None if no such pair exsits.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> bag.remove(1)
        (1,10)  # could be any of the 3 pairs with key == 1.
        >>> bag.remove(2)
        (2,20)
        >>> bag.remove(20)
        >>>
        '''
        checkItem = self.uset.find(key)
        if (checkItem == None):
            return None
        else:
            val_list = self.uset.remove(key)[1]     
            val = val_list.pop(0)
            if (len(val_list) != 0):
                self.uset.add(key, val_list)
            return (key, val)

    def find(self, key):
        '''Returns a pair from the Bag that contains key; None if no
        such pair exists.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> bag.find(1)
        (1,10)  # could be any of the 3 pairs with key == 1.
        >>> bag.find(2)
        (2,20)
        >>> bag.find(20)
        >>>
        '''
        checkItem = self.uset.find(key)
        if (checkItem == None):
            return None
        else:
            return (key, checkItem[1][0])

    def find_all(self, key):
         checkItem = self.uset.find(key)
         if (checkItem == None):
             return []
         else:
             key_val_list = []
             for val in checkItem[1]:
                 key_val_list.append((key, val))
             return key_val_list    



    def size(self):
        '''Returns the number of pairs currently in the Bag.
        
        >>> bag = Bag()
        >>> bag.size()
        0
        >>> bag.add(1, 10)
        >>> bag.add(2, 20)
        >>> bag.size()
        2
        >>> bag.add(2, 30)
        >>> bag.size()
        3
        '''
        size = 0
        for key in self.keys():
            size += len(self.uset.find(key)[1])
        return size


    def keys(self):
        '''Returns a list of keys in the Bag.

        >>> bag = Bag()
        >>> bag.add(1, 10)
        >>> bag.add(1, 10)
        >>> bag.add(1, 20)
        >>> bag.add(2, 20)
        >>> sorted(bag.keys())
        [1, 2]
        '''
        return self.uset.keys()