class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def get_binary(word):
            binary=0
            for char in word:
                binary|=(1<<ord(char)-97)
            return binary

        ref=get_binary(allowed)
        count=0
        for word in words:
            cur=get_binary(word)
            if cur| ref==ref:
                count+=1
        return count