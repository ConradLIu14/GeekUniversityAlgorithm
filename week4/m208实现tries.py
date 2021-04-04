class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_end = '#'
        self.root = dict()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in word:
            if i in node:
                node = node[i]
            else:
                node[i] = dict()
                node = node[i]
        node[self.is_end] = self.is_end

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in word:
            if i not in node:
                return False
            node = node[i]
        return self.is_end in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in prefix:
            if i not in node:
                return False
            node = node[i]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)