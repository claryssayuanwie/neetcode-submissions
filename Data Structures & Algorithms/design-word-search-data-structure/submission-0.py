class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.endOfWord
            c = word[i]
            if c != '.':
                if c not in node.children:
                    return False # does not exist even as a char
                return dfs(node.children[c], i + 1)
            else:
                for child in node.children.values(): # dict!
                    if dfs(child, i + 1): # if child++ doesnt break the code, then word is valid
                        return True
                return False
        return dfs(self.root, 0)