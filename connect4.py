

class Game:
    def __init__(self, rows, cols) -> None:
        # validate input
        if not isinstance(rows, int):
            raise TypeError("rows must be an int")
        if not isinstance(cols, int):
            raise TypeError("cols must be an int")
        if rows < 4:
            raise ValueError("rows must be 4 or greater")
        if cols < 4:
            raise ValueError("cols must be 4 or greater")
        
        self.rows = rows
        self.cols = cols
        self.board = [['-'] * cols for _ in range(rows)]
        self.top = [0] * cols
        self.turn = 'X'
        self.complete = None
        self.winner = None
    
    def dropDisc(self, col):
        # validate input
        if self.complete:
            # TODO: Check error type
            print("game is complete")
            return
        if col < 0 or col >= self.cols:
            print(f"col to drop disc must be between 0 and {self.cols}")
            return
        if self.top[col] > self.cols:
            print(f"col {col} is full")
            return

        # place piece
        row = self.rows - self.top[col] - 1
        self.board[row][col] = self.turn
        self.top[col] = self.top[col] + 1
        
        if self.checkForConnection(row, col, self.turn):
            self.winner = self.turn
            self.complete = True
        
        print(f"turn is: {self.turn}")
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def checkForConnection(self, row, col, player):
        # vertical
        count = 1
        
        # go up
        for r in range(row - 1, -1, -1):
            if self.board[r][col] != player:
                break
            count += 1
        
        # go down
        for r in range(row + 1, self.rows):
            if self.board[r][col] != player:
                break
            print(f"At index {row}, {col}, found {self.board[r][col]}")
            count += 1
        
        print(f"count: {count}")
        if count >= 4:
            return True
        
        # horizontal

        # go left
        for c in range(col - 1, -1, -1):
            if self.board[row][c] != player:
                break
            count += 1
        
        # go right
        for c in range(col + 1, self.cols):
            if self.board[row][c] != player:
                break
            count += 1
        
        if count >= 4:
            return True


        # right tilting diagonal
        count = 1
        r, c = row + 1, col - 1
        while (0 <= r < self.rows) and (0 <= c < self.cols) and self.board[r][c] == player:
            count += 1
            r += 1
            c -= 1
            print(f"count is {count} at row {r}, col {c}")
        
        r, c = row - 1, col + 1
        while (0 <= r < self.rows) and (0 <= c < self.cols) and self.board[r][c] == player:
            count += 1
            r -= 1
            c += 1
        
        if count >= 4:
            return True

        # left tilting diagonal
        count = 1
        r, c = row - 1, col - 1
        while (0 <= r < self.rows) and (0 <= c < self.cols) and self.board[r][c] == player:
            count += 1
            r -= 1
            c -= 1
        
        r, c = row + 1, col + 1
        while (0 <= r < self.rows) and (0 <= c < self.cols) and self.board[r][c] == player:
            count += 1
            r += 1
            c += 1
        
        if count >= 4:
            return True

        return False
    
    def __str__(self) -> str:
        res = []
        for r in range(self.rows):
            for c in range(self.cols):
                res.append(self.board[r][c])
                res.append(" ")
            res.append("\n")
        return "".join(res)

        

if __name__ == "__main__":
    game = Game(6,7)
    print(str(game))
    while not game.complete:
        col = int(input(f"Drop disc for player {game.turn}: "))
        game.dropDisc(col)
        print(str(game))
    
    print(f"Player {game.winner} wins!")
