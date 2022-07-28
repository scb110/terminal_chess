class Piece:
    def __init__(self, piecetype, team, square):
        self.piecetype = piecetype
        self.team = team
        self.square = square

    def set_piece_type(self, piecetype):
        self.piecetype = piecetype

    def get_piece_type(self):
        return self.piecetype

    def set_team(self, team):
        self.team = team

    def get_team(self):
        return self.team

    def set_square(self, square):
        self.square = square

    def get_square(self):
        return self.square


class Game:
    def __init__(self):
        self.reference_board = {

                            18: 'a8', 28: 'b8', 38: 'c8', 48: 'd8', 58: 'e8', 68: 'f8', 78: 'g8', 88: 'h8',
                            17: 'a7', 27: 'b7', 37: 'c7', 47: 'd7', 57: 'e7', 67: 'f7', 77: 'g7', 87: 'h7',
                            16: 'a6', 26: 'b6', 36: 'c6', 46: 'd6', 56: 'e6', 66: 'f6', 76: 'g6', 86: 'h6',
                            15: 'a5', 25: 'b5', 35: 'c5', 45: 'd5', 55: 'e5', 65: 'f5', 75: 'g5', 85: 'h5',
                            14: 'a4', 24: 'b4', 34: 'c4', 44: 'd4', 54: 'e4', 64: 'f4', 74: 'g4', 84: 'h4',
                            13: 'a3', 23: 'b3', 33: 'c3', 43: 'd3', 53: 'e3', 63: 'f3', 73: 'g3', 83: 'h3',
                            12: 'a2', 22: 'b2', 32: 'c2', 42: 'd2', 52: 'e2', 62: 'f2', 72: 'g2', 82: 'h2',
                            11: 'a1', 21: 'b1', 31: 'c1', 41: 'd1', 51: 'e1', 61: 'f1', 71: 'g1', 81: 'h1',

        }
        self.game_board = {
                            'a8': '.', 'b8': '.', 'c8': '.', 'd8': '.', 'e8': '.', 'f8': '.', 'g8': '.', 'h8': '.',
                            'a7': '.', 'b7': '.', 'c7': '.', 'd7': '.', 'e7': '.', 'f7': '.', 'g7': '.', 'h7': '.',
                            'a6': '.', 'b6': '.', 'c6': '.', 'd6': '.', 'e6': '.', 'f6': '.', 'g6': '.', 'h6': '.',
                            'a5': '.', 'b5': '.', 'c5': '.', 'd5': '.', 'e5': '.', 'f5': '.', 'g5': '.', 'h5': '.',
                            'a4': '.', 'b4': '.', 'c4': '.', 'd4': '.', 'e4': '.', 'f4': '.', 'g4': '.', 'h4': '.',
                            'a3': '.', 'b3': '.', 'c3': '.', 'd3': '.', 'e3': '.', 'f3': '.', 'g3': '.', 'h3': '.',
                            'a2': '.', 'b2': '.', 'c2': '.', 'd2': '.', 'e2': '.', 'f2': '.', 'g2': '.', 'h2': '.',
                            'a1': '.', 'b1': '.', 'c1': '.', 'd1': '.', 'e1': '.', 'f1': '.', 'g1': '.', 'h1': '.'
                            }
        self.active_pieces = []

    def get_upper_numeric_limit(self, num):
        string_num_square = str(num)
        tens = string_num_square[0]
        ones_limit = '8'
        edge = int(tens + ones_limit)
        return edge

    def get_bottom_numeric_limit(self, num):
        string_num_square = str(num)
        tens = string_num_square[0]
        ones_limit = '1'
        edge = int(tens + ones_limit)
        return edge

    def get_right_numeric_limit(self, num):
        string_num_square = str(num)
        ones = string_num_square[1]
        tens_right_limit = '8'
        edge = int(tens_right_limit + ones)
        return edge

    def get_left_numeric_limit(self, num):
        string_num_square = str(num)
        ones = string_num_square[1]
        tens_left_limit = '1'
        edge = int(tens_left_limit + ones)
        return edge

    def bishop_queen_up_right_range(self, alphanum):
        moving_piece = self.get_occupant_by_alphanum(alphanum)
        bq_up_right_range = []
        origin = self.get_num_by_alphanum(alphanum)
        current_num = origin + 11
        while self.num_square_on_reference_board_num(current_num):
            square = self.get_alphanum_by_num(current_num)
            occupant = self.game_board[square]
            if occupant == '.':
                bq_up_right_range.append(square)
            elif occupant.get_team() != moving_piece.get_team():
                bq_up_right_range.append(square)
                return bq_up_right_range
            else:
                return bq_up_right_range

            current_num += 11

        return bq_up_right_range

    def bishop_queen_down_left_range(self, alphanum):
        moving_piece = self.get_occupant_by_alphanum(alphanum)
        bq_down_left_range = []
        origin = self.get_num_by_alphanum(alphanum)
        current_num = origin - 11
        while self.num_square_on_reference_board_num(current_num):
            square = self.get_alphanum_by_num(current_num)
            occupant = self.game_board[square]
            if occupant == '.':
                bq_down_left_range.append(square)
            elif occupant.get_team() != moving_piece.get_team():
                bq_down_left_range.append(square)
                return bq_down_left_range
            else:
                return bq_down_left_range

            current_num -= 11

        return bq_down_left_range

    def bishop_queen_up_left_range(self, alphanum):
        moving_piece = self.get_occupant_by_alphanum(alphanum)
        bq_up_left_range = []
        origin = self.get_num_by_alphanum(alphanum)
        current_num = origin - 9
        while self.num_square_on_reference_board_num(current_num):
            square = self.get_alphanum_by_num(current_num)
            occupant = self.game_board[square]
            if occupant == '.':
                bq_up_left_range.append(square)
            elif occupant.get_team() != moving_piece.get_team():
                bq_up_left_range.append(square)
                return bq_up_left_range
            else:
                return bq_up_left_range

            current_num -= 9

        return bq_up_left_range

    def bishop_queen_down_right_range(self, alphanum):
        moving_piece = self.get_occupant_by_alphanum(alphanum)
        bq_down_right_range = []
        origin = self.get_num_by_alphanum(alphanum)
        current_num = origin + 9
        while self.num_square_on_reference_board_num(current_num):
            square = self.get_alphanum_by_num(current_num)
            occupant = self.game_board[square]
            if occupant == '.':
                bq_down_right_range.append(square)
            elif occupant.get_team() != moving_piece.get_team():
                bq_down_right_range.append(square)
                return bq_down_right_range
            else:
                return bq_down_right_range

            current_num += 9

        return bq_down_right_range


    def rook_queen_up_range(self, alphanum):
        moving_piece = self.get_occupant_by_alphanum(alphanum)
        rq_up_range = []
        origin = self.get_num_by_alphanum(alphanum)
        upper_edge = self.get_upper_numeric_limit(origin)
        current_num = origin + 1
        while current_num <= upper_edge and self.num_square_on_reference_board_num(current_num):
            square = self.get_alphanum_by_num(current_num)
            occupant = self.game_board[square]
            if occupant == '.':
                rq_up_range.append(square)
            elif occupant.get_team() != moving_piece.get_team():
                rq_up_range.append(square)
                return rq_up_range
            else:
                return rq_up_range

            current_num += 1

        return rq_up_range

    def rook_queen_down_range(self, alphanum):
        moving_piece = self.get_occupant_by_alphanum(alphanum)
        rq_down_range = []
        origin = self.get_num_by_alphanum(alphanum)
        bottom_edge = self.get_bottom_numeric_limit(origin)
        current_num = origin - 1
        while (current_num >= bottom_edge) and (self.num_square_on_reference_board_num(current_num)):
            square = self.get_alphanum_by_num(current_num)
            occupant = self.game_board[square]
            if occupant == '.':
                rq_down_range.append(square)
            elif occupant.get_team() != moving_piece.get_team():
                rq_down_range.append(square)
                return rq_down_range
            else:
                return rq_down_range

            current_num -= 1

        return rq_down_range

    def rook_queen_right_range(self, alphanum):
        moving_piece = self.get_occupant_by_alphanum(alphanum)
        rq_right_range = []
        origin = self.get_num_by_alphanum(alphanum)
        right_edge = self.get_right_numeric_limit(origin)
        current_num = origin + 10
        while current_num <= right_edge and self.num_square_on_reference_board_num(current_num):
            square = self.get_alphanum_by_num(current_num)
            occupant = self.game_board[square]
            if occupant == '.':
                rq_right_range.append(square)
            elif occupant.get_team() != moving_piece.get_team():
                rq_right_range.append(square)
                return rq_right_range
            else:
                return rq_right_range

            current_num += 10

        return rq_right_range

    def rook_queen_left_range(self, alphanum):
        moving_piece = self.get_occupant_by_alphanum(alphanum)
        rq_left_range = []
        origin = self.get_num_by_alphanum(alphanum)
        left_edge = self.get_left_numeric_limit(origin)
        current_num = origin - 10
        while current_num >= left_edge and self.num_square_on_reference_board_num(current_num):
            square = self.get_alphanum_by_num(current_num)
            occupant = self.game_board[square]
            if occupant == '.':
                rq_left_range.append(square)
            elif occupant.get_team() != moving_piece.get_team():
                rq_left_range.append(square)
                return rq_left_range
            else:
                return rq_left_range

            current_num -= 10

        return rq_left_range

    def knight_range(self, alphanum):
        moving_piece = self.get_occupant_by_alphanum(alphanum)
        n_range = []
        current_num = self.get_num_by_alphanum(alphanum)
        default_octopus_nums = [(current_num+12), (current_num+21), (current_num+19), (current_num + 8),
                                (current_num-12), (current_num-21), (current_num-19), (current_num-8)]

        for option in default_octopus_nums:
            if self.num_square_on_reference_board_num(option):
                if self.get_occupant_by_num(option) == '.':
                    alphanum = self.get_alphanum_by_num(option)
                    n_range.append(alphanum)

                else:
                    destination_occupant = self.get_occupant_by_num(option)
                    if destination_occupant.get_team() != moving_piece.get_team():
                        alphanum = self.get_alphanum_by_num(option)
                        n_range.append(alphanum)

        return n_range

    def square_on_board_alphanum(self, square):
        """determines whether a given square coordinate is on the game_board"""
        for key in self.game_board.keys():
            if key == square:
                return True
        return False

    def num_square_on_reference_board_num(self, num):
        """determines whether a given number is a key on the reference_board"""
        for key in self.reference_board.keys():
            if key == num:
                return True
        return False

    def get_alphanum_by_num(self, num):
        return self.reference_board[num]

    def get_num_by_alphanum(self, alphanum):
        for key in self.reference_board.keys():
            if self.reference_board[key] == alphanum:
                return key

    def get_occupant_by_alphanum(self, square):
        return self.game_board[square]

    def get_occupant_by_num(self, num):
        square = self.reference_board[num]
        return self.get_occupant_by_alphanum(square)

    def set_square_occupant(self, square, occupant):
        self.game_board[square] = occupant
        return

    def move_piece(self, origin, destination):
        occupant = self.get_occupant_by_alphanum(destination)
        moving_piece = self.get_occupant_by_alphanum(origin)
        self.set_square_occupant(destination, moving_piece)
        self.set_square_occupant(origin, '.')
        moving_piece.set_square(destination)
        if occupant != '.':
            occupant.set_square(None)
            self.active_pieces.remove(occupant)
        return

    def occupant_is_piece_by_alphanum(self, alphanum):
        occupant = self.get_occupant_by_alphanum(alphanum)
        if occupant != "." and occupant is not None:
            return True
        else:
            return False

    def occupant_is_piece_by_num(self, num):
        square = self.game_board[num]
        occupant_is_piece = self.occupant_is_piece_alphanum(square)
        if occupant_is_piece:
            return True
        else:
            return False

    def generate_pieces(self):
        # black pieces
        br1 = Piece('R', 'black', 'a8')
        br2 = Piece('R', 'black', 'h8')
        bn1 = Piece('N', 'black', 'b8')
        bn2 = Piece('N', 'black', 'g8')
        bb1 = Piece('B', 'black', 'c8')
        bb2 = Piece('B', 'black', 'f8')
        bk = Piece('K', 'black', 'e8')
        bq = Piece('Q', 'black', 'd8')
        bp1 = Piece('p', 'black', 'a7')
        bp2 = Piece('p', 'black', 'b7')
        bp3 = Piece('p', 'black', 'c7')
        bp4 = Piece('p', 'black', 'd7')
        bp5 = Piece('p', 'black', 'e7')
        bp6 = Piece('p', 'black', 'f7')
        bp7 = Piece('p', 'black', 'g7')
        bp8 = Piece('p', 'black', 'h7')
        # white pieces
        wr1 = Piece('R', 'white', 'a1')
        wr2 = Piece('R', 'white', 'h1')
        wn1 = Piece('N', 'white', 'b1')
        wn2 = Piece('N', 'white', 'g1')
        wb1 = Piece('B', 'white', 'c1')
        wb2 = Piece('B', 'white', 'f1')
        wk = Piece('K', 'white', 'e1')
        wq = Piece('Q', 'white', 'd1')
        wp1 = Piece('p', 'white', 'a2')
        wp2 = Piece('p', 'white', 'b2')
        wp3 = Piece('p', 'white', 'c2')
        wp4 = Piece('p', 'white', 'd2')
        wp5 = Piece('p', 'white', 'e2')
        wp6 = Piece('p', 'white', 'f2')
        wp7 = Piece('p', 'white', 'g2')
        wp8 = Piece('p', 'white', 'h2')
        list_of_generated_pieces = [
            br1, br2, bn1, bn2, bb1, bb2, bk, bq, bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8,
            wr1, wr2, wn1, wn2, wb1, wb2, wk, wq, wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8]
        for piece in list_of_generated_pieces:
            self.active_pieces.append(piece)
        return

    def set_pieces(self):
        for piece in self.active_pieces:
            square = piece.get_square()
            self.set_square_occupant(square, piece)
        return

    def print_board(self):
        counter = 1
        for key in self.game_board.keys():
            occupant = self.game_board[key]
            if counter % 8 == 0:
                if occupant == '.':
                    print(f"{occupant}\n")
                    counter += 1

                if occupant != '.':
                    piece = occupant.get_piece_type()
                    print(piece)
                    counter +=1

            else:
                if occupant == '.':
                    print(f"{occupant}", end="   ")
                    counter += 1

                if occupant != '.':
                    piece = occupant.get_piece_type()
                    print(f"{piece}", end="   ")
                    counter += 1

        return


def main():

    game = Game()
    game.generate_pieces()
    game.set_pieces()
    game.print_board()
    for x in game.active_pieces:
        print(f"{x.get_team()} {x.get_piece_type()} on {x.get_square()}")
    game.move_piece('a2', 'a4')
    game.print_board()
    game.move_piece('b7', 'b5')
    game.print_board()
    game.move_piece('a4', 'b5')
    game.print_board()

    print(game.rook_queen_up_range('c2'))
    print(game.rook_queen_down_range('a7'))
    for x in game.active_pieces:
        print(f"{x.get_team()} {x.get_piece_type()} on {x.get_square()}")

    print(game.rook_queen_right_range('b5'))
    game.move_piece('h2', 'h4')
    game.move_piece('d2', 'd4')
    print(game.rook_queen_left_range('h4'))
    game.print_board()
    print(game.bishop_queen_up_right_range('d4'))
    print(game.bishop_queen_up_left_range('d4'))
    print(game.bishop_queen_down_right_range('d4'))
    print(game.bishop_queen_down_left_range('d4'))
    print(game.knight_range('d4'))
    print(game.knight_range('g7'))





if __name__ == '__main__':
    main()



