class TrieNode:
    def __init__(self):
        # Stores children nodes and whether node is the end of a word
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        # Insert character by character into trie
        for c in word:
            # if character path does not exist, create it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True
        

    def search(self, word: str, end=True) -> bool:
        cur = self.root
        # Search character by character in trie
        for c in word:
            # if character path does not exist, return False
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isEnd if end else True


    def startsWith(self, prefix: str) -> bool:
        # Same as search, except there is no isEnd condition at final return
        return self.search(prefix, False)