def easy_ai(board):
    moves = [Move(coords) for coords in get_moves(board)]

    for m in moves:
        m.set_features(board)
        m.set_advanced_features(board)
        m.set_value()

    best_value = max([m.value for m in moves])
    best_moves = [m for m in moves if m.value == best_value]
    return choice(best_moves).coords




value_set = {
    "rank up": 1,
    "jump": 3,
    "king jump": 5,
    "king me": 5,
    "open back": -10
}

advanced_value_set = {
    "seeking": 1,
    "forethought": 0            # Dynamic
}


class Move:
    def __init__(self, coords):
        self.coords = coords
        
        self.value = 0
        
        self.features = dict([(key, False) for key in value_set.keys()])
        self.advanced_features = dict([(key, False) for key in advanced_value_set.keys()])

    def set_value(self):
        for key in features.keys():
            if self.features[key]:
                self.value += value_set[key]
        for key in advanced_features.keys():
            if self.advanced_features[key]:
                self.value += advanced_value_set[key]
