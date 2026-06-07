class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        L = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - L + 1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1

            res = max(res, r - L +1)
        return res