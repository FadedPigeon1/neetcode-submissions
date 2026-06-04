class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        L = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[L])
                L+=1
            charSet.add(s[r])
            res = max(res, r - L + 1)
        return res
        

