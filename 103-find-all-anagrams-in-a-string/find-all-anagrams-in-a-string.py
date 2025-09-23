class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p_counter = Counter(p)
        p_len = len(p)
        l = []

        for i in range(len(s) - p_len + 1):
            if p_counter == Counter(s[i:i+p_len]):
                l.append(i)
        
        return l