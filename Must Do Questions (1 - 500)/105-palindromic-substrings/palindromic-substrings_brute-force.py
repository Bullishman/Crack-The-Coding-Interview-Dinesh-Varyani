class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j + 1]
                if substring == substring[::-1]:
                    result += 1

        return result