class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        board_len = len(board)

        for row in range(board_len):
            for col in range(board_len):
                curr = board[row][col]

                if curr == ".":
                    continue
                
                if curr in rows[row]:
                    return False

                if curr in cols[col]:
                    return False
                
                if curr in squares[(row // 3, col // 3)]:
                    return False

                
                cols[col].append(curr)
                rows[row].append(curr)
                squares[(row // 3, col // 3)].append(curr)

        return True
