class Solution:
    def casty(self, word):
        if word == ".":
            return 0
        
        return int(word)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row
        for row in range(0, 9):
            temp = {}
            for i in range(0, 9):
                num = self.casty(board[row][i])
                if num == 0:
                    continue
                if temp.get(num) is None:
                    temp[num] = True
                else:
                    return False;

         


        #rows
        for col in range(0, 9):
            temp = {}
            for i in range(0, 9):
                num = self.casty(board[i][col])
                if num == 0:
                    continue
                if temp.get(num) is None:
                    temp[num] = True
                else:
                    return False;

        #section
        for i in range(0,3):
            for j in range(0, 3):
                temp = {}
                
                for x in range(0,3):
                    for y in range(0, 3):
                        num = self.casty(board[(i * 3)+y][(j * 3)+x])
                        if num == 0:
                            continue
                        if temp.get(num) is None:
                            temp[num] = True
                        else:
                            return False;
        return True