class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)

        if s_len < p_len:
            return []

        freq_p, freq_s = [0] * 26, [0] * 26

        for i in range(p_len):
            freq_s[ord(s[i]) - ord('a')] += 1
            freq_p[ord(p[i]) - ord('a')] += 1

        ans = []
        if freq_p == freq_s:
            ans.append(0)

        for i in range(p_len, s_len):
            freq_s[ord(s[i - p_len]) - ord('a')] -= 1
            freq_s[ord(s[i]) - ord('a')] += 1

            if freq_p == freq_s:
                ans.append(i - p_len + 1)

        return ans