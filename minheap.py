
class MinHeap:
    def __init__(self):
        self.list = []
        self.len = 0
    
    def minimizer(self, array, index):
        while index > 0:
            iParent = int((index-1)/2)
            number = array[index]
            parentNumber = array[iParent]
            if number < parentNumber:
                array[index] = parentNumber
                array[iParent] = number
            index = iParent
        return array

    def push(self, key):
        self.len += 1
        array = self.list
        array.append(key)
        self.list = self.minimizer(array, self.len-1)
        return

    def maximize(self, array):
        index = 0
        len = self.len
        while index < len:
            number = array[index]
            iLeft = 2*index + 1
            iRight = 2*index + 2
            if iRight >= len:
                return array
            left = array[iLeft]
            if iLeft == len:
                if number > left:
                    array[iLeft] = number
                    array[index] = left
                return array
            right = array[iRight]
            if number <= left and number <= right:
                return array
            if number <= left or left > right:
                array[index] = right
                array[iRight] = number
                index = iRight
            else:
                array[index] = left
                array[iLeft] = number
                index = iLeft
        return array
    
    def pop(self):
        if self.len == 0: return "None"
        array = self.list
        root = array[0]
        self.len -= 1
        array[0] = array.pop(self.len)
        self.list = self.maximize(array)
        return root

    def print(self):
        for key in self.list:
            print(key, end = " ")
        print()
        return


if __name__ == "__main__":
    print("CG test 3:")
    keys = "9 37 5 17 8 32 29 31 42 25 14 7 45 2 41 28 1 44 18 24 26 46 19 4 11 34 36 43 21 38 23 13 39 40 20 50 27 35 33 12 15 47 6 49 30"
    heap = MinHeap()
    for key in keys.split(" "):
        heap.push(int(key))
    heap.print()
    for i in range(22):
        heap.pop()
    heap.print()
    print("27 28 29 31 30 32 36 37 33 39 40 35 34 43 38 46 49 44 42 50 41 45 47   Expected") 
    print()
    print("Standard test 1")
    items = [4, 8, 6, 5, 1, 2, 3]
    heap = MinHeap()
    for key in items:
        heap.push(key)
    heap.print()        # 1 4 2 8 5 6 3 
    print(heap.pop())   # 1
    heap.print()        # 2 4 3 8 5 6 
    print()
    print("CG test 1:")
    items = [4, 5, 2, 6, 10, 7]
    newHeap = MinHeap()
    for key in items:
        newHeap.push(key)
    newHeap.print()
    newHeap.pop()
    newHeap.print()
    newHeap.pop()
    newHeap.print()
    newHeap.pop()
    newHeap.print()