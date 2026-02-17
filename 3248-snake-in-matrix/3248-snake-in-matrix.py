class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        grid = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                grid[i][j] = (i * n) + j
        m=0
        l=0
        for k in commands:
            if k=="DOWN":
                m+=1
            if k=="RIGHT":
                l+=1
            if k=="UP":
                m-=1
            if k=="LEFT":
                l-=1
        return(grid[m][l])