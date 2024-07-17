import random


class hex:
    def __init__(self):
        self.lin = ["A", "A", "A", "4", "5", "6", "B", "B", "B"]
        self.p1 = 3
        self.p2 = 3
        self.cplayer = 2
        self.win = 0
        self.mode = 0
        self.boxes = [
            ["A", "A", "A", "B", "5", "6", "7", "B", "B"],
            ["A", "A", "A", "4", "B", "6", "B", "8", "B"],
            ["A", "2", "A", "A", "B", "6", "7", "8", "B"],
            ["1", "A", "A", "B", "A", "6", "7", "8", "B"],
            ["A", "2", "A", "B", "B", "6", "7", "B", "9"],
            ["A", "A", "3", "B", "5", "B", "7", "8", "B"],
            ["1", "A", "A", "4", "A", "B", "B", "8", "9"],
            ["1", "A", "A", "A", "B", "B", "B", "8", "9"],
            ["A", "2", "A", "A", "5", "B", "7", "B", "9"],
            ["A", "A", "3", "B", "B", "A", "7", "8", "B"],
            ["1", "A", "A", "4", "B", "6", "7", "8", "B"],
            ["1", "A", "A", "4", "B", "6", "B", "8", "9"],
            ["A", "2", "A", "B", "5", "6", "7", "8", "B"],
            ["1", "2", "A", "A", "A", "B", "7", "8", "9"],
            ["A", "2", "3", "B", "B", "B", "7", "8", "9"],
            ["1", "A", "3", "A", "B", "B", "7", "8", "9"],
            ["1", "A", "3", "B", "B", "A", "7", "8", "9"],
            ["A", "2", "3", "A", "A", "B", "7", "8", "9"],
            ["1", "2", "A", "B", "A", "A", "7", "8", "9"],
            ["1", "2", "A", "A", "B", "6", "7", "8", "9"],
            ["1", "A", "3", "B", "A", "6", "7", "8", "9"],
            ["1", "A", "3", "4", "A", "B", "7", "8", "9"],
            ["A", "2", "3", "A", "B", "5", "7", "8", "9"],
            ["1", "2", "A", "4", "B", "A", "7", "8", "9"],
        ]

    def display(self):
        print(" ")
        print(self.lin[0:3])
        print(self.lin[3:6])
        print(self.lin[6:9])
        print(" ")
        print("p1(B): " + str(self.p1))
        print("p2(A): " + str(self.p2))

    def mover(self, move, piece, player):
        if player == 1:
            self.lin[move] = "B"
            self.lin[piece] = str(piece + 1)
            if move + 1 <= 3:
                self.win = 1
        elif player == 2:
            self.lin[move] = "A"
            self.lin[piece] = str(piece + 1)
            if move + 1 >= 7:
                self.win = 2

    def play(self, player, piece):
        if player == 1:
            move = self.mchecker(player, piece)

        elif player == 2:
            if self.mode == 1:
                move = self.sinmchecker(player, piece)
            else:
                move = self.mchecker(player, piece)

        if self.p2 == 0:
            self.win = 1
        if self.p1 == 0:
            self.win = 2

        self.display()

    def sel(self):
        if self.cplayer == 1:
            self.cplayer = 2
        elif self.cplayer == 2:
            self.cplayer = 1

    def pchecker(self, player):
        ret = 0
        while ret == 0:
            piece = int(input("input piece"))
            if self.lin[piece - 1] != "B" and player == 1:
                print("that is not ur piece. try again")
            elif self.lin[piece - 1] != "A" and player == 2:
                print("that is not ur piece. try again")
            else:
                if player == 1:
                    if piece in {2, 5, 8}:
                        if (self.lin[piece - 4] in ["A", "B"]) and (
                            self.lin[piece - 5] != "A" and self.lin[piece - 3] != "A"
                        ):
                            print("cannot select move 7")
                        else:
                            ret = 1

                    elif piece in {1, 4, 7}:
                        if (self.lin[piece - 4] in ["A", "B"]) and (
                            self.lin[piece - 3] != "A"
                        ):
                            print("cannot select move es")
                        else:
                            ret = 1
                    elif piece in {3, 6, 9}:
                        if (self.lin[piece - 4] in ["A", "B"]) and (
                            self.lin[piece - 5] != "A"
                        ):
                            print("cannot select movess")
                        else:
                            ret = 1
                elif player == 2:
                    if piece in {2, 5, 8}:
                        if (self.lin[piece + 2] in ["A", "B"]) and (
                            self.lin[piece + 3] != "B" and self.lin[piece + 1] != "B"
                        ):
                            print("cannot select move")
                        else:
                            ret = 1

                    elif piece in {1, 4, 7}:
                        if (self.lin[piece + 2] in ["A", "B"]) and (
                            self.lin[piece + 3] != "B"
                        ):
                            print("cannot select move")
                        else:
                            ret = 1
                    elif piece in {3, 6, 9}:
                        if (self.lin[piece + 2] in ["A", "B"]) and (
                            self.lin[piece + 1] != "B"
                        ):
                            print("cannot select move")
                        else:
                            ret = 1

        return piece

    def sinpchecker(self, player):
        ret = 0
        while ret == 0:
            if player == 2:
                piece = int(random.randint(1, 9))
            else:
                piece = int(input("input piece"))
            if self.lin[piece - 1] != "B" and player == 1:
                print("that is not ur piece. try again")
            elif self.lin[piece - 1] != "A" and player == 2:
                print("that is not ur piece. try again")
            else:
                if player == 2:
                    if piece in {2, 5, 8}:
                        if (self.lin[piece + 2] in ["A", "B"]) and (
                            self.lin[piece + 3] != "B" and self.lin[piece + 1] != "B"
                        ):
                            print("cannot select move")
                        else:
                            ret = 1

                    elif piece in {1, 4, 7}:
                        if (self.lin[piece + 2] in ["A", "B"]) and (
                            self.lin[piece + 3] != "B"
                        ):
                            print("cannot select move")
                        else:
                            ret = 1
                    elif piece in {3, 6, 9}:
                        if (self.lin[piece + 2] in ["A", "B"]) and (
                            self.lin[piece + 1] != "B"
                        ):
                            print("cannot select move")
                        else:
                            ret = 1
                elif player == 1:
                    if piece in {2, 5, 8}:
                        if (self.lin[piece - 4] in ["A", "B"]) and (
                            self.lin[piece - 5] != "B" and self.lin[piece - 3] != "B"
                        ):
                            print("cannot select move")
                        else:
                            ret = 1

                    elif piece in {1, 4, 7}:
                        if (self.lin[piece - 5] in ["A", "B"]) and (
                            self.lin[piece - 5] != "B"
                        ):
                            print("cannot select move")
                        else:
                            ret = 1
                    elif piece in {3, 6, 9}:
                        if (self.lin[piece - 5] in ["A", "B"]) and (
                            self.lin[piece - 3] != "B"
                        ):
                            print("cannot select move")
                        else:
                            ret = 1

        return piece

    def mchecker(self, player, piece):
        ret = 0
        while ret == 0:
            move = int(input("input ur move")) - 1
            if player == 2:
                if (move - piece) >= 2 and (move - piece <= 4):
                    if (
                        (piece == 8 and move == 6)
                        or (piece == 5 and move == 3)
                        or (piece == 2 and move == 0)
                        or (piece == 6 and move == 8)
                        or (piece == 3 and move == 5)
                        or (piece == 0 and move == 2)
                    ):
                        print("incorrect move. try again p")
                    else:
                        if move < piece:
                            print("error")
                        elif ((move - piece) == 2 or (move - piece) == 4) and self.lin[
                            move
                        ] == "B":
                            print("fjjgv")
                            self.mover(move, piece, player)
                            self.p1 = self.p1 - 1
                            ret = 1

                        elif ((move - piece) == 2 or (move - piece) == 4) and self.lin[
                            move
                        ] != "B":
                            print("incorrect move. try again")
                        elif (move - piece) == 3 and self.lin[move] != "B":
                            self.mover(move, piece, player)
                            ret = 1
                        elif (move - piece) == 3 and self.lin[move] == "B":
                            print(
                                "incorrect move. enemy pawn is already there. try again"
                            )
                        elif self.lin[move] == "A":
                            print("incorrect move. ur pawn is already there. try again")

                else:
                    print("incorrect move. try again u")

            elif player == 1:
                if (piece - move) >= 2 and (piece - move) <= 4:
                    if (
                        (piece == 8 and move == 6)
                        or (piece == 5 and move == 3)
                        or (piece == 2 and move == 0)
                        or (piece == 6 and move == 8)
                        or (piece == 3 and move == 5)
                        or (piece == 0 and move == 2)
                    ):
                        print("incorrect move. try again c")
                    else:

                        if move > piece:
                            print("error")
                        elif ((piece - move) == 2 or (piece - move) == 4) and self.lin[
                            move
                        ] == "A":
                            self.mover(move, piece, player)
                            self.p2 = self.p2 - 1
                            ret = 1

                        elif ((piece - move) == 2 or (piece - move) == 4) and self.lin[
                            move
                        ] != "A":
                            print("incorrect move. try again")
                        elif (piece - move) == 3 and self.lin[move] != "A":
                            self.mover(move, piece, player)
                            ret = 1
                        elif (piece - move) == 3 and self.lin[move] == "A":
                            print(
                                "incorrect move. enemy pawn is already there. try again"
                            )
                        elif self.lin[move] == "B":
                            print("incorrect move. ur pawn is already there. try again")

                else:
                    print("incorrect move. try again d")

        return move

    def sinmchecker(self, player, piece):
        ret = 0
        while ret == 0:
            if player == 2:
                move = int(random.randint(1, 9)) - 1
            else:
                move = int(input("input ur move")) - 1

            if player == 2:
                if (move - piece) >= 2 and (move - piece <= 4):
                    if (
                        (piece == 8 and move == 6)
                        or (piece == 5 and move == 3)
                        or (piece == 2 and move == 0)
                        or (piece == 6 and move == 8)
                        or (piece == 3 and move == 5)
                        or (piece == 0 and move == 2)
                    ):
                        print("incorrect move. try again p")
                    else:
                        if move < piece:
                            print("error")
                        elif ((move - piece) == 2 or (move - piece) == 4) and self.lin[
                            move
                        ] == "B":
                            print("fjjgv")
                            self.mover(move, piece, player)
                            self.p1 = self.p1 - 1
                            ret = 1

                        elif ((move - piece) == 2 or (move - piece) == 4) and self.lin[
                            move
                        ] != "B":
                            print("incorrect move. try again")
                        elif (move - piece) == 3 and self.lin[move] != "B":
                            self.mover(move, piece, player)
                            ret = 1
                        elif (move - piece) == 3 and self.lin[move] == "B":
                            print(
                                "incorrect move. enemy pawn is already there. try again"
                            )
                        elif self.lin[move] == "A":
                            print("incorrect move. ur pawn is already there. try again")

                else:
                    print("incorrect move. try again u")

            elif player == 1:
                if (piece - move) >= 2 and (piece - move) <= 4:
                    if (
                        (piece == 8 and move == 6)
                        or (piece == 5 and move == 3)
                        or (piece == 2 and move == 0)
                        or (piece == 6 and move == 8)
                        or (piece == 3 and move == 5)
                        or (piece == 0 and move == 2)
                    ):
                        print("incorrect move. try again c")
                    else:

                        if move > piece:
                            print("error")
                        elif ((piece - move) == 2 or (piece - move) == 4) and self.lin[
                            move
                        ] == "A":
                            self.mover(move, piece, player)
                            self.p2 = self.p2 - 1
                            ret = 1

                        elif ((piece - move) == 2 or (piece - move) == 4) and self.lin[
                            move
                        ] != "A":
                            print("incorrect move. try again")
                        elif (piece - move) == 3 and self.lin[move] != "A":
                            self.mover(move, piece, player)
                            ret = 1
                        elif (piece - move) == 3 and self.lin[move] == "A":
                            print(
                                "incorrect move. enemy pawn is already there. try again"
                            )
                        elif self.lin[move] == "B":
                            print("incorrect move. ur pawn is already there. try again")

                else:
                    print("incorrect move. try again d")

        return move

    def cdraw(self, player):
        block = ["A", "B"]
        count = 0

        for i in range(3):
            lind = self.lin[slice((0 + i), (7 + i), 3)]
            ldraw = len(block)
            for i in range(len(lind) - ldraw + 1):
                if lind[i : i + ldraw] == block:
                    count += 1
            print("done  " + str(count))
            if self.p1 == count and self.p2 == count:
                self.win = player

    def double(self):
        while self.win == 0:
            self.display()
            self.sel()
            print("player " + str(self.cplayer) + " turn")

            piece = self.pchecker(self.cplayer)
            self.play(self.cplayer, piece - 1)
            self.cdraw(self.cplayer)

    def single(self):
        while self.win == 0:
            self.display()
            self.sel()
            print("player " + str(self.cplayer) + " turn")

            piece = self.sinpchecker(self.cplayer)
            self.play(self.cplayer, piece - 1)
            self.cdraw(self.cplayer)

    def mirror(self, clist):
        l1 = clist[slice(0, 3, 1)]
        l2 = clist[slice(3, 6, 1)]
        l3 = clist[slice(6, 9, 1)]
        liln = []
        l1.reverse()
        l2.reverse()
        l3.reverse()
        liln = l1 + l2 + l3
        count = 0
        for i in liln:
            if i not in {"A", "B"}:
                liln[count] = 0
            count = count + 1
        cc = 0
        for i in liln:
            if i not in {"A", "B"}:
                liln[cc] = str(cc + 1)
            cc = cc + 1
        return liln

    def aiplay(self):
        count = 0
        match = 10
        while match == 10:
            for i in self.boxes:
                if i == self.lin:
                    match = count
            if match == 10:
                nlin = self.mirror(self.lin)
                self.lin = nlin
        return match

    def start(self):
        print("welcome! input 1 for single player, 2 for double player: ")
        pl = int(input(" "))
        while pl < 1 or pl > 2:
            pl = int(input("incorrect. try again"))

        if pl == 1:
            self.mode = 1
            self.single()
        elif pl == 2:
            self.mode = 2
            self.double()

        print("player " + str(self.win) + " wins")


hexa = hex()
hexa.start()
