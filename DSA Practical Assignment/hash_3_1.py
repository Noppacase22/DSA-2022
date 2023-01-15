import time
from hash_1 import HashTable
        
# Function that reads 'words_alpha.txt' and inserts them to the given HashTable H.
def readAlpha(hashTable):
    with open("words_alpha.txt", "r", encoding="utf-8") as file:
        for line in file:   
            line = line[:-1]    # Reading every line and removing newline character
            hashTable.insert(line)      # and inserting it to HashTable
        file.close()
    return None                 # Since HashTable H is a python list we don't have to return it.


# Function that reads 'kaikkisanat.txt' and counts and returns the amount of matching words
def readSanat(hashTable):
    with open("kaikkisanat.txt", "r", encoding="utf-8") as file:
        counter = 0                                 # Running sum of matching words
        for line in file:                               # For every word in the file
            counter += hashTable.search(line[:-1])      # Sum up the results of searching for words - HashTable.search() returns 1 if found, 0 otherwise
        file.close()
    return counter

# Main code block if running this file.
if __name__ == "__main__":
    tableSize = 10000
    start = time.time()
    hashTable = HashTable(tableSize)    #Initializing the HashTable. This is laughably fast in python.
    mid1 = time.time()
    print(f"Initializing the Hashtable: {round(mid1-start,4)}s")

    readAlpha(hashTable)            # Reading english words and adding them to the HashTable.
    mid2 = time.time()    
    print(f"Adding the words: {round(mid2-mid1,4)}s")
    
    count = readSanat(hashTable)    # This gives the amount of matching words.
    end = time.time()
    print(f"Finding common words: {round(end-mid2,4)}s")    # ~1s for me
    print(f"Total run time: {round(end-start,4)}s")         # This is ~3s on my end.
    print(f"Total matching words found: {count}")           # Should be 1250
    

    # Change to True to print statistics and table of collision distribution.
    # Keep false for checking base functionality.

    debug = False
    debug = True 
    if not debug:
        exit()
    print()

    # Creating a list of HashTable to get a better view of distribution.
    # a[i] represents how many LinkedLists of size i exist within the HashTable.
    # We use max size 100 here for convenience. In case of index errror we have too many hashes resulting in same value.
    # In other words, Index error means the code(hash function) is not optimized enough.
    MAX_SIZE = 100
    list = [0]*MAX_SIZE          
    for i in range(tableSize):  # Iterating every slot of HashTable
        if hashTable.table[i] == None: l = 0    # If we get None there are unused hash values, so list size is 0.
        else: l = hashTable.table[i].length()   # Else we get length of the LinkedList
        list[l] = list[l] + 1                 # and use it as index
    
    # Calculating statistics for code optimization
    sum = 0             # Running sum of list values
    first = 0           # First nonzero value
    last = 0            # The last nonzero value

    median = 0          # Where the middle is located
    mode = 0            # Index for the most collisions

    nodeValues = 0      # These two are used to
    usedNodes = 0       # calculate average

    for i in range(MAX_SIZE):
        sum += list[i]*i
        nodeValues += list[i]
        if list[i] != 0:
            usedNodes += 1
            last = i
            if first == 0:
                first = i
        if list[i] > list[mode]:
            mode = i
        if median == 0 and sum >= int(370105/2):
            median = i
    
    print(f"Fewest collisions: {first} on {list[first]} different hashes")      
    print(f"Most collisions: {last} on {list[last]} different hashes")         
    print("Median:", list[median], "nodes with", median, "collisions.")     # 370105/10000 = 37 is average for even distribution
    print("Average per node:", round(nodeValues/usedNodes, 2))          # Ideally we want this as high as possible.
    print("Most common collision count:", mode, "in", list[mode], "nodes.")
    print()
     
    # This is a semi-visual representation of the distribution.
    # You could just as well visualize with graphs, but this is enough for me personally (due to lack of time)
    print("This should've really been a graph...")
    print(list)
    print()
    
