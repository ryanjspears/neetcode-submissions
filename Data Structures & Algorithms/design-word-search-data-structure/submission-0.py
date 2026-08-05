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

    def __str__(self):
        return (
            f"Node(val={self.val}, "
            f"children={list(self.nodes.keys())}, "
            f"endWord={self.endWord})"
        )

class WordDictionary:

    def __init__(self):
        self.root = Node("-")
        

    def addWord(self, word: str) -> None:
        p = self.root
        for letter in word:
            tmp =  p.getNextNode(letter)
            if tmp is None:
                tmp = Node(letter)
                p.addNode(tmp)

            p = tmp

        p.endWord = True


    def search(self, word: str) -> bool:
        q = [self.root]


        for letter in word:
            if letter == ".":
                #grab all next node by level
                tmp = []
                while len(q) > 0:
                    node_p = q.pop()
                    #append all next nodes
                    for node in node_p.nodes.values():
                        tmp.append(node)

                if len(tmp) == 0:
                    return False
                
                q = tmp
            else:
                print("hit")
                print(q)
                tmp = []
                #for each node get the nodes that are the next letter
                while len(q) > 0:
                    node_p = q.pop()
                    #append next letter node
                    nex = node_p.getNextNode(letter)
                    if nex is not None:
                        tmp.append(nex)

                if len(tmp) == 0:
                    return False

                q = tmp
                print(q)
        
        #search for endWord
        for node in q:
            if node.endWord:
                return True
        
        return False