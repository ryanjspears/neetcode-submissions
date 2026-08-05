class Node:
    def __init__(self, val):
        self.val = val
        self.nodes = {} #map of nodes
        self.endWord = False

    def getNextNode(self, val):
        if self.nodes.get(val) is None:
            return None
        
        return self.nodes[val]

    def addNode(self, node):
        self.nodes[node.val] = node

    def isLeaf(self):
        return len(self.nodes) == 0
        

class PrefixTree:

    def __init__(self):
        self.root = Node("-")
        

    def insert(self, word: str) -> None:
        p = self.root
        for letter in word:
            tmp =  p.getNextNode(letter)
            if tmp is None:
                tmp = Node(letter)
                p.addNode(tmp)

            p = tmp

        p.endWord = True


    def search(self, word: str) -> bool:
        p = self.root
        for letter in word:
            tmp =  p.getNextNode(letter)
            if tmp is None:
                return False

            p = tmp

        return p.endWord
        
    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for letter in prefix:
            tmp =  p.getNextNode(letter)
            if tmp is None:
                return False

            p = tmp

        return True