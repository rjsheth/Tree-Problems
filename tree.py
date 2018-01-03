class Node:
  def __init__(self,data):
      self.data = data
      self.left = None
      self.right = None
      self.parent = None

class Tree:
    def __init__(self):
        self.root = None
        self.leftnum = 0
        self.rightnum = 0

    def add(tree,new):
        n = Node(new)
        if tree.root == None:
            tree.root = n
        else:
            curr = tree.root
            while(curr != None):
                parent = curr
                if n.data < curr.data:
                    curr = curr.left
                elif n.data > curr.data:
                    curr = curr.right
                else:
                    break
                n.parent = parent
        if n.data < tree.root.data:
            tree.leftnum += 1
        elif n.data > tree.root.data:
            tree.rightnum += 1
        #rebalanceTree()

    def rebalanceTree():
        return

    def printTree(self): # inorder traversal
        curr = self.root
        if curr == None:
            return
        if curr.left != None and curr.right != None:
            (curr.left).printTree()
            print(curr)
            (curr.right).printTree()


t = Tree()
for i in range(1,21):
    print(i)
    t.add(i)

t.printTree()
