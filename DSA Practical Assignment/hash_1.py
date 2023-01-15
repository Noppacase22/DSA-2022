import linked   #Linked structure from earlier week, modified.

TABLESIZE = 10000

class HashTable:
    def __init__(self, tableSize):
        self.size = tableSize
        self.table = [None]*tableSize

    # Hashing method
    def hash(self, key):               
        key = str(key)  # Making sure key is string
        sum = 0
        for i in range(len(key)):   # Iterating every sumbol in the given word
            char = ord(key[i])      # Take the ascii code of the current symbol
            sum += char**2          # Adding ascii squared to the sum
        return sum % self.size          # Returning

    # Insert method
    def insert(self, key):
        i = self.hash(key)
        if self.table[i] == None:   #Initialize a new LinkedList if hash hasn't been seen before,
            LList = linked.LinkedList()
        else:
            LList = self.table[i]   # else use the existing one
        LList.insert(key, 0)        # Inserting to the head of the linked list, instead of the end
        self.table[i] = LList
        return None
    
    # Delete method
    def delete(self, key):
        i = self.hash(key)
        if self.table[i] == None:   # If there's nothing to delete we can return.
            return None
        LList = self.table[i]
        deleteIndex = LList.index(key)  # Getting the index of key in LinkedList.
        if deleteIndex == -1: return None   # -1 means key is not there, return.
        LList.delete(deleteIndex)
        self.table[i] = LList
        return None

    # Search method
    def search(self, key):
        i = self.hash(key)
        if self.table[i] == None:   # If there's no LinkedList in hash destination, return 0
            return 0
        LList = self.table[i]
        iCheck = LList.index(key)   # Check the index of key.
        if iCheck == -1:            # -1 means not found, return 0
            return 0
        else:
            return 1                # Index found, return 1. Could've returned boolean values.