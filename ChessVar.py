# Author: Jovanny Gochez
# GitHub username: jgochez
# Date: 08/18/2023
# Description: Portfolio Project


class ChessVar:
    """
    Class that represents the entire chess game
    along with its functionality
    """

    def __init__(self):
        """
        The constructor for ChessVar class. Takes no parameter,
        initializes the data members, and sets them as private.
        """

        self._referenceBoard = [['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'],
                                ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
                                ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6'],
                                ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5'],
                                ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4'],
                                ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3'],
                                ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
                                ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']]
        self._liveBoard = [['___', '___', '___', '___', '___', '___', '___', '___'],
                           ['___', '___', '___', '___', '___', '___', '___', '___'],
                           ['___', '___', '___', '___', '___', '___', '___', '___'],
                           ['___', '___', '___', '___', '___', '___', '___', '___'],
                           ['___', '___', '___', '___', '___', '___', '___', '___'],
                           ['___', '___', '___', '___', '___', '___', '___', '___'],
                           ['W_R', 'W1B', 'W1N', '___', '___', 'B1N', 'B1B', 'B_R'],
                           ['W_K', 'W2B', 'W2N', '___', '___', 'B2N', 'B2B', 'B_K']]
        self._board_row = None
        self._board_column = None
        self._check_for_player = 0

    def display_reference_board(self):
        """
        display reference board
        """
        for row in self._referenceBoard:
            print(row)
        print()

    def display_live_board(self):
        """
        display live board
        """
        for row in self._liveBoard:
            print(row)
        print()

    def find_index(self, current, new):
        """
        convert numerical chess locations
        to indexes to track pieces in our
        data structure
        """
        current_row = 0
        current_column = 0
        new_row = 0
        new_column = 0

        # find indices for current location
        for row in self._referenceBoard:
            for pos in row:
                if current == pos:
                    current_row = self._referenceBoard.index(row)
                    current_column = row.index(pos)

        # find indices for new location
        for row in self._referenceBoard:
            for pos in row:
                if new == pos:
                    new_row = self._referenceBoard.index(row)
                    new_column = row.index(pos)

        return current_row, current_column, new_row, new_column

    def check_king(self, row1, col1, row2, col2):
        """
        using mathematical formulas, we will produce every
        possible and legal move the piece can make
        """
        move1 = [row1 - 1, row1 + 0, row1 + 1]  # [row-down, row-none, row-up]
        move2 = [col1 - 1, col1 + 0, col1 + 1]  # [column-down, column-none, column-up]

        # every move is a combination of move1 and move2
        for row_ele in move1:
            for col_ele in move2:
                if row_ele == row2 and col_ele == col2:
                    return True
        return False

    def check_rook(self, row1, col1, row2, col2):
        """
        using mathematical formulas, we will produce every
        possible and legal move the piece can make
        """
        l1 = [0, 1, 2, 3, 4, 5, 6, 7]

        for ele in l1:
            if row1 == row2 and col1 + ele == col2:  # row-none and column-up
                return True
            if row1 == row2 and col1 - ele == col2:  # row-none and column-down
                return True
            if col1 == col2 and row1 + ele == row2:  # column-none and row-up
                return True
            if col1 == col2 and row1 - ele == row2:  # column-none and row-down
                return True
        return False

    def check_bishop(self, row1, col1, row2, col2):
        """
        using mathematical formulas, we will produce every
        possible and legal move the piece can make
        """
        l1 = [0, 1, 2, 3, 4, 5, 6, 7]

        for ele in l1:
            if row1 + ele == row2 and col1 + ele == col2:  # upper-right diagonal
                return True
            if row1 - ele == row2 and col1 - ele == col2:  # lower-left diagonal
                return True
            if row1 + ele == row2 and col1 - ele == col2:  # upper-left diagonal
                return True
            if row1 - ele == row2 and col1 + ele == col2:  # lower-right diagonal
                return True
        return False

    def check_knight(self, row1, col1, row2, col2):
        """
        using mathematical formulas, we will produce every
        possible and legal move the piece can make
        """
        if row1 - 2 == row2 and col1 - 1 == col2:  # 2-down and 1-left
            return True
        if row1 - 2 == row2 and col1 + 1 == col2:  # 2-down and 1-right
            return True
        if row1 + 2 == row2 and col1 + 1 == col2:  # 2-up and 1-right
            return True
        if row1 + 2 == row2 and col1 - 1 == col2:  # 2-up and 1-left
            return True

        if row1 - 1 == row2 and col1 - 2 == col2:  # 2-left and 1-down
            return True
        if row1 - 1 == row2 and col1 + 2 == col2:  # 2-right and 1-down
            return True
        if row1 + 1 == row2 and col1 + 2 == col2:  # 2-right and 1-up
            return True
        if row1 + 1 == row2 and col1 - 2 == col2:  # 2-left and 1-up
            return True

        return False

    def check_obstruction_for_rook(self, row1, col1, row2, col2):
        """
        trace the exact path the piece took by subtracting
        the row and column of the beginning and last location
        and then locate any pieces on the way to validate move
        by iterating through those indices
        """
        if row2 - row1 > 0 and col2 - col1 == 0:  # moved upward
            for i in range(row1 + 1, row2):
                if self._liveBoard[i][col1] != '___':
                    return False
        if row2 - row1 < 0 and col2 - col1 == 0:  # moved downward
            for i in range(row2 + 1, row1):
                if self._liveBoard[i][col1] != '___':
                    return False
        if row2 - row1 == 0 and col2 - col1 < 0:  # moved leftward
            for i in range(col2 + 1, col1):
                if self._liveBoard[row1][i] != '___':
                    return False
        if row2 - row1 == 0 and col2 - col1 > 0:  # moved rightward
            for i in range(col1 + 1, col2):
                if self._liveBoard[row1][i] != '___':
                    return False
        return True

    def check_obstruction_for_bishop(self, row1, col1, row2, col2):
        """
        trace the exact path the piece took by subtracting
        the row and column of the beginning and last location
        and then locate any pieces on the way to validate move
        by iterating through those indices
        """
        if row2 - row1 > 0 and col2 - col1 > 0:  # moved upper-right diagonal
            for i in range(1, row2 - row1):
                if self._liveBoard[row1 + i][col1 + i] != '___':
                    return False
        if row2 - row1 < 0 and col2 - col1 < 0:  # moved lower-left diagonal
            for i in range(1, row1 - row2):
                if self._liveBoard[row1 - i][col1 - i] != '___':
                    return False
        if row2 - row1 < 0 < col2 - col1:  # moved lower-right diagonal
            for i in range(1, row1 - row2):
                if self._liveBoard[row1 - i][col1 + i] != '___':
                    return False
        if row2 - row1 > 0 > col2 - col1:  # moved upper-left diagonal
            for i in range(1, row2 - row1):
                if self._liveBoard[row1 + i][col1 - i] != '___':
                    return False
        return True

    def check_live_location(self, single_piece):
        """
        check the index location for our current piece
        """
        piece_row = 0
        piece_column = 0

        for row in self._liveBoard:
            for piece in row:
                if single_piece == piece:
                    piece_row = self._liveBoard.index(row)
                    piece_column = row.index(piece)
        return piece_row, piece_column

    def check_king_check(self, piece, row1, col1, row2, col2):
        """
        to validate a move we must run a simulation where
        we temporarily allow the current move to be made
        and every piece on the board is given an opportunity
        to make a legal attempt at capturing their enemy
        king allowing us to see if any king is left on check
        """
        king1_row, king1_col = None, None
        king2_row, king2_col = None, None

        # temporarily allow candidate move for simulation
        self._liveBoard[row1][col1] = "___"
        temp_piece = self._liveBoard[row2][col2]
        self._liveBoard[row2][col2] = piece

        # find indices of both kings for simulation
        for row in self._liveBoard:
            for piece_in_dim in row:
                if piece_in_dim[2] == 'K' and piece_in_dim[0] == piece[0]:
                    king1_row, king1_col = self.check_live_location(piece_in_dim)

                if piece_in_dim[2] == 'K' and piece_in_dim[0] != piece[0]:
                    king2_row, king2_col = self.check_live_location(piece_in_dim)

        # begin simulation
        for row in self._liveBoard:
            for other_piece_in_dim in row:

                # simulations for opponent's pieces
                if other_piece_in_dim[0] != piece[0]:

                    # Opponent's Rook
                    if other_piece_in_dim[2] == 'R':
                        other_piece_row, other_piece_col = self.check_live_location(other_piece_in_dim)
                        validate_rook = self.check_rook(other_piece_row, other_piece_col, king1_row, king1_col)
                        obstruction_check_rook = self.check_obstruction_for_rook(other_piece_row, other_piece_col,
                                                                                 king1_row, king1_col)

                        if validate_rook is True:
                            if obstruction_check_rook is True:
                                self._liveBoard[row2][col2] = temp_piece
                                self._liveBoard[row1][col1] = piece

                                return False

                    # Opponent's Bishop
                    if other_piece_in_dim[2] == 'B':
                        other_piece_row, other_piece_col = self.check_live_location(other_piece_in_dim)
                        validate_bishop = self.check_bishop(other_piece_row, other_piece_col, king1_row, king1_col)
                        obstruction_check_bishop = self.check_obstruction_for_bishop(other_piece_row, other_piece_col,
                                                                                     king1_row, king1_col)
                        if validate_bishop is True:
                            if obstruction_check_bishop is True:
                                self._liveBoard[row2][col2] = temp_piece
                                self._liveBoard[row1][col1] = piece

                                return False

                    # Opponent's Knight
                    if other_piece_in_dim[2] == 'N':
                        other_piece_row, other_piece_col = self.check_live_location(other_piece_in_dim)
                        validate_knight = self.check_knight(other_piece_row, other_piece_col, king1_row, king1_col)

                        if validate_knight is True:
                            self._liveBoard[row2][col2] = temp_piece
                            self._liveBoard[row1][col1] = piece

                            return False

                    # Opponent's King
                    if other_piece_in_dim[2] == 'K':
                        other_piece_row, other_piece_col = self.check_live_location(other_piece_in_dim)
                        validate_king = self.check_king(other_piece_row, other_piece_col, king1_row, king1_col)

                        if validate_king is True:
                            self._liveBoard[row2][col2] = temp_piece
                            self._liveBoard[row1][col1] = piece

                            return False

                # Simulations for current player's pieces
                if other_piece_in_dim[0] == piece[0]:

                    # Current player's Rook
                    if other_piece_in_dim[2] == 'R':
                        other_piece_row, other_piece_col = self.check_live_location(other_piece_in_dim)
                        validate_rook = self.check_rook(other_piece_row, other_piece_col, king2_row, king2_col)
                        obstruction_check_rook = self.check_obstruction_for_rook(other_piece_row, other_piece_col,
                                                                                 king2_row, king2_col)

                        if validate_rook is True:
                            if obstruction_check_rook is True:
                                self._liveBoard[row2][col2] = temp_piece
                                self._liveBoard[row1][col1] = piece

                                return False

                    # Current player's Bishop
                    if other_piece_in_dim[2] == 'B':
                        other_piece_row, other_piece_col = self.check_live_location(other_piece_in_dim)
                        validate_bishop = self.check_bishop(other_piece_row, other_piece_col, king2_row, king2_col)
                        obstruction_check_bishop = self.check_obstruction_for_bishop(other_piece_row, other_piece_col,
                                                                                     king2_row, king2_col)
                        if validate_bishop is True:
                            if obstruction_check_bishop is True:
                                self._liveBoard[row2][col2] = temp_piece
                                self._liveBoard[row1][col1] = piece

                                return False

                    # Current player's Knight
                    if other_piece_in_dim[2] == 'N':
                        other_piece_row, other_piece_col = self.check_live_location(other_piece_in_dim)
                        validate_knight = self.check_knight(other_piece_row, other_piece_col, king2_row, king2_col)

                        if validate_knight is True:
                            self._liveBoard[row2][col2] = temp_piece
                            self._liveBoard[row1][col1] = piece

                            return False

                    # Current player's King
                    if other_piece_in_dim[2] == 'K':
                        other_piece_row, other_piece_col = self.check_live_location(other_piece_in_dim)
                        validate_king = self.check_king(other_piece_row, other_piece_col, king2_row, king2_col)

                        if validate_king is True:
                            self._liveBoard[row2][col2] = temp_piece
                            self._liveBoard[row1][col1] = piece

                            return False

        # No king was captured in simulation, thus not in check
        self._liveBoard[row2][col2] = temp_piece
        self._liveBoard[row1][col1] = piece
        return True

    def check_location(self, current, new):
        """
        simultaneously check the indices of the current
        location and new location to validate whether
        the user is picking a correct piece at a valid
        location to be subsequently moved at an also
        valid location on the live board
        """
        current_counter = 0
        new_counter = 0

        # if current location input is found in reference board increment counter
        for rowC in self._referenceBoard:
            for posC in rowC:
                if posC == current:
                    current_counter += 1

        # if new location input is found in reference board increment counter
        for rowN in self._referenceBoard:
            for posN in rowN:
                if posN == new:
                    new_counter += 1

        # if both locations found both counters should display 1 validating locations
        if current_counter == 1 and new_counter == 1:
            return True
        else:
            return False

    def check_for_winner(self):
        """
        occurring after every move, checking game
        for a winner or tie occurs here by iterating
        over the live board
        """
        finish_line_count = 0
        winner_initials = []
        finish_line = self._liveBoard[0]
        for cell in finish_line:
            if cell[2] == 'K':
                finish_line_count += 1
                winner_initials.append(cell[0])
        if (self._check_for_player % 2) == 0:
            if 'W' in winner_initials and 'B' in winner_initials:
                print("TIE")
                return False
            if 'W' in winner_initials and 'B' not in winner_initials:
                print("WHITE_WON")
                return False
            if 'W' not in winner_initials and 'B' in winner_initials:
                print("BLACK_WON")
                return False
            else:
                return True
        else:
            return True

    def make_move(self, current_pos, new_pos):
        """
        this method is the heart of the program where all validations of
        moves and modifications of the live board corresponding to the
        move are made
        """
        # Validate if input locations are valid:
        location_results = self.check_location(current_pos, new_pos)
        if location_results is True:

            # Convert chess board dimensions into indices:
            cur_row_index, cur_col_index, new_row_index, new_col_index = self.find_index(current_pos, new_pos)
            current_piece = self._liveBoard[cur_row_index][cur_col_index]
            new_location = self._liveBoard[new_row_index][new_col_index]

            # Validate if square has a piece:
            if current_piece == '___':
                print("Invalid move, no chess piece found in that location.")

            # Validate move if Rook:
            if current_piece[2] == "R":
                check_player = self._check_for_player
                validate_rook = self.check_rook(cur_row_index, cur_col_index, new_row_index, new_col_index)
                obstruction_check_rook = self.check_obstruction_for_rook(cur_row_index, cur_col_index,
                                                                         new_row_index,
                                                                         new_col_index)

                # validate if current piece matches current player
                if ((check_player % 2) == 0 and current_piece[0] == 'W') or (
                        (check_player % 2) > 0 and current_piece[0] == 'B'):
                    # validate Rook can execute the move
                    if validate_rook is True:
                        # validate Rook wasn't jumping over any piece
                        if obstruction_check_rook is True:
                            check_king_check = self.check_king_check(current_piece, cur_row_index, cur_col_index,
                                                                     new_row_index,
                                                                     new_col_index)
                            # validate move wouldn't leave any king in check
                            if check_king_check is True:
                                # validate player's piece will not land on another player's piece
                                if current_piece[0] != new_location[0]:
                                    self._liveBoard[cur_row_index][cur_col_index] = "___"
                                    self._liveBoard[new_row_index][new_col_index] = current_piece

                                    # Even value means current player is WHITE
                                    if (check_player % 2) == 0:
                                        print("Player WHITE just moved.")
                                        self._check_for_player += 1
                                    # Odd value means current player is BLACK
                                    else:
                                        print("Player BLACK just moved.")
                                        self._check_for_player += 1
                                        self.check_for_winner()
                                else:
                                    print("Invalid move, you have a piece in that desired location.")
                            else:
                                print("Invalid move, a king would have been left in check.")
                        else:
                            print("Invalid move, your rook is not allowed to jump over pieces.")
                    else:
                        print("Invalid move, Rook is not allowed to execute that movement.")
                else:
                    print("Invalid move, you are attempting to move opponent's piece.")

            # Validate move if piece is Bishop:
            if current_piece[2] == 'B':
                check_player = self._check_for_player
                validate_bishop = self.check_bishop(cur_row_index, cur_col_index, new_row_index, new_col_index)
                obstruction_check_bishop = self.check_obstruction_for_bishop(cur_row_index, cur_col_index,
                                                                             new_row_index, new_col_index)
                # validate if current piece matches current player
                if ((check_player % 2) == 0 and current_piece[0] == 'W') or (
                        (check_player % 2) > 0 and current_piece[0] == 'B'):
                    # validate Bishop can execute the move
                    if validate_bishop is True:
                        # validate Bishop wasn't jumping over any piece
                        if obstruction_check_bishop is True:
                            check_king_check = self.check_king_check(current_piece, cur_row_index, cur_col_index,
                                                                     new_row_index,
                                                                     new_col_index)
                            # validate move wouldn't leave any king in check
                            if check_king_check is True:
                                # validate player's piece will not land on another player's piece
                                if current_piece[0] != new_location[0]:
                                    self._liveBoard[cur_row_index][cur_col_index] = "___"
                                    self._liveBoard[new_row_index][new_col_index] = current_piece

                                    # Even value means current player is WHITE
                                    if (check_player % 2) == 0:
                                        print("Player WHITE just moved.")
                                        self._check_for_player += 1

                                    # Odd value means current player is BLACK
                                    else:
                                        print("Player BLACK just moved.")
                                        self._check_for_player += 1
                                        self.check_for_winner()
                                else:
                                    print("Invalid move, you have a piece in that desired location.")
                            else:
                                print("Invalid move, a king would have been left in check.")
                        else:
                            print("Invalid move, your bishop is not allowed to jump over pieces.")
                    else:
                        print("Invalid move, Bishop is not allowed to execute that movement.")
                else:
                    print("Invalid move, you are attempting to move opponent's piece.")

            # Validate move if piece is Knight:
            if current_piece[2] == 'N':
                check_player = self._check_for_player
                validate_knight = self.check_knight(cur_row_index, cur_col_index, new_row_index, new_col_index)

                # validate if current piece matches current player
                if ((check_player % 2) == 0 and current_piece[0] == 'W') or (
                        (check_player % 2) > 0 and current_piece[0] == 'B'):
                    # validate Knight can execute the move
                    if validate_knight is True:
                        check_king_check = self.check_king_check(current_piece, cur_row_index, cur_col_index,
                                                                 new_row_index,
                                                                 new_col_index)
                        # validate move wouldn't leave any king in check
                        if check_king_check is True:
                            # validate player's piece will not land on another player's piece
                            if current_piece[0] != new_location[0]:
                                self._liveBoard[cur_row_index][cur_col_index] = "___"
                                self._liveBoard[new_row_index][new_col_index] = current_piece

                                # Even value means current player is WHITE
                                if (check_player % 2) == 0:
                                    print("Player WHITE just moved.")
                                    self._check_for_player += 1

                                # Odd value means current player is BLACK
                                else:
                                    print("Player BLACK just moved.")
                                    self._check_for_player += 1
                                    self.check_for_winner()
                            else:
                                print("Invalid move, you have a piece in that desired location.")
                        else:
                            print("Invalid move, a king would have been left in check.")
                    else:
                        print("Invalid move,Knight is not allowed to execute that movement.")
                else:
                    print("Invalid move, you are attempting to move opponent's piece.")

            # Validate move if piece is King:
            if current_piece[2] == 'K':
                check_player = self._check_for_player
                validate_king = self.check_king(cur_row_index, cur_col_index, new_row_index, new_col_index)
                # validate if current piece matches current player
                if ((check_player % 2) == 0 and current_piece[0] == 'W') or (
                        (check_player % 2) > 0 and current_piece[0] == 'B'):
                    # validate King can execute the move
                    if validate_king is True:
                        check_king_check = self.check_king_check(current_piece, cur_row_index, cur_col_index,
                                                                 new_row_index,
                                                                 new_col_index)
                        # validate move wouldn't leave any king in check
                        if check_king_check is True:
                            # validate player's piece will not land on another player's piece
                            if current_piece[0] != new_location[0]:
                                self._liveBoard[cur_row_index][cur_col_index] = "___"
                                self._liveBoard[new_row_index][new_col_index] = current_piece

                                # Even value means current player is WHITE
                                if (check_player % 2) == 0:
                                    print("Player WHITE just moved.")
                                    self._check_for_player += 1

                                # Odd value means current player is BLACK
                                else:
                                    print("Player BLACK just moved.")
                                    self._check_for_player += 1
                                    self.check_for_winner()
                            else:
                                print("Invalid move, you have a piece in that desired location.")
                        else:
                            print("Invalid move, a king would have been left in check.")
                    else:
                        print("Invalid move, King is not allowed to execute that movement.")
                else:
                    print("Invalid move, you are attempting to move opponent's piece.")

        # if location input validations came back False
        else:
            print("Invalid move, location does not exist.")


def ChessUI():
    chess_obj = ChessVar()
    chess_obj.display_live_board()
    print("Player white first.")
    check_for_winner = True

    while check_for_winner:
        current_square = str(input("Choose your piece: "))
        new_square = str(input("Choose new square: "))
        chess_obj.make_move(current_square, new_square)
        check_for_winner = chess_obj.check_for_winner()
        chess_obj.display_live_board()
    print("Game Over")


if __name__ == "__main__":
    ChessUI()
