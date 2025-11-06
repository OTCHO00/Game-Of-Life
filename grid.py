from config import NB_LIGNES, NB_COLONNES

class Grid:
    def __init__(self):
        self.row = NB_LIGNES
        self.cols = NB_COLONNES
        self.cels = set()
        self.generation = 0

    def get_cels(self):
        return self.cels

    def get_cell(self, row, col):

        if (row, col) in self.cels:
            return True
        else:
            return False

    def set_cell(self, row, col, state):
        
        if (row, col) in self.cels and not state:
            self.cels.discard((row, col))
        
        if (row, col) not in self.cels and state:
            self.cels.add((row, col))

    def toggle_cel(self, row, col):

        if (row, col) in self.cels:
            self.cels.discard((row, col))
        
        else:
            self.cels.add((row, col))
    
    def count_neighbors(self, row, col):

        nb_voisins = 0
        directions = [
            (-1, 0),
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, -1),
            (1, 1),
            (-1, +1),
            (1, -1),
        ]

        for (x, y) in directions:
            r, c = (row + x, col + y)
            if 0 <= r < self.row and 0 <= c < self.cols and (r, c) in self.cels:
                nb_voisins += 1
        
        return nb_voisins
    
    def apply_rules(self, row, col, nb_voisins):
        
        if self.get_cell(row, col):
            if nb_voisins == 0 or nb_voisins == 1 or nb_voisins >= 4:
                return False
            if nb_voisins == 2 or nb_voisins == 3:
                return True
        else:
            if nb_voisins == 3:
                return True
            else:
                return False
    
    def insert_patterns(self, pattern, start_row, start_col):
        
        for (x, y) in pattern:

            row = start_row + x
            col = start_col + y

            if 0 <= row < self.row and 0 <= col < self.cols:
                self.cels.add((row, col))

    def count_alive(self):

        return len(self.cels)
    
    def clear(self):

        self.generation = 0
        self.cels.clear()

    def update(self):

        new_cels = set()

        for x in range(0, self.row):
            for y in range(0, self.cols):

                nb_voisins = self.count_neighbors(x, y)
                if self.apply_rules(x, y, nb_voisins):
                    new_cels.add((x, y))
        
        self.cels = new_cels
        self.generation += 1
