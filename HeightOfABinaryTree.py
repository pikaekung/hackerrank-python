from turtle import right


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

max_level = 0
level = 0


def pretaversal(root):
    print(root.info)
    if root.left:
        pretaversal(root.left)
    if root.right:
        pretaversal(root.right)


def height(root):
    global level
    print(root.info, level)
    if not root.left and not root.right:
        level -= 2
        print("Highest Level => ", level)

    if root.left:
        level += 1
        height(root.left)

    if root.right:
        level += 1
        height(root.right)

    return level


tree = BinarySearchTree()
t = 6
arr = list(map(int, "4 1 8 10 9 3".split()))

for i in range(t):
    tree.create(arr[i])

height(tree.root)
# pretaversal(tree.root)
