class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        leng = len(word)

        for i in word:
            if i.isupper():
                count += 1

        if count == leng or count == 0 or (count == 1 and word[0].isupper()):
            return True
        else:
            return False
