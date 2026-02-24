class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        s_len = len(s)
        dp = [False] * (s_len + 1)
        dp[0] = True

        for i in range(1, s_len + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[s_len]