class Node:
    def __init__(self, val, left_child, right_child):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child


class Tree:
    def __init__(self):
        self.root = None

    def addNode(self,root, val):
        if self.root == None:
            self.root = Node(val, None, None)
            return
        if root == None:
            root = Node(val, None, None)
            print("added",val)
        else:
            if (val > root.val):
                self.addNode(root.right_child,val)
            else:
                self.addNode(root.left_child,val)
    def print_tree(self,root):
        if(root == None):
            return
        print(root.val)
        self.print_tree(root.left_child)
        self.print_tree(root.right_child)



def main():
    tree = Tree()
    tree.addNode(tree.root,1)
    tree.addNode(tree.root,2)
    tree.print_tree(tree.root)

if __name__ == "__main__":
    main()