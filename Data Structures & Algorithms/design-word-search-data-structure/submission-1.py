class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode() 

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str, node=None, i=0) -> bool:
        word = word[i:]
        if not node:
            node = self.root
        for index, char in enumerate(word):
            if char == '.':
                for another_char in node.children:
                    if self.search(word, node.children[another_char], index + 1):
                        return True
                return False
            elif char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
