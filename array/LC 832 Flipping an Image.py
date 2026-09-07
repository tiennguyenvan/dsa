class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for r in range(n):
            for c in range(n//2):
                c1 = n-1-c
                image[r][c], image[r][c1] = image[r][c1], image[r][c]

        for r in range(n):
            for c in range(n):
                image[r][c] = 0 if image[r][c] == 1 else 1
        return image
