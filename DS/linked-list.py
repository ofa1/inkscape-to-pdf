class Node:
    value = None
    nextn = None

    def __init__(self, value):
        self.value = value
    
    def add(self, node):
        self.nextn = node
    
    def remove(self):
        self.nextn = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    start = None
    end = None
    length = 0

    def push(self, value):
        if self.start == None:
            self.start = self.end = Node(value)
        else:
            self.end.add(Node(value))
            self.end = self.end.nextn
        self.length += 1
    
    def pop(self):
        if self.start == None or self.end == None:
            return
        else:
            traverser = self.start
            if traverser.nextn == None:
                self.start = self.end = None
            else:
                while traverser.nextn.nextn != None:
                    traverser = traverser.nextn
                traverser.remove()
                self.end = traverser
    
    def __repr__(self):
        s = "["
        traverser = self.start
        while traverser != None:
            s += str(traverser.value) + " "
            traverser = traverser.nextn
        s += "]"
        return s

list1 = LinkedList()
list1.push(1)
list1.push(2)
print(list1)
list1.pop()
print(list1)
list1.push(3)
print(list1)
list1.pop()
list1.pop()
print(list1)