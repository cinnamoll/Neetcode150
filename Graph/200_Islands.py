class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.pop()
                dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for x,y in dir:
                    r_now = row + x
                    c_now = col + y
                    if (r_now in range(rows) and c_now in range(cols) 
                        and grid[r_now][c_now] == "1" and (r_now, c_now) not in visit):
                        q.append((r_now, c_now))
                        visit.add((r_now, c_now))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands