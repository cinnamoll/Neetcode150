class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            visit.add((r, c))
            area = 1
            while q:
                row, col = q.popleft()
                dir = [[1,0], [0,1], [-1,0], [0,-1]]
                for x,y in dir:
                    r_now = row + x
                    c_now = col + y
                    if (r_now in range(rows) and c_now in range(cols) 
                        and grid[r_now][c_now] == 1 and (r_now, c_now) not in visit):
                        q.append((r_now,c_now))
                        visit.add((r_now,c_now))
                        area += 1
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    temp = bfs(r,c)
                    res = max(res, temp)

        return res