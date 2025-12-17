from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací možné tahy pěšáka (pouze pohyb o 1 vpřed).
        """
        row, col = self.position
        moves = []

        # Určení směru: Bílý (white) jde nahoru (+1), Černý (black) dolů (-1)
        direction = 1 if self.color == 'white' else -1
        
        # Pěšák se hýbe o jedno pole vpřed (změna pouze v řádku)
        next_pos = (row + direction, col)

        if self.is_position_on_board(next_pos):
            moves.append(next_pos)

        return moves
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací možné tahy střelce (diagonály).
        """
        row, col = self.position
        moves = []
        # Směry diagonál: (row_change, col_change)
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            # Střelec může jít o 1 až 7 polí, dokud nenarazí na konec desky
            for i in range(1, 8):
                new_pos = (row + (dr * i), col + (dc * i))
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break # Pokud jsme mimo desku, v tomto směru dál nejdeme
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací možné tahy věže (vertikálně a horizontálně).
        """
        row, col = self.position
        moves = []
        # Směry: nahoru, dolů, doprava, doleva
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            for i in range(1, 8):
                new_pos = (row + (dr * i), col + (dc * i))
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací možné tahy dámy (kombinace věže a střelce).
        """
        row, col = self.position
        moves = []
        # Dáma se hýbe všemi 8 směry
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),   # Jako věž
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Jako střelec
        ]

        for dr, dc in directions:
            for i in range(1, 8):
                new_pos = (row + (dr * i), col + (dc * i))
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Vrací možné tahy krále (jedno pole všemi směry).
        """
        row, col = self.position
        # Král se může pohnout o 1 pole do 8 směrů
        potential_moves = [
            (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1), 
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        
        final_moves = []
        for move in potential_moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    # Testování figur
    print("--- Knight (Jezdec) ---")
    knight = Knight("black", (1, 2))
    print(knight)
    print(knight.possible_moves())

    print("\n--- Pawn (Pěšák - bílý) ---")
    white_pawn = Pawn("white", (2, 2))
    print(white_pawn) # Očekáváno: (3, 2)
    print(white_pawn.possible_moves())

    print("\n--- Pawn (Pěšák - černý) ---")
    black_pawn = Pawn("black", (7, 2))
    print(black_pawn) # Očekáváno: (6, 2)
    print(black_pawn.possible_moves())

    print("\n--- King (Král) ---")
    king = King("white", (5, 5))
    print(king)
    print(king.possible_moves()) # Očekáváno: 8 okolních polí

    print("\n--- Queen (Dáma) ---")
    queen = Queen("black", (4, 4))
    print(queen)
    print(f"Počet tahů dámy ze středu: {len(queen.possible_moves())}") # Očekáváno: 27 tahů