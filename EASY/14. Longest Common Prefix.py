from typing import List


class Node:
    def __init__(self):
        self.node = {}
        self.eow = False
        self.n = 0

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, words):
        for word in words:
            if word == "":
                return False
            current = self.root

            for char in word:
                if char not in current.node:
                    current.node[char] = Node()
                current.n = current.n + 1
                current = current.node[char]
            current.eow = True
        return True

    def search_longest_prefix(self):
        current = self.root

        output = ""
        flag = True
        while flag:
            keys = list(current.node.keys())
            if len(keys) != 1:
                flag = False 
            else:
                key = keys[0]
                if current.n != current.node[key].n:
                    flag = False
                output = output + key
                current = current.node[key]
                    

        return output

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie_instance = Trie()
        insert = trie_instance.insert(strs)
        if not insert:
            return ""
        return trie_instance.search_longest_prefix()

    
                    
        
instance = Solution()
call = instance.longestCommonPrefix(["flower","flow","flight"])
# call = instance.longestCommonPrefix(["WORD", "WORDS", "WORDZ", "WORDX"])
# call = instance.longestCommonPrefix([""])
# call = instance.longestCommonPrefix(["", "a"])
# call = instance.longestCommonPrefix(["ab", "a"])

print(call)
