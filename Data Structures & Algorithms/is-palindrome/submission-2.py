import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        i=0
        j=len(s)-1

        s1 = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(s1)
        return (s1==s1[::-1])