class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(idx, x, y):
            if idx == len(word):
                return True
            if not (0 <= x < len(board) and 0 <= y < len(board[0])) or (board[x][y] != word[idx]):
                return False
            
            temp, board[x][y] = board[x][y], "/"
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if dfs(idx + 1, x + dx, y + dy):
                    return True
            board[x][y] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j):
                    return True
                    
        return False