from hash_1 import HashTable

TABLESIZE = 3


if __name__ == "__main__":
    insertValues = [12, 'hashtable', 1234, 4328989, 'BM40A1500', -12456, 'aaaabbbbcccc']
    findValues = [-12456, 'hashtable', 1235]
    removeValues = ['BM40A1500', 1234, 'aaaabbbbcccc']
    H = HashTable(3)
    print("Adding values:\n")
    for value in insertValues:
        H.insert(value)
        for slot in H.table:
            if slot == None:
                print(None)
                continue
            slot.print()
        print()
    
    print("Finding values:")
    for value in findValues:
        result = H.search(value)
        if result == 0:
            print(f"The value '{value}' was not found within the hash table.")
        else:
            print(f"The value '{value}' was found within the hash table. Hurray!")

    print()
    print("Removing values:")
    for value in removeValues:
        H.delete(value)
        for slot in H.table:
            if slot == None:
                print(None)
                continue
            slot.print()
        print()