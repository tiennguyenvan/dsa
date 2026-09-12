class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        if not m:
            return image
        n = len(image[0])
        if sr < 0 or sr >= m or sc < 0 or sc >= n:
            return image

        q = deque()
        DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        s_color = image[sr][sc]
        q.append([sr, sc])
        image[sr][sc] = color

        while q:
            r, c = q.popleft()

            for dx, dy in DIRS:
                x, y = r+dx, c+dy
                if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != s_color or image[x][y] == color:
                    continue
                q.append((x, y))
                image[x][y] = color
        return image
