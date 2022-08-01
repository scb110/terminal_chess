#from dataclasses import replace
#from functools import total_ordering
#from turtle import down
#from unicodedata import numeric
#from modules.colors import Colors
#c = Colors
class ChessGame:
    """This class provides the foundation for two players to engaage in a
    friendly(or not so friendly...) game of command line chess"""

    def __init__(self):
        """ initializer       """
        self._boardcoordinates ={
        'a8': 18, 'b8': 28, 'c8': 38, 'd8': 48, 'e8': 58, 'f8': 68, 'g8': 78, 'h8':88,
        'a7': 17, 'b7': 27, 'c7': 37, 'd7': 47, 'e7': 57, 'f7': 67, 'g7': 77, 'h7': 87,
        'a6': 16, 'b6': 26, 'c6': 36, 'd6': 46, 'e6': 56, 'f6': 66, 'g6': 76, 'h6': 86,
        'a5': 15, 'b5': 25, 'c5': 35, 'd5': 45, 'e5': 55, 'f5': 65, 'g5': 75, 'h5': 85,
        'a4': 14, 'b4': 24, 'c4': 34, 'd4': 44, 'e4': 54, 'f4': 64, 'g4': 74, 'h4': 84,
        'a3': 13, 'b3': 23, 'c3': 33, 'd3': 43, 'e3': 53, 'f3': 63, 'g3': 73, 'h3': 83,
        'a2': 12, 'b2': 22, 'c2': 32, 'd2': 42, 'e2': 52, 'f2': 62, 'g2': 72, 'h2': 82,
        'a1': 11, 'b1': 21, 'c1': 31, 'd1': 41, 'e1': 51, 'f1': 61, 'g1': 71, 'h1': 81
        }
        

        self._active_board ={
        18:'.', 28: '.', 38: '.', 48: '.', 58: '.', 68:'.', 78:'.', 88:'.',
        17:'.', 27: '.', 37: '.', 47: '.', 57: '.', 67:'.', 77:'.', 87:'.',
        16:'.', 26: '.', 36: '.', 46: '.', 56: '.', 66:'.', 76:'.', 86:'.',
        15:'.', 25: '.', 35: '.', 45: '.', 55: '.', 65:'.', 75:'.', 85:'.',
        14:'.', 24: '.', 34: '.', 44: '.', 54: '.', 64:'.', 74:'.', 84:'.',
        13:'.', 23: '.', 33: '.', 43: '.', 53: '.', 63:'.', 73:'.', 83:'.',
        12:'.', 22: '.', 32: '.', 42: '.', 52: '.', 62:'.', 72:'.', 82:'.',
        11:'.', 21: '.', 31: '.', 41: '.', 51: '.', 61:'.', 71:'.', 81:'.'
        }
        
        # will hold pieces of piece type
        self._pieces = []

        self._game_history = []
        self._moving_team = 1
    
    
    def reset_game(self):
        self._pieces = []
        self._moving_team = 1
        self._active_board ={
        18:'.', 28: '.', 38: '.', 48: '.', 58: '.', 68:'.', 78:'.', 88:'.',
        17:'.', 27: '.', 37: '.', 47: '.', 57: '.', 67:'.', 77:'.', 87:'.',
        16:'.', 26: '.', 36: '.', 46: '.', 56: '.', 66:'.', 76:'.', 86:'.',
        15:'.', 25: '.', 35: '.', 45: '.', 55: '.', 65:'.', 75:'.', 85:'.',
        14:'.', 24: '.', 34: '.', 44: '.', 54: '.', 64:'.', 74:'.', 84:'.',
        13:'.', 23: '.', 33: '.', 43: '.', 53: '.', 63:'.', 73:'.', 83:'.',
        12:'.', 22: '.', 32: '.', 42: '.', 52: '.', 62:'.', 72:'.', 82:'.',
        11:'.', 21: '.', 31: '.', 41: '.', 51: '.', 61:'.', 71:'.', 81:'.'
        }
        self.get_start_pieces()
        self.set_pieces()
        print("NEW GAME!")
        return 

    def update_moving_team(self):
        self._moving_team += 1
        return
    
    def get_moving_team_color(self):
        if self._moving_team % 2 == 0:
            return "black"
        
        if self._moving_team % 2 == 1:
            return "white"

    def rook_queen_up_range(self, start_square):
        moving_piece = self.get_piece_on_square(start_square)
        moving_team = moving_piece.get_team()
        rq_up_range = []
        numeric = int(self._boardcoordinates[start_square])+1
        while ((numeric%10) < 9):
            alpha= self.get_alphanumeric_by_numeric(numeric)
            if self.is_empty_square(alpha) is False:
                candidate = self.piece_by_numeric(numeric)

                if candidate.get_team()==moving_team:
                    return rq_up_range

                else:
                    rq_up_range.append(self.get_alphanumeric_by_numeric(numeric))
                    return rq_up_range
            else:
                rq_up_range.append(self.get_alphanumeric_by_numeric(numeric))
                numeric += 1

        return rq_up_range

    def rook_queen_down_range(self, start_square):
        moving_piece = self.get_piece_on_square(start_square)
        moving_team = moving_piece.get_team()
        rq_down_range = []
        numeric = int(self._boardcoordinates[start_square])-1
        while ((numeric%10)>0):
            alpha= self.get_alphanumeric_by_numeric(numeric)
            if self.is_empty_square(alpha) is False:
                candidate = self.piece_by_numeric(numeric)

                if candidate.get_team()==moving_team:
                    return rq_down_range

                else:
                    rq_down_range.append(self.get_alphanumeric_by_numeric(numeric))
                    return rq_down_range
            else:
                rq_down_range.append(self.get_alphanumeric_by_numeric(numeric))
                numeric -= 1

        return rq_down_range

    def rook_queen_left_range(self, start_square):
        moving_piece = self.get_piece_on_square(start_square)
        moving_team = moving_piece.get_team()
        rq_left_range = []
        numeric = int(self._boardcoordinates[start_square])-10
        while (numeric > 10 ):
            alpha = self.get_alphanumeric_by_numeric(numeric)

            if self.is_empty_square(alpha) is False:
                candidate = self.piece_by_numeric(numeric)

                if candidate.get_team()==moving_team:
                    return rq_left_range

                else:
                    rq_left_range.append(self.get_alphanumeric_by_numeric(numeric))
                    return rq_left_range
            else:
                rq_left_range.append(self.get_alphanumeric_by_numeric(numeric))
                numeric -= 10

        return rq_left_range

    def coordinate_is_on_board(self, coord):
        valid_numerics = list(self._active_board.keys())
        for valid_coord in valid_numerics:
            if valid_coord == coord:
                return True
        return False


    def rook_queen_right_range(self, start_square):
        moving_piece = self.get_piece_on_square(start_square)
        moving_team = moving_piece.get_team()
        rq_right_range = []
        numeric = int(self._boardcoordinates[start_square])+10
        while (numeric < 89 ):
            alpha = self.get_alphanumeric_by_numeric(numeric)

            if self.is_empty_square(alpha) is False:
                candidate = self.piece_by_numeric(numeric)

                if candidate.get_team()==moving_team:
                    return rq_right_range

                else:
                    rq_right_range.append(self.get_alphanumeric_by_numeric(numeric))
                    return rq_right_range
            else:
                rq_right_range.append(self.get_alphanumeric_by_numeric(numeric))
                numeric += 10

        return rq_right_range

    def bishop_queen_up_right_range(self, start_square):
        moving_piece = self.get_piece_on_square(start_square)
        moving_team = moving_piece.get_team()
        bq_up_right_range = []
        numeric = int(self._boardcoordinates[start_square])+11
        if self.coordinate_is_on_board(numeric) is False:
            return bq_up_right_range
        alpha = self.get_alphanumeric_by_numeric(numeric)
        while self.square_is_on_board(alpha):
            alpha = self.get_alphanumeric_by_numeric(numeric)
            if self.is_empty_square(alpha) is False:
                candidate = self.piece_by_numeric(numeric)

                if candidate.get_team()==moving_team:
                    return bq_up_right_range
                else:
                    bq_up_right_range.append(self.get_alphanumeric_by_numeric(numeric))
                    return bq_up_right_range
            else:
                bq_up_right_range.append(self.get_alphanumeric_by_numeric(numeric))
                numeric += 11
                if self.coordinate_is_on_board(numeric) is False:
                    return bq_up_right_range
                else:
                    alpha= self.get_alphanumeric_by_numeric(numeric)

        return bq_up_right_range

    def bishop_queen_up_left_range(self, start_square):
        moving_piece = self.get_piece_on_square(start_square)
        moving_team = moving_piece.get_team()
        bq_up_left_range = []
        numeric = int(self._boardcoordinates[start_square])-9
        if self.coordinate_is_on_board(numeric) is False:
            return bq_up_left_range
        alpha = self.get_alphanumeric_by_numeric(numeric)
        while self.square_is_on_board(alpha):
            alpha = self.get_alphanumeric_by_numeric(numeric)
            if self.is_empty_square(alpha) is False:
                candidate = self.piece_by_numeric(numeric)

                if candidate.get_team()==moving_team:
                    return bq_up_left_range
                else:
                    bq_up_left_range.append(self.get_alphanumeric_by_numeric(numeric))
                    return bq_up_left_range
            else:
                bq_up_left_range.append(self.get_alphanumeric_by_numeric(numeric))
                numeric -= 9
                if self.coordinate_is_on_board(numeric) is False:
                    return bq_up_left_range
                else:
                    alpha= self.get_alphanumeric_by_numeric(numeric)
                
        return bq_up_left_range

    def bishop_queen_down_left_range(self, start_square):
        moving_piece = self.get_piece_on_square(start_square)
        moving_team = moving_piece.get_team()
        bq_down_left_range = []
        numeric = int(self._boardcoordinates[start_square])-11
        if self.coordinate_is_on_board(numeric) is False:
            return bq_down_left_range
        alpha = self.get_alphanumeric_by_numeric(numeric)
        while self.square_is_on_board(alpha):
            alpha = self.get_alphanumeric_by_numeric(numeric)
            if self.is_empty_square(alpha) is False:
                candidate = self.piece_by_numeric(numeric)

                if candidate.get_team()==moving_team:
                    return bq_down_left_range
                else:
                    bq_down_left_range.append(self.get_alphanumeric_by_numeric(numeric))
                    return bq_down_left_range
            else:
                bq_down_left_range.append(self.get_alphanumeric_by_numeric(numeric))
                numeric -= 11
                if self.coordinate_is_on_board(numeric) is False:
                    return bq_down_left_range
                else:
                    alpha= self.get_alphanumeric_by_numeric(numeric)
                
        return bq_down_left_range

    def bishop_queen_down_right_range(self, start_square):
        moving_piece = self.get_piece_on_square(start_square)
        moving_team = moving_piece.get_team()
        bq_down_right_range = []
        numeric = int(self._boardcoordinates[start_square])+9
        if self.coordinate_is_on_board(numeric) is False:
            return bq_down_right_range
        alpha = self.get_alphanumeric_by_numeric(numeric)
        while self.square_is_on_board(alpha):
            alpha = self.get_alphanumeric_by_numeric(numeric)
            if self.is_empty_square(alpha) is False:
                candidate = self.piece_by_numeric(numeric)

                if candidate.get_team()==moving_team:
                    return bq_down_right_range
                else:
                    bq_down_right_range.append(self.get_alphanumeric_by_numeric(numeric))
                    return bq_down_right_range
            else:
                bq_down_right_range.append(self.get_alphanumeric_by_numeric(numeric))
                numeric += 9
                if self.coordinate_is_on_board(numeric) is False:
                    return bq_down_right_range
                else:
                    alpha= self.get_alphanumeric_by_numeric(numeric)
                
        return bq_down_right_range


    def square_is_on_board(self, coord):
        list_of_squares = self._boardcoordinates.keys()
        for square in list_of_squares:
            if square == coord:
                return True
        return False


    def move_is_on_board(self, coord1, coord2):
        if self.square_is_on_board(coord1) and self.square_is_on_board(coord2):
            return True
        else:
            if self.square_is_on_board(coord1) is False:
                print(f"{coord1} is not a valid square.  (file must be a-g and rank must be 1-8)")
            if self.square_is_on_board(coord2) is False:
                print(f"{coord2} is not a valid square.  (file must be a-g and rank must be 1-8)")
            return False

    def is_empty_square(self, alphanumeric):
        if self.get_piece_on_square(alphanumeric) == '.':
            return True
        else:
            return False

    def get_numeric_boardcoord(self, alphanumeric):
        numeric_boardcoord = self._boardcoordinates[alphanumeric]
        return numeric_boardcoord

    def get_piece_on_square(self, square):
        numeric_location = self.get_numeric_boardcoord(square)
        piece_on_square = self._active_board[numeric_location]
        return piece_on_square

    def piece_by_numeric(self, number):
        """used for internal cases when dealing already with numeric values needing to reference square occupant"""
        numeric_location = number
        piece = self._active_board[numeric_location]
        return piece

    def get_alphanumeric_by_numeric(self, numeric):
        keys_are = list(self._boardcoordinates.keys())
        values_are = list(self._boardcoordinates.values())
        return list(keys_are)[list(values_are).index(numeric)]

    def update_square(self, square, occupant):
        numeric_square = self.get_numeric_boardcoord(square)
        self._active_board[numeric_square] = occupant


    def move_piece(self, from_coord, to_coord):
        """method that takes a reference to a piece by the coordinate it is on, as well as a reference
        to the coordinate it should move to, and then moves the piece to that coordinate."""

        moving_piece = self.get_piece_on_square(from_coord)
        current_occupant = self.get_piece_on_square(to_coord)
        if (current_occupant == '.'):
            moving_piece.set_square(to_coord)
            self.update_square(to_coord, moving_piece)
            self.update_square(from_coord, '.')
            return

        if current_occupant.get_team() != moving_piece.get_team():
            captured_piece = self.get_piece_on_square(to_coord)
            captured_piece.set_square(None)
            self._pieces.remove(current_occupant)
            moving_piece.set_square(to_coord)
            self.update_square(to_coord, moving_piece)
            self.update_square(from_coord, '.')
            return
        
        else:
            print("You can't capture your own piece!")
            return 
        


    def print_board(self):
        """a method that prints the current state of the board to the screen"""
        
        total_placed = 1
        for square in self._active_board:
            if total_placed %8 == 0:
                if self._active_board[square]=='.':
                    print(f"{self._active_board[square]}")
                

                else:
                    piece = self._active_board[square]
                    piece_print_val = piece.get_shape()
                    print(f"{piece_print_val}")

                total_placed += 1
                
            else:
                if self._active_board[square]=='.':
                    print(f"{self._active_board[square]}", end="   ")
                

                else:
                    piece = self._active_board[square]
                    piece_print_val = piece.get_shape()
                    print(f"{piece_print_val}", end="   ")
                    
                total_placed += 1


        

    def get_start_pieces(self):
        # black and white pawns
        bp1 = Piece('a7', 'p', 'black')
        bp2 = Piece('b7', 'p', 'black')
        bp3 = Piece('c7', 'p', 'black')
        bp4 = Piece('d7', 'p', 'black')
        bp5 = Piece('e7', 'p', 'black')
        bp6 = Piece('f7', 'p', 'black')
        bp7 = Piece('g7', 'p', 'black')
        bp8 = Piece('h7', 'p', 'black')
        wp1 = Piece('a2', 'p', 'white')
        wp2 = Piece('b2', 'p', 'white')
        wp3 = Piece('c2', 'p', 'white')
        wp4 = Piece('d2', 'p', 'white')
        wp5 = Piece('e2', 'p', 'white')
        wp6 = Piece('f2', 'p', 'white')
        wp7 = Piece('g2', 'p', 'white')
        wp8 = Piece('h2', 'p', 'white')

        # black pieces
        bR1 = Piece('a8', 'R', 'black')
        bR2 = Piece('h8', 'R', 'black')
        bN1 = Piece('b8', 'N', 'black')
        bN2 = Piece('g8', 'N', 'black')
        bB1 = Piece('c8', 'B', 'black')
        bB2 = Piece('f8', 'B', 'black')
        bK1 = Piece('e8', 'K', 'black')
        bQ1 = Piece('d8', 'Q', 'black')

        # white  pieces
        wR1 = Piece('a1', 'R', 'white')
        wR2 = Piece('h1', 'R', 'white')
        wN1 = Piece('b1', 'N', 'white')
        wN2 = Piece('g1', 'N', 'white')
        wB1 = Piece('c1', 'B', 'white')
        wB2 = Piece('f1', 'B', 'white')             
        wK1 = Piece('e1', 'K', 'white')
        wQ1 = Piece('d1', 'Q', 'white')


        # get all pieces stored in official game array
        all_pieces = [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8, wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8, bR1, bR2, bN1, bN2, bB1, bB2, bK1, bQ1, wR1, wR2, wN1, wN2, wB1, wB2, wK1, wQ1]
        for this_piece in all_pieces:
            self._pieces.append(this_piece)

        for piece in self._pieces:
            for coord in self._boardcoordinates:
                if piece.get_square() == coord:
                    print(f"{piece.get_square()} = {self._boardcoordinates[coord]}")

    def set_pieces(self):
        """A method to to take all pieces in the self._pieces array and place them on the board"""

        #for piece in self._pieces:
        #    for coord in self._boardcoordinates:
        #        if piece.get_square() == coord:
        #            set_piece_at = int(self._boardcoordinates[coord])
        #            self._active_board[set_piece_at] = piece.get_shape()
        for piece in self._pieces:
            location = piece.get_square()
            self.update_square(location, piece)

    
    def queen_options_this_turn(self, queen_pos):
        current_options = []
        ur = self.bishop_queen_up_right_range(queen_pos)
        ul = self.bishop_queen_up_left_range(queen_pos)
        dr = self.bishop_queen_down_right_range(queen_pos)
        dl = self.bishop_queen_down_left_range(queen_pos)
        u =  self.rook_queen_up_range(queen_pos)
        d =  self.rook_queen_down_range(queen_pos)
        r =  self.rook_queen_right_range(queen_pos)
        l =  self.rook_queen_left_range(queen_pos)
        all_options_lists = [ur, ul, dr, dl, u, d, r, l]
        for options_list in all_options_lists:
            for option in options_list:
                current_options.append(option)
        return current_options 

    def pawn_options_this_turn(self, pawn_pos):
        current_options = []

        captures = self.pawn_oblique_options(pawn_pos)
        for option in captures:
            current_options.append(option)

        forwards = self.pawn_forward_range(pawn_pos)
        for option in forwards:
            current_options.append(option)
        
        return current_options
        

    def pawn_oblique_options(self, square):
        pawn_diags = []
        moving_piece = self.get_piece_on_square(square)
        if moving_piece.get_team() == 'white':
            current_coord = self.get_numeric_boardcoord(square)
            diag_left_coord = current_coord-9
            if self.coordinate_is_on_board(diag_left_coord):
                diag_left_piece = self.piece_by_numeric(diag_left_coord)
                if diag_left_piece != '.':
                    if diag_left_piece.get_team()=='black':
                        left_black_target = diag_left_piece.get_square()
                        pawn_diags.append(left_black_target)

            diag_right_coord = current_coord+11
            if self.coordinate_is_on_board(diag_right_coord):
                diag_right_piece = self.piece_by_numeric(diag_right_coord)            
                if diag_right_piece != '.':
                    if diag_right_piece.get_team()=='black':
                        right_black_target = diag_right_piece.get_square()
                        pawn_diags.append(right_black_target)
            return pawn_diags

        if moving_piece.get_team() == 'black':
            current_coord = self.get_numeric_boardcoord(square)
            diag_left_coord = current_coord+9
            if self.coordinate_is_on_board(diag_left_coord):
                diag_left_piece = self.piece_by_numeric(diag_left_coord)
                if diag_left_piece != '.':
                    if diag_left_piece.get_team()=='white':
                        left_white_target = diag_left_piece.get_square()
                        pawn_diags.append(left_white_target)

            diag_right_coord = current_coord-11
            if self.coordinate_is_on_board(diag_right_coord):
                diag_right_piece = self.piece_by_numeric(diag_right_coord)            
                if diag_right_piece != '.':
                    if diag_right_piece.get_team()=='white':
                        right_white_target = diag_right_piece.get_square()
                        pawn_diags.append(right_white_target)
            return pawn_diags

        return pawn_diags


    
    def pawn_forward_range(self, square):
        pawn_forward_options = []
        moving_piece = self.get_piece_on_square(square)
        if moving_piece.get_team() == 'white':
            current_coord = self.get_numeric_boardcoord(square)
            if current_coord%10 == 2:
                third_rank_coord = current_coord + 1
                third_rank_piece = self.piece_by_numeric(third_rank_coord)
                fourth_rank_coord = current_coord + 2
                fourth_rank_piece = self.piece_by_numeric(fourth_rank_coord)
                
                if third_rank_piece == ".":
                    option = self.get_alphanumeric_by_numeric(third_rank_coord)
                    pawn_forward_options.append(option)
            
                if (third_rank_piece == ".") and (fourth_rank_piece=="."):
                    option2 = self.get_alphanumeric_by_numeric(fourth_rank_coord)
                    pawn_forward_options.append(option2)
                return pawn_forward_options
            
            if ((current_coord%10)<=7) and ((current_coord%10)>2):
                next_rank_coord = current_coord + 1
                next_rank_piece = self.piece_by_numeric(next_rank_coord)
                if (next_rank_piece == "."):
                    forward_option = self.get_alphanumeric_by_numeric(next_rank_coord)
                    pawn_forward_options.append(forward_option)
                return pawn_forward_options
            if (current_coord%10)==8:
                print("Time to promote this pawn")
                    
            return pawn_forward_options

        if moving_piece.get_team() == 'black':
            current_coord = self.get_numeric_boardcoord(square)
            if current_coord%10 == 7:
                sixth_rank_coord = current_coord - 1
                sixth_rank_piece = self.piece_by_numeric(sixth_rank_coord)
                fifth_rank_coord = current_coord - 2
                fifth_rank_piece = self.piece_by_numeric(fifth_rank_coord)
                
                if sixth_rank_piece == ".":
                    option = self.get_alphanumeric_by_numeric(sixth_rank_coord)
                    pawn_forward_options.append(option)
            
                if (sixth_rank_piece == ".") and (fifth_rank_piece=="."):
                    option2 = self.get_alphanumeric_by_numeric(fifth_rank_coord)
                    pawn_forward_options.append(option2)
                return pawn_forward_options
            
            if ((current_coord%10)>=2) and ((current_coord%10)<7):
                next_rank_coord = current_coord - 1
                next_rank_piece = self.piece_by_numeric(next_rank_coord)
                if (next_rank_piece == "."):
                    forward_option = self.get_alphanumeric_by_numeric(next_rank_coord)
                    pawn_forward_options.append(forward_option)
                return pawn_forward_options
            if (current_coord%10)==1:
                print("Time to promote this pawn")
                    
                return pawn_forward_options
    
    
    
    def rook_options_this_turn(self, rook_pos):
        current_options = []
        u =  self.rook_queen_up_range(rook_pos)
        d =  self.rook_queen_down_range(rook_pos)
        r =  self.rook_queen_right_range(rook_pos)
        l =  self.rook_queen_left_range(rook_pos)
        all_options_lists = [u, d, r, l]
        for options_list in all_options_lists:
            for option in options_list:
                current_options.append(option)
        return current_options 

    def knight_options_this_turn(self, coord):
        start_coord = self.get_numeric_boardcoord(coord)
        moving_piece = self.piece_by_numeric(start_coord)
        oct1 = start_coord + 12
        oct2 = start_coord + 21
        oct3 = start_coord + 19
        oct4 = start_coord + 8
        oct5 = start_coord - 12
        oct6 = start_coord - 21
        oct7 = start_coord - 19
        oct8 = start_coord - 8
        valid_moves=[]
        numeric_range = [oct1, oct2, oct3, oct4, oct5, oct6, oct7, oct8]
        for numeric_spot in numeric_range:
            if self.coordinate_is_on_board(numeric_spot):
                occupant = self.piece_by_numeric(numeric_spot)
                if occupant == '.':
                    open_square = self.get_alphanumeric_by_numeric(numeric_spot)
                    valid_moves.append(open_square)
                
                if (occupant!='.') and occupant.get_team() != moving_piece.get_team():
                    potential_octopus_victim = occupant.get_square()
                    valid_moves.append(potential_octopus_victim)
                
        return valid_moves

    def bishop_options_this_turn(self, bishop_pos):
        current_options = []
        ur = self.bishop_queen_up_right_range(bishop_pos)
        ul = self.bishop_queen_up_left_range(bishop_pos)
        dr = self.bishop_queen_down_right_range(bishop_pos)
        dl = self.bishop_queen_down_left_range(bishop_pos)
        all_options_lists = [ur, ul, dr, dl]
        for options_list in all_options_lists:
            for option in options_list:
                current_options.append(option)
        return current_options

    def get_current_on_boards(self):
        active_pieces = []
        for coord in self._active_board:
            occupant = self.piece_by_numeric(coord)
            if occupant != '.':
                active_pieces.append(occupant)
        return active_pieces

    def king_directionals(self, king_pos):
        numeric_coord = self.get_numeric_boardcoord(king_pos)
        side_1 = numeric_coord + 1
        side_2 = numeric_coord + 11
        side_3 = numeric_coord + 10
        side_4 = numeric_coord + 9
        side_5 = numeric_coord - 1
        side_6 = numeric_coord - 11
        side_7 = numeric_coord - 10
        side_8 = numeric_coord + 9
        squares_on_board = []
        list_of_numeric_options = [side_1, side_2, side_3, side_4, side_5, side_6, side_7, side_8]
        for option in list_of_numeric_options:
            on_board = self.coordinate_is_on_board(option)
            if on_board is True:
                square = self.get_alphanumeric_by_numeric(option)
                squares_on_board.append(square)
        return squares_on_board

    def get_opposing_pieces(self, moving_team):
        all_pieces = self.get_current_on_boards()
        opposing_pieces = []
        for piece in all_pieces:
            if piece.get_team() != moving_team:
                opposing_pieces.append(piece)
        return opposing_pieces

    def get_opposing_team_moves(self, moving_team):
        enemies = self.get_opposing_pieces(moving_team)
        enemy_options = []
        for enemy in enemies:
            if enemy.get_shape() == "Q":
                queen_options = self.queen_options_this_turn(enemy.get_square())
                for option in queen_options:
                    enemy_options.append(option)
            if enemy.get_shape() == "R":
                rook_options = self.rook_options_this_turn(enemy.get_square())
                for option in rook_options:
                    enemy_options.append(option)
            if enemy.get_shape() == "B":
                bishop_options = self.bishop_options_this_turn(enemy.get_square())
                for option in bishop_options:
                    enemy_options.append(option)
            if enemy.get_shape() == "N":
                knight_options = self.knight_options_this_turn(enemy.get_square())
                for option in knight_options:
                    enemy_options.append(option)
            if enemy.get_shape() == "p":
                pawn_options = self.pawn_options_this_turn(enemy.get_square())
                for option in pawn_options:
                    enemy_options.append(option)

        return enemy_options

    def get_opposing_team_threats(self, moving_team):
        enemies = self.get_opposing_pieces(moving_team)
        enemy_options = []
        for enemy in enemies:
            if enemy.get_shape() == "K":
                king_options = self.king_directionals(enemy.get_square())
                for option in king_options:
                    enemy_options.append(option)

            if enemy.get_shape() == "Q":
                queen_options = self.queen_options_this_turn(enemy.get_square())
                for option in queen_options:
                    enemy_options.append(option)
            if enemy.get_shape() == "R":
                rook_options = self.rook_options_this_turn(enemy.get_square())
                for option in rook_options:
                    enemy_options.append(option)
            if enemy.get_shape() == "B":
                bishop_options = self.bishop_options_this_turn(enemy.get_square())
                for option in bishop_options:
                    enemy_options.append(option)
            if enemy.get_shape() == "N":
                knight_options = self.knight_options_this_turn(enemy.get_square())
                for option in knight_options:
                    enemy_options.append(option)
            if enemy.get_shape() == "p":
                pawn_options = self.pawn_oblique_options(enemy.get_square())
                for option in pawn_options:
                    enemy_options.append(option)

        return enemy_options

    def king_move_is_legal(self, king_start_square, try_square, color):
        # create a new game
        hypothetical = ChessGame()
        # set pieces to original position.  
        hypothetical.get_start_pieces()
        hypothetical.set_pieces()
        # take list of tuples which is the list of moves  (self._game_history) of the current game

        # iterate through list of moves simply calling to get to current position
        hypothetical.copy_position(self._game_history)
        # play the hypothetical king move by calling move_piece King to try_square
        hypothetical.move_piece(king_start_square, try_square)
        # check opposing threats.  ***Still need to modify for pawns...only include their kill places***
        enemy_threats = hypothetical.get_opposing_team_threats(color)
        # if there is any threat at all return False
        for threatened_square in enemy_threats:
            if threatened_square == try_square:
                return False
        # Otherwise return true
        return True

    def in_check(self, color):
        hypothetical = ChessGame()
        hypothetical.get_start_pieces()
        hypothetical.set_pieces()
        hypothetical.copy_position(self._game_history)
        if color == 'black':
            ally_pieces = hypothetical.get_opposing_pieces('white')
            for ally in ally_pieces:
                # find potentially attacked king
                if ally.get_shape() == "K":
                    # look at his enemy's threats after move
                    enemy_threats = hypothetical.get_opposing_team_threats('black')
                    for threatened_square in enemy_threats:
                        if ally.get_square() == threatened_square:
                            # if a threatened square is the square he's on, return True
                            return True
        if color == 'white':
            ally_pieces = hypothetical.get_opposing_pieces('black')
            for ally in ally_pieces:
                if ally.get_shape() == "K":
                    enemy_threats = hypothetical.get_opposing_team_threats('white')
                    for threatened_square in enemy_threats:
                        if ally.get_square() == threatened_square:
                            return True

        # reaching this means not in check
        return False

    def checkmate_delivered(self, start_square, try_square, color):
        # get checked position
        hypothetical = ChessGame()
        hypothetical.get_start_pieces()
        hypothetical.set_pieces()
        hypothetical.copy_position(self._game_history)
        hypothetical.move_piece(start_square, try_square)

        # pull up checked team's pieces
        if color == 'black':
            # black did checking, let's pull up white's allies
            ally_pieces = hypothetical.get_opposing_pieces('black')
            # iterate through checked team's pieces
            for ally in ally_pieces:
                # grab piece's square for reference starting_point
                starting_point = ally.get_square()
                # get piece's options
                if ally.get_shape() == 'K':
                    potentials = hypothetical.king_directionals(starting_point)
                    for option in potentials:
                        if hypothetical.king_move_is_legal(starting_point, option):
                            # see if still check...if not return False
                            if hypothetical.still_in_check(starting_point, option, 'white') is False:
                                return False

                if ally.get_shape()=='Q':
                    potentials = hypothetical.queen_options_this_turn(starting_point)
                    for option in potentials:
                        if hypothetical.still_in_check(starting_point, option, 'white') is False:
                            return False
                if ally.get_shape()=='B':
                    potentials = hypothetical.bishop_options_this_turn(starting_point)
                    for option in potentials:
                        if hypothetical.still_in_check(starting_point, option, 'white') is False:
                            return False
                if ally.get_shape()=='N':
                    potentials = hypothetical.knight_options_this_turn(starting_point)
                    for option in potentials:
                        if hypothetical.still_in_check(starting_point, option, 'white') is False:
                            return False
                if ally.get_shape()=='R':
                    potentials = hypothetical.rook_options_this_turn(starting_point)
                    for option in potentials:
                        if hypothetical.still_in_check(starting_point, option, 'white') is False:
                            return False

                if ally.get_shape() == 'p':
                    potentials = hypothetical.pawn_options_this_turn(starting_point)
                    for option in potentials:
                        if hypothetical.still_in_check(starting_point, option, 'white') is False:
                            return False

        if color == 'white':
            # white did checking, let's pull up black's allies
            ally_pieces = hypothetical.get_opposing_pieces('white')
            # iterate through checked team's pieces
            for ally in ally_pieces:
                # grab piece's square for reference starting_point
                starting_point = ally.get_square()
                # get piece's options
                if ally.get_shape() == 'K':
                    potentials = hypothetical.king_directionals(starting_point)
                    for option in potentials:
                        if hypothetical.king_move_is_legal(starting_point, option):
                            # see if still check...if not return False
                            if hypothetical.still_in_check(starting_point, option, 'black') is False:
                                return False

                if ally.get_shape() == 'Q':
                    potentials = hypothetical.queen_options_this_turn(starting_point)
                    for option in potentials:
                        if hypothetical.still_in_check(starting_point, option, 'black') is False:
                            return False
                if ally.get_shape() == 'B':
                    potentials = hypothetical.bishop_options_this_turn(starting_point)
                    for option in potentials:
                        if hypothetical.still_in_check(starting_point, option, 'black') is False:
                            return False
                if ally.get_shape() == 'N':
                    potentials = hypothetical.knight_options_this_turn(starting_point)
                    for option in potentials:
                        if hypothetical.still_in_check(starting_point, option, 'black') is False:
                            return False
                if ally.get_shape() == 'R':
                    potentials = hypothetical.rook_options_this_turn(starting_point)
                    for option in potentials:
                        if hypothetical.still_in_check(starting_point, option, 'black') is False:
                            return False

                if ally.get_shape() == 'p':
                    potentials = hypothetical.pawn_options_this_turn(starting_point)
                    for option in potentials:
                        if hypothetical.still_in_check(starting_point, option, 'black') is False:
                            return False

        # if we get this far, that means there was no saving move...checkmate has been delivered
        # return True to alert of status
        return True

    def still_in_check(self, start_square, try_square, color):
        # generate position on hypothetical board
        hypothetical = ChessGame()
        hypothetical.get_start_pieces()
        hypothetical.set_pieces()
        hypothetical.copy_position(self._game_history)
        hypothetical.move_piece(start_square, try_square)

        if color == 'black':
            ally_pieces = hypothetical.get_opposing_pieces('white')
            for ally in ally_pieces:
                # find potentially attacked king
                if ally.get_shape() == "K":
                    # look at his enemy's threats after move
                    enemy_threats = hypothetical.get_opposing_team_threats('black')
                    for threatened_square in enemy_threats:
                        if ally.get_square() == threatened_square:
                            # if a threatened square is the square he's on, return True
                            return True

        if color == 'white':
            ally_pieces = hypothetical.get_opposing_pieces('black')
            for ally in ally_pieces:
                if ally.get_shape() == "K":
                    enemy_threats = hypothetical.get_opposing_team_threats('white')
                    for threatened_square in enemy_threats:
                        if ally.get_square() == threatened_square:
                            return True

        return False

    def checked_opponent(self, start_square, try_square, color):
        # generate position on hypothetical board
        hypothetical = ChessGame()
        hypothetical.get_start_pieces()
        hypothetical.set_pieces()
        hypothetical.copy_position(self._game_history)
        hypothetical.move_piece(start_square, try_square)

        if color == 'black':
            ally_pieces = hypothetical.get_opposing_pieces('black')
            for ally in ally_pieces:
                # find potentially attacked king
                if ally.get_shape() == "K":
                    # look at his enemy's threats after move
                    enemy_threats = hypothetical.get_opposing_team_threats('white')
                    for threatened_square in enemy_threats:
                        if ally.get_square() == threatened_square:
                            # if a threatened square is the square he's on, return True
                            return True

        if color == 'white':
            ally_pieces = hypothetical.get_opposing_pieces('white')
            for ally in ally_pieces:
                if ally.get_shape() == "K":
                    enemy_threats = hypothetical.get_opposing_team_threats('black')
                    for threatened_square in enemy_threats:
                        if ally.get_square() == threatened_square:
                            return True

        return False

    def tuple_move(self, moved_from, moved_to):
        approved_move = (moved_from, moved_to)
        return approved_move

    def document_move(self, approved_move):
        self._game_history.append(approved_move)
        return 

    def copy_position(self, documented_moves_list):
        for move in documented_moves_list:
            moved_from = move[0]
            moved_to = move[1]
            this_move = (moved_from, moved_to)
            self.move_piece(moved_from, moved_to)
            self._game_history.append(this_move)
            self.update_moving_team()
            
        return 

    def play(self, origin, destination):
        print(f"({self.get_moving_team_color}'s turn)")
        moving_piece = self.get_piece_on_square(origin)

        # check that turn and color match up
        if moving_piece.get_team() != self.get_moving_team_color():
            print(f"It's not {moving_piece.get_team()}'s turn, it's {self.get_moving_team_color()}'s turn")
            return 
        
        # check that move is on board
        if self.move_is_on_board(origin, destination) is False:
            return
        
        # make sure that the specific piece is moving to a valid option in the position
        piece_type = moving_piece.get_shape()
        if piece_type == "K":
            legal_king_move = bool(self.king_move_is_legal(origin, destination, self.get_moving_team_color()))
            if legal_king_move is False:
                print(f"That is not an option for the {moving_piece.get_team()} king on {origin}")
                return

        if piece_type == "Q":
            queen_moves = self.queen_options_this_turn(origin)
            if destination not in queen_moves:
                print(f"That is not an option for the {moving_piece.get_team()} piece on {origin}")
                return 

        if piece_type == "R":
            rook_moves = self.rook_options_this_turn(origin)
            if destination not in rook_moves:
                print(f"That is not an option for the {moving_piece.get_team()} piece on {origin}")
                return 
        
        if piece_type == "N":
            knight_moves = self.knight_options_this_turn(origin)
            if destination not in knight_moves:
                print(f"That is not an option for the {moving_piece.get_team()} piece on {origin}")
                return 
        
        if piece_type == "B":
            bishop_moves = self.bishop_options_this_turn(origin)
            if destination not in bishop_moves:
                print(f"That is not an option for the {moving_piece.get_team()} piece on {origin}")
                return 

        if piece_type == "p":
            pawn_moves = self.pawn_options_this_turn(origin)
            if destination not in pawn_moves:
                print(f"That is not an option for the {moving_piece.get_team()} piece on {origin}")
                return

        in_check = bool(self.still_in_check(origin, destination, self.get_moving_team_color()))

        if in_check:
            print(f"Find a move that avoids check!")
            return

        # check is_check status
        checked_enemy_on_move = bool(self.checked_opponent(origin, destination, self.get_moving_team_color()))
        if checked_enemy_on_move:
            game_over = bool(self.checkmate_delivered(origin, destination, self.get_moving_team_color()))
            if game_over:
                self.move_piece(origin, destination)
                this_move = (origin, destination)
                self._game_history.append(this_move)
                self.print_board()
                print(f"CHECKMATE\nThe {self.get_moving_team_color()} team has won!!")
                self.reset_game()
                return
            else:
                print(f"CHECK!!")
        # make move
        self.move_piece(origin, destination)

        # store move
        this_move = (origin, destination)
        self._game_history.append(this_move)

        # update moving team
        self.update_moving_team()

        return 


class Piece:
    """The essential piece data type"""
    def __init__(self, square, shape, team):
        self._square = square
        self._shape = shape
        self._team = team

    def get_square(self):
        return self._square

    def set_square(self, new_square):
        self._square = new_square

    def get_shape(self):
        return self._shape

    def set_shape(self, new_shape):
        self._shape = new_shape
    
    def get_team(self):
        return self._team
    
    def set_team(self, new_team):
        self._team = new_team

    


     


def main():
    """
    game.print_board()
    print("\n\n")
    game.print_board()
    print("\n\n")
    game.move_piece('a2', 'a4')
    print("\n\n")
    game.move_piece('a7', 'a6')
    print("\n\n")
    game.move_piece('a1', 'a3')
    print("\n\n")
    game.move_piece('a4', 'a5')
    print("\n\n")
    game.move_piece('a3', 'e3')
    print("\n\n")
    game.move_piece('h7', 'h6')
    game.move_piece('e3', 'e7')
    game.move_piece('d2', 'd5')
    game.print_board()
    bishop_options = game.bishop_options_this_turn('d5')
    rook_options = game.rook_options_this_turn('d5')
    queen_options = game.queen_options_this_turn('d5')

    print(bishop_options)
    print("\n")
    print(rook_options)
    print("\n")
    print(queen_options)
    game.move_piece('f2', 'f4')
    game.move_piece('g7', 'g5')
    game.print_board()
    killer_rook_options = game.rook_options_this_turn('e7')
    black_g_pawn_options = game.pawn_options_this_turn('g5')
    white_f_pawn_options = game.pawn_options_this_turn('f4')

    print(killer_rook_options)
    print(black_g_pawn_options)
    print(white_f_pawn_options)
    #up_left = game.bishop_queen_up_left_range('d5')
    #down_right = game.bishop_queen_down_right_range('d5')
    #down_left = game.bishop_queen_down_left_range('d5')
    #print(f"upright range is: {up_right}")
    #print(f"upleft range is: {up_left}")
    #print(f"downright range is: {down_right}")
    #print(f"downleft range is: {down_left}")
    # """

    game = ChessGame()
    game.get_start_pieces()
    game.set_pieces()

   

    while True:
        print(f"{game.get_moving_team_color()}'s turn!")
        game.print_board()
        prompt_user_action = input("Type 'm' to move a piece or 'r' to reset game:   ")
        if prompt_user_action == 'm':
            prompt_origin = input("Enter a square to move from:  ")
            prompt_destination = input("Enter a square to move to:  ")
            game.play(prompt_origin, prompt_destination)
            
        if prompt_user_action == 'r':
            game.reset_game()


if __name__ == '__main__':
    main()









