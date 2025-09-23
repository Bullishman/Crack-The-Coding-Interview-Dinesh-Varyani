class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            intersection = set(text1) & set(text2)
            if len(intersection) == 0:
                return 0

            lst_t1, lst_t2 = [char for char in text1 if char in intersection], [char for char in text2 if char in intersection]
            dp = [0] * len(lst_t2)

            for i in range(len(lst_t1)):
                cnt = 0
                for j in range(len(lst_t2)):
                    if dp[j] > cnt:
                        cnt = dp[j]
                    elif lst_t1[i] == lst_t2[j]:
                        dp[j] = cnt + 1

            return max(dp)