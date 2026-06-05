class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for i in range(9):
            for j in range(9):

                curr = board[i][j]

                if curr == ".":
                    continue
                
                if (curr in rows[i]) or (curr in cols[j]) or (curr in squares[(i//3, j//3)]):
                    return False

                rows[i].append(curr)
                cols[j].append(curr)
                squares[(i//3, j//3)].append(curr)
                

        return True
                
                


        