class BaseballTeam:
    def __init__(self):
        self.players = set()

    def add_player(self, player):
        self.players.add(player)
    
    def remove_player(self, player):
        self.players.remove(player)

    