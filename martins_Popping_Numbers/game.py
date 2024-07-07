import time

from GameBoard import GameBoard
from player import Player
import random
import string


class Game:
    def __init__(self, size, nums):
        self.board = GameBoard(size)
        self.size = size
        self.player = Player()
        self.allowedNums = nums
        self.predictedMoves = []
        self.foundCombos = []
        self.freeSpaces = self.board.allSpaces.copy()

    def run(self):
        self.round()
        self.game_over()

    def round(self):
        if len(self.freeSpaces) <= 4:
            return
        self.gen_pmoves()
        self.board.show_map()
        self.score_bar()
        pm = self.select_cell()
        self.freeSpaces.remove(pm)
        self.commit_pmoves()
        self.check_combos(pm)
        self.commit_combo()
        self.round()

    def game_over(self):
        print("Game Over!")
        print(f"Score achieved: {self.player.show_points()}")
        time.sleep(5)

    def score_bar(self):
        print('---' * 5)
        print('   Score:' + str(self.player.show_points()) + '      ')
        print('---' * 5)

    def check_combos(self, pm):
        cords = self.predictedMoves.copy()
        cords.append(pm)
        self.predictedMoves = []

        for cord in cords:
            x_combo = []
            self.combo(cord, [1, 0], self.board.get(cord[0], cord[1]), x_combo)
            self.combo(cord, [-1, 0], self.board.get(cord[0], cord[1]), x_combo)

            y_combo = []
            self.combo(cord, [0, 1], self.board.get(cord[0], cord[1]), y_combo)
            self.combo(cord, [0, -1], self.board.get(cord[0], cord[1]), y_combo)

            xy_combo = []
            self.combo(cord, [1, 1], self.board.get(cord[0], cord[1]), xy_combo)
            self.combo(cord, [-1, -1], self.board.get(cord[0], cord[1]), xy_combo)

            yx_combo = []
            self.combo(cord, [-1, 1], self.board.get(cord[0], cord[1]), yx_combo)
            self.combo(cord, [1, -1], self.board.get(cord[0], cord[1]), yx_combo)

            if len(x_combo) >= 3: self.foundCombos.append(x_combo)
            if len(y_combo) >= 3: self.foundCombos.append(y_combo)
            if len(xy_combo) >= 3: self.foundCombos.append(xy_combo)
            if len(yx_combo) >= 3: self.foundCombos.append(yx_combo)

    def commit_combo(self):
        for combo in self.foundCombos:
            if len(combo) < 3:
                print(f"Error in combo commiter: {combo}")

            if len(combo) == 3:
                self.player.increase_points(100)
            if len(combo) == 4:
                self.player.increase_points(200)
            if len(combo) == 5:
                self.player.increase_points(500)

            # reset cells
            for cell in combo:
                self.board.set(cell[0], cell[1], ' ')
                self.freeSpaces.append([cell[0], cell[1]])

            self.foundCombos.remove(combo)

    def combo(self, cxy: list, rxy: list, t, output: list):
        if cxy[0] >= self.size or cxy[1] >= self.size or cxy[0] < 0 or cxy[1] < 0:
            return
        if self.board.get(cxy[0], cxy[1]) != t:
            return

        if cxy not in output:
            output.append(cxy)
        ncxy = [cxy[0] + rxy[0], cxy[1] + rxy[1]]

        return self.combo(ncxy, rxy, t, output)

    def gen_pmoves(self):

        for i in range(3):
            xyv = self.rand_coord().copy()
            self.board.set(xyv[0], xyv[1], '*')
            xyv.append(random.choice(self.allowedNums))
            self.predictedMoves.append(xyv)

    def commit_pmoves(self):
        for i in range(len(self.predictedMoves)):
            xyv = self.predictedMoves[i]
            value = xyv[2]

            if self.board.get(xyv[0], xyv[1]) != '*':
                new = self.rand_coord()
                new.append(value)
                self.predictedMoves[i] = new
                xyv = new

            if [xyv[0], xyv[1]] in self.freeSpaces:
                self.freeSpaces.remove([xyv[0], xyv[1]])

            self.board.set(xyv[0], xyv[1], xyv[2])

    def rand_coord(self):
        return random.choice(self.freeSpaces).copy()

    def select_cell(self):
        print("Select number to place!")
        txt = ''
        for num in self.allowedNums:
            txt += '| ' + str(num) + ' |'
        print(txt)
        value = 0
        while True:
            choice = input("Input choice: ")
            if choice.isdigit():
                if int(choice) in self.allowedNums:
                    value = int(choice)
                    break

            print(f"Entered choice [{choice}] is not a valid number. Try Again!")

        print("Select Cell to place number in! format: A0")
        while True:
            choice = input("Input choice: ")
            y = choice[0].lower()
            x = choice[1:]
            if y not in list(string.ascii_lowercase):
                print(f"Invalid location [{choice}]. Try again!")
                continue
            if list(string.ascii_lowercase).index(y) >= self.size:
                print(f"Invalid location [{choice}]. Try again!")
                continue


            yc = list(string.ascii_lowercase).index(y)
            xc = choice[1:]
            if x.isdigit():
                if int(x) < self.size:
                    if self.board.get(int(xc), yc) == ' ' or self.board.get(int(xc), yc) == '*':
                        self.board.set(int(xc), yc, value)
                        return [int(xc), yc]

            print(f"Invalid location [{choice}]. Try again!")
