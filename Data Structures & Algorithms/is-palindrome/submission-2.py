class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = []
        for i in s.lower():
            if i.isalnum():
                result.append(i)
        return result[::-1] == result