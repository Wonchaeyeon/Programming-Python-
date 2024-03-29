class TicTacToe:
    def __init__(self):
        self.board = [".",".",".",".",".",".",".",".","."]
        self.current_turn="O"

    def set(self,row,col):
        if self.get(row,col)==".": #빈칸일때만
            # if self.current_turn == "O":
            #     self.current_turn = "X"
            # else:
            #     self.current_turn="O"
            self.current_turn="X" if self.current_turn =="O" else "O"  #만약 O면 X를 넣고, O면 그냥 O를 넣어라.
                              #여기 "X"부터 뒤까지가 먼저 해석. (위에 4줄이랑 같은 말임)
            self.board[(row * 3)+col]=self.current_turn
        else:
            print("빈칸이 아니에요, 제대로 잘 입력해요.")
    def get(self,row,col):
        return self.board[(row*3)+col]   #row의 1차원 보드 값 바뀌게 하는것

    def check_winner(self):
        check = self.current_turn
        #-
        for i in range(3):
            if self.get(i,0) == self.get(i,1) ==self.get(i,2)==check:
                return check
        # |
            if self.get(0, i) == self.get(1,i) == self.get(2,i) == check:
                return check
        #\
        if self.get(0,0) == self.get(1,1) ==self.get(2,2) ==check:
            return check
        #/
        if self.get(0,2)==self.get(1,1) ==self.get(2,0) ==check:
            return check
        if not "." in self.board:
            return "d"

    def __str__(self):
        s=""
        for i,ch in enumerate(self.board):  #enumerate는 인덱스와 같이 나온다.
            s += ch
            if i % 3 == 2:
                s+="\n"
        return s
if __name__ == '__main__':
    ttt=TicTacToe()
    print(ttt)
    ttt.set(0,0)
    ttt.set(0,1)
    ttt.set(1,0)
    ttt.set(1,1)
    ttt.set(2,0)
    ttt.set(2,2)
    print(ttt)


