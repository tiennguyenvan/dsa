class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        notSurround = set()
        ROWS = len(board)
        if not ROWS:
            return
        COLS = len(board[0])
        q = deque()
        DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for row in range(ROWS):
            for col in range(COLS):
                if (row not in [0, ROWS-1]) and (col not in [0, COLS-1]):
                    continue
                if board[row][col] != 'O':
                    continue
                if (row, col) in notSurround:
                    continue
                q.append([row, col])
                while q:
                    r, c = q.popleft()
                    if (r, c) in notSurround:
                        continue
                    notSurround.add((r, c))
                    for dx, dy in DIRS:
                        x, y = r + dx, c + dy
                        if x < 0 or x >= ROWS or y < 0 or y >= COLS or board[x][y] != 'O':
                            continue
                        if (x, y) in notSurround:
                            continue
                        q.append([x, y])

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in notSurround:
                    continue
                board[row][col] = 'X'
