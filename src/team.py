class Team:

    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
    
    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_name):
        for player in self.players:
            if player_name == player:
                return True
        else:
            return False

    def play_game(self, has_won):
        if has_won == True:
            self.points += 3
        elif has_won == False:
            self.points += 0