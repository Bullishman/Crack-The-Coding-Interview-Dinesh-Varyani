class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        row_len, col_len = len(board), len(board[0])

        if len(word) > row_len * col_len:
            return False

        char_counter = Counter(chain.from_iterable(board))
        for char, char_count in Counter(word).items():
            if char_counter[char] < char_count:
                return False

        if char_counter[word[0]] > char_counter[word[-1]]:
            word = word[::-1]

        visited = set()
        def find_word(x, y, i):
            if len(word) == i:
                return True
            if x < 0 or y < 0 or x >= row_len or y >= col_len or word[i] != board[x][y] or (x, y) in visited:
                return False

            visited.add((x, y))
            result = (find_word(x - 1, y, i + 1) or find_word(x + 1, y, i + 1) or find_word(x, y - 1, i + 1) or find_word(x, y + 1, i + 1))
            visited.remove((x, y))

            return result

        for x in range(row_len):
            for y in range(col_len):
                if find_word(x, y, 0):
                    return True

        return False