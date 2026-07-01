from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        rowSet, colSet, squareSet
        '''

        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        square = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in rowSet[r]:
                    return False

                elif board[r][c] in colSet[c]:
                    return False

                elif board[r][c] in square[(r//3, c//3)]:
                    return False

                elif board[r][c] == ".":
                    continue

                else:
                    rowSet[r].add(board[r][c])
                    colSet[c].add(board[r][c])
                    square[(r//3, c//3)].add(board[r][c])


        return True
        