class Solution:
    '''DFS solution'''
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        # up, down, right, left
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        seen = set()

        def dfs(row, col):
            # if the row or col are out of bounds of the grid
            # the curr node is 0 (not land)
            # the curr node was already seen -> return None
            if (
                row not in range(ROWS)
                or col not in range(COLS)
                or (row, col) in seen
                or grid[row][col] == "0"
            ):
                return None

            # mark the curr node as visited
            seen.add((row, col))

            # recursively traverse for each direction
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        for row in range(ROWS):
            for col in range(COLS):
                # for each node -> we iterate 
                # we check if the the node is land and if we have "seen" it
                # when we call DFS, it will mark all adjacent land as "seen" before we hit 
                # the next node -> hence `not in seen` = new island
                if grid[row][col] == "1" and (row, col) not in seen:
                    # new ialand found -> call DFS to explore other islands + inc islands
                    dfs(row, col)
                    islands += 1
        return islands
