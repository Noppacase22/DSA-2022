class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = Node(None, None, None)

    def insert(self, key: int):
        node = self.root
        new = Node(key, None, None)
        if node.key == None:
            self.root = new
            return
        while key != node.key:
            if key > node.key:
                if node.right != None:
                    node = node.right
                else:
                    node.right = new
                    return
            else:
                if node.left != None:
                    node = node.left
                else:
                    node.left = new
                    return
    
    def search(self, key: int):
        node = self.root
        while node.key != key:
            if key > node.key:
                if node.right == None:
                    return False
                else:
                    node = node.right
            elif node.left == None:
                return False
            else:
                node = node.left
        return True

    def order(self, node):
        if node == None:
            return ""
        elif node.key == None:
            return ""
        else:
            return (f"{node.key} {self.order(node.left)} {self.order(node.right)}")

    def preorder(self):
        jono = self.order(self.root)
        print(" ".join(jono.split()))
        return

    def remove(self, key:int):
        node = self.root
        while node.key != key:
            if node.key == None:
                return
            if key > node.key:
                if node.right == None:
                    return
                node = node.right
            else:
                if node.left == None:
                    return
                node = node.left
        
        if node.right == None and node.left == None:
            node.key = None
            return
        elif node.right == None or node.left == None:
            if node.right == None:
                new = node.left
            else:
                new = node.right
            node.key = new.key
            node.left = new.left
            node.right = new.right
        else:
            next = node.right
            while next.left != None:
                if next.left.key == None:
                    break
                next = next.left
            
            if next.right != None:
                next.key = next.right.Key
                next.right = next.right.right
                next.left = next.right.left
            else:
                next.key = None
            node.key = next.key

            
        
if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 4, 6, 2]
    for key in keys:
        Tree.insert(key)

    Tree.preorder()     # 5 1 3 2 4 9 7 6 
    Tree.remove(1)
    Tree.preorder()     # 5 3 2 4 9 7 6 
    Tree.remove(9)
    Tree.preorder()     # 5 3 2 4 7 6
    Tree.remove(3)
    Tree.preorder()     # 5 2 4 7 6
