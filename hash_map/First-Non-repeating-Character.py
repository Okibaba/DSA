class Solution:
    def firstUniqChar(self, input_word: str) -> int:
        word={}

        for letter in input_word:
            if letter in word:
                word[letter] +=1
            else: 
                word[letter]=1

        for index,key in enumerate(word):
            if word[key]==1:
                return index

        
        return -1


if __name__== "__main__":
    sol=Solution()
    print(sol.firstUniqChar("apple"))