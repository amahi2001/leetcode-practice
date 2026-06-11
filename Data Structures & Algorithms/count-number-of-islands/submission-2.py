class Solution:
    """BFS solution"""
    # lots of overlap with DFS solution (see that before)
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        seen = set()
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def bfs(row, col):
            q = deque([(row, col)])
            while q:
                # pop from the q
                r, c = q.popleft()

                # for each direction, precalc 1 level
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # if adjacent nodes are land -> add them to q and seen
                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in seen
                    ):
                        q.append((nr, nc))
                        seen.add((nr, nc))

        # remains the same
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in seen:
                    bfs(row, col)
                    islands += 1

        return islands
