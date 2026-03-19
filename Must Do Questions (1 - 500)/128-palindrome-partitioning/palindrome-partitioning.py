class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions, lst, l = [], [([], 0)], len(s)

        while lst:
            pals, i = lst.pop()
            for j in range(i + 1, l + 1):
                sub = s[i:j]
                if sub == sub[::-1]:
                    if j == l:
                        partitions.append(pals + [sub])
                    else:
                        lst.append((pals + [sub], j))
                        
        return partitions