class Cell:
    def __init__(self, x, y):
        self.north = None
        self.east = None
        self.west = None
        self.south = None
        self.x = x
        self.y = y

    def get_neighbors(self):
        a_set = []
        if self.north is None:
            a_set.append(0)
        if self.south is None and self.y -2 >= 0:
            a_set.append(1)
        if self.east is None:
            a_set.append(2)
        if self.west is None and self.x - 2 >= 0:
            a_set.append(3)
        return a_set
