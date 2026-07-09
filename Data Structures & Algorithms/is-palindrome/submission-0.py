class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=[]
        for i in range(len(s)):
            if s[i]!=' ' and s[i].isalnum():
                word.append(s[i].lower())
        print
        return word==word[::-1]