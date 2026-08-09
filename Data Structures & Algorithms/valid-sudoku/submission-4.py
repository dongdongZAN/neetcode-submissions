class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # subBoxSet = [set() for _ in range(9)]
        # for i in range(9):
        #     rowSet = set()
        #     columnSet = set()

        #     for j in range(9):
        #         # 检查第 i 行
        #         if board[i][j] != ".":
        #             if board[i][j] in rowSet:
        #                 return False
        #             rowSet.add(board[i][j])

        #             box_index = (i // 3) * 3 + (j // 3)
        #             if board[i][j] in subBoxSet[box_index]:
        #                 return False
        #             subBoxSet[box_index].add(board[i][j])

        #         # 检查第 i 列
        #         if board[j][i] != ".":
        #             if board[j][i] in columnSet:
        #                 return False
        #             columnSet.add(board[j][i])

        # return True

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if ((board[r][c] in rows[r]) or (board[r][c] in cols[c]) or (board[r][c] in squares[(r // 3, c // 3)])):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        
        return True



