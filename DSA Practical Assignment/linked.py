class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.len = 0

    def append(self, data):         # Add data node to the end of the current list
        new = Node(data, None)
        node = self.head
        while node.next != None:
            node = node.next
        node.next = new
        self.len += 1
    
    def insertOrder(self, data):    # Unused, makes ordered LinkedLists
        node = self.head
        while node.next != None:
            if node.next.data > data:
                break
            node = node.next
        new = Node(data, node.next)
        node.next = new
        self.len += 1

    def print(self):                # Prints data values in a given LinkedList with an arrow inbetween 
        if self.head.next == None:
            print ("None")
            return
        string = ""
        node = self.head
        while node.next.next != None:
            node = node.next
            string += str(node.data) + " -> "
        string += str(node.next.data)
        print(string)
    
    def insert(self, data, index):  # Inserts data node to given index
        node = self.head
        for i in range(index):
            node = node.next
        node.next = Node(data, node.next)
        self.len += 1
    
    def index(self, data):      # Searches LinkedList and returns index of desired data node, or -1 if not found
        node = self.head
        i = 0
        while node.next != None:
            node = node.next
            if node.data == data:
                return i
            else: i += 1
        return -1
    
    def delete(self, index):    # Removes node with index, or none if out of range
        if index >= self.len:   
            return
        node = self.head
        for i in range(index):
            node = node.next
        node.next = node.next.next
        self.len -= 1

    def length(self):       # Returns amount of nodes in LinkedList
        return self.len

if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.print()           # 1 -> 3
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()           # 15 -> 1 -> 10 -> 3
    print(L.index(1))   # 1
    L.delete(0)
    L.print()           # 1 -> 10 -> 3