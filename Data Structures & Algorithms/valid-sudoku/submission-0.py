class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        for x in range(9):
            for y in range(9):
                sq = (y // 3) + ((x // 3))*3
                value = board[x][y]
                if value != ".":
                    if value in rows[x] or value in cols[y] or value in squares[sq]:
                        return False
                    else:
                        rows[x].add(value)
                        cols[y].add(value)
                        squares[sq].add(value)
        return True