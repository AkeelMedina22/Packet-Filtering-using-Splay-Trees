class Node:
    def __init__(self, rule, lower, upper):

        self.rulenum = rule
        self.lst = []  # keep filling this every time something new is inserted through in order traversal

        self.parent = None
        self.left = None
        self.right = None

        self.lower = lower
        self.upper = upper


class SplayTree(Node):

    def __init__(self):

        self.root = None
        self.bound_lst = {}

    # rotate left at node x
    def left_rotate(self, x):

        y = x.right
        x.right = y.left

        if y.left != None:
            y.left.parent = x

        y.parent = x.parent

        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    # rotate right at node x
    def right_rotate(self, x):

        y = x.left
        x.left = y.right

        if y.right != None:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == None:  # x is root
            self.root = y
        elif x == x.parent.right:  # x is right child
            x.parent.right = y
        else:  # x is left child
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, n):

        while n.parent != None:  # node is not root

            if n.parent == self.root:  # node is child of root, one rotation

                if n == n.parent.left:
                    self.right_rotate(n.parent)
                else:
                    self.left_rotate(n.parent)
            else:

                a = n.parent
                b = a.parent  # grandparent

                if n.parent.left == n and a.parent.left == a:  # both are left children
                    self.right_rotate(b)
                    self.right_rotate(a)
                elif n.parent.right == n and a.parent.right == a:  # both are right children
                    self.left_rotate(b)
                    self.left_rotate(a)
                elif n.parent.right == n and a.parent.left == a:
                    self.left_rotate(a)
                    self.right_rotate(b)
                elif n.parent.left == n and a.parent.right == a:
                    self.right_rotate(a)
                    self.left_rotate(b)

    def insert(self, rule, bounds):
        lower = int(bounds[0])
        upper = int(bounds[1])
        self.bound_lst[rule] = [int(bounds[0]), int(bounds[1])]

        for _ in range(2):

            if _ == 0:
                node = Node(rule, lower, upper)
            else:
                node = Node(rule, upper, lower)

            y = None
            x = self.root

            while x != None:
                y = x

                if (node.lower < x.lower):
                    x = x.left
                else:
                    x = x.right

            node.parent = y

            if y == None:
                self.root = node
            elif node.lower < y.lower:
                y.left = node
            else:
                y.right = node

            self.splay(node)

    def exists(self, k):

        current = self.root

        while current != None:
            if (current.lower < current.upper):
                if (k > current.lower and k < current.upper):
                    return True

                if k < current.lower:
                    current = current.left

                elif k > current.lower:
                    current = current.right

                elif k == current.lower:
                    return True
            else:

                if (k < current.lower and k > current.upper):
                    return True

                if k < current.lower:
                    current = current.left

                elif k > current.lower:
                    current = current.right

                elif k == current.lower:
                    return True

    def find(self, k):

        accepted = self.exists(k)

        if accepted == True:
            return True

        return None
