class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        # up, down, right, left
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        seen = set()

        def dfs(row, col):


            # if the row or col are out of bounds of the grid -> return None
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or (row, col) in seen
                or grid[row][col] == "0"
            ):
                return None

            seen.add((row, col))

            # recursively traverse for each direction
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in seen:
                    dfs(row, col)
                    islands += 1
        return islands
