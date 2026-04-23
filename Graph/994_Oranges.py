class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        countFresh, res = 0, 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    countFresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        dir = [[0,1], [1,0], [-1,0], [0,-1]]
        while q and countFresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for x, y in dir:
                    r_now = r + x
                    c_now = c + y
                    if (r_now >= 0 and r_now < rows and
                        c_now >= 0 and c_now < cols and
                        grid[r_now][c_now] == 1):
                        grid[r_now][c_now] = 2
                        q.append([r_now, c_now])
                        countFresh -= 1
            res+=1
        return res if countFresh == 0 else -1
                