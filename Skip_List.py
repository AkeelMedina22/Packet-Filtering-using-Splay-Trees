from random import randint, seed

# https://gist.github.com/sachinnair90/3bee2ef7dd3ff0dc5aec44ec40e2d127


class Node:

    def __init__(self, height=16, elem=0, upper=0):

        self.elem = elem
        self.upper = upper
        self.next = [None]*height


class SkipList:

    def __init__(self):

        self.head = Node()
        self.len = 0
        self.maxHeight = 16

    def __len__(self):

        return self.len

    def find(self, elem, update=None):

        if update == None:
            update = self.updateList(elem)

        if len(update) > 0:
            item = update[0]
            while item != None and item.elem <= elem:

                if item.elem <= elem and item.upper >= elem:
                    return True

                item = update[0].next[0]

        return None

    def contains(self, elem, update=None):

        return self.find(elem, update) != None

    def randomHeight(self):

        height = 1

        while randint(1, 2) != 1:
            height += 1

        return height

    def updateList(self, elem):

        update = [None]*self.maxHeight
        x = self.head

        for i in reversed(range(self.maxHeight)):

            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]

            update[i] = x

        return update

    def insert(self, rule, elem):

        lower = int(elem[0])
        upper = int(elem[1])
        _node = Node(self.randomHeight(), lower, upper)

        self.maxHeight = max(self.maxHeight, len(_node.next))

        while len(self.head.next) < len(_node.next):
            self.head.next.append(None)

        update = self.updateList(lower)

        if self.find(lower, update) == None:

            for i in range(len(_node.next)):
                _node.next[i] = update[i].next[i]
                update[i].next[i] = _node

            self.len += 1
