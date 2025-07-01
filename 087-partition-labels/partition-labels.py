class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_map = {char: idx for idx, char in enumerate(s)}

        res = []
        prev = -1
        max_idx = 0

        for idx, char in enumerate(s):
            max_idx = max(max_idx, char_map[char])
            if max_idx == idx:
                res.append(max_idx - prev)
                prev = max_idx
        
        return res