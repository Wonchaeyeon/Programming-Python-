from tictactoe import TicTacToe

class GameManager:
    def __init__(self):
        self.ttt=TicTacToe()

    def play(self):
        #show_board()
        print(self.ttt)
        #반복하자
        while True:
            # 위치를 입력받자
            row = int(input("row: "))
            col = int(input("col: "))
            # 말을 놓자
            self.ttt.set(row,col)
            print(self.ttt)
             # check_winner()
            # 결과 출력하자
            if self.ttt.check_winner() == "O":
                print("O 승리 , ㅊㅋㅊㅋ")
                break
            elif self.ttt.check_winner() == "X":
                print("X 승리 , ㅊㅋㅊㅋ")
                break
            elif self.ttt.check_winner() == "d":
                print("무승부")
                break

if __name__ == '__main__':
   gm= GameManager()
   gm.play()