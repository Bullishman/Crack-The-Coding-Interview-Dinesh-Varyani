class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, mx = 0, 0

        for r, c in enumerate(s):
            if c in seen:
                l = max(l, seen[c] + 1)
            seen[c] = r
            mx = max(mx, r - l + 1)

        return mx