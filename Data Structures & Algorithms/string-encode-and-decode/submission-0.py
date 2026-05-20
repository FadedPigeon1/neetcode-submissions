class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for i in strs:
            sizes.append(len(i))
        for j in sizes:
            res += str(j)
            res += ','
        res += '#'
        for i in strs:
            res += i
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for j in sizes:
            res.append(s[i:i+j])
            i += j
        return res

