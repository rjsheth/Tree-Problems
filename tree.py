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

    def rebalanceTree(self): # rebalancing factor
        curr = self.root
        if self.leftnum + 2 <= self.rightnum: # right heavy
            lowest = curr.right
            curr = curr.right
            while(curr!=None):
                if curr.data < lowest.data:
                    lowest = curr
                curr = curr.left    # since right heavy iterate in the left side
            # make lowest root
            if lowest == self.root.right:
                self.makeImmRoot("right")
                self.rightnum-=1
                self.leftnum+=1
        elif self.leftnum >= self.rightnum + 2: # left heavy
            lowest = curr.left
            curr = curr.left
            while(curr!=None):
                if curr.data < lowest.data:
                    lowest = curr
                curr = curr.right    # since right heavy iterate in the left side
            # make lowest root
            if lowest == self.root.left:
                self.makeImmRoot("left")
                self.rightnum+=1
                self.leftnum-=1
        print("median =",self.root.data)

    def makeImmRoot(self,direction):
        if direction == 'right':
            temp = self.root.right
            self.root.right = None
            self.root.parent = temp
            templeft = temp.left
            temp.left = self.root
            self.root = temp
            self.root.right.left = templeft
        if direction == 'left':
            temp = self.root.left
            self.root.left = None
            self.root.parent = temp
            tempright = temp.right
            temp.right = self.root
            self.root = temp
            self.root.left.right = tempright



    def add(tree,new):
        n = Node(new)
        if tree.root == None:
            tree.root = n
        else:
            curr = tree.root
            parent = curr
            left = False
            # parent = curr
            while(curr != None):
                parent = curr
                if n.data < curr.data:
                    curr = curr.left
                    left = True
                elif n.data > curr.data:
                    curr = curr.right
                    left = False
                else:
                    print("duplicates")
                    return
            n.parent = parent
            if left:
                parent.left = n
                tree.leftnum += 1
            else:
                parent.right = n
                tree.rightnum += 1
        tree.rebalanceTree()

    def printTree(self,curr): # inorder traversal
        if curr == None:
            return
        self.printTree(curr.left)
        print(curr.data)
        self.printTree(curr.right)


t = Tree()
l = list()
for i in range(1,21):
    l.append(i)
    print(l)
    t.add(i)

t.printTree(t.root)

print('\n')

k = Tree()
j = list()
for i in range(1,21):
    j.append((i%7)*-1)
    print(j)
    k.add((i%7)*-1)

k.printTree(k.root)
