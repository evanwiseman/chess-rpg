

class Player:
    def __init__(self, name: str):
        self.name = name
        self.pieces = []
        self.taken_pieces = []
        self.lost_pieces = []
        self.gold = 0
        self.wins = 0
        self.losses = 0
