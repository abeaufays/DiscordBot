import itertools

width = 7
height = 6
connection_needed = 4

player_sign = [":heart:", ":blue_heart:"]

current_game = None

def play(user, play):
    if current_game is None:
        current_game = Game()
    return current_game.play(user,play)


class Game(object):
    def Game(self):
        self.grid = [[] for x in range(width)]
        self.player = []


    def play(self, user, play):
        if len(self.player) < 2:
            self.player.append(user)

        if user in self.player: 
            self.grid[play].append( player_sign[ self.player.index(user) ] )
            if is_winning_move(self.grid, player_sign[ self.player.index(user) ], play):
                self.end_game()

    def end_game(self):
        current_game = None
    
def is_winning_move(grid, sign, play):
    level = len(grid[play]) -1 
    if level < 0:
        return False
    buffer = 0
    for i in grid[play]:
        if i == sign:
            buffer += 1
        else:
            buffer = 0
        if buffer == 4:
            return True
    buffer = 0
    for i in range(width):
        if grid[i][level] if level < len(grid[i]) else None == sign:
            buffer += 1
        else:
            buffer = 0
        if buffer == 4:
            return True

    w_parse = range( max(0, play-level), min(width, play+height) )
    h_parse = range( max(0, level-play), min(height, level + (width-play)))

    buffer = 0
    for i, j in zip(w_parse, h_parse):
        if grid[i][j] if j < len(grid[i]) else None == sign:
            buffer += 1
        else:
            buffer = 0
        if buffer == 4:
            return True


    rw_parse = range( max(0, play-height + level), min(width, play+height) )
    rh_parse = range( min(level+play, height), max(0, level - (width-play)) -1, -1)
    buffer = 0
    for i, j in zip(rw_parse, rh_parse):
        if grid[i][j] if j < len(grid[i]) else None == sign:
            buffer += 1
        else:
            buffer = 0
        if buffer == 4:
            return True
    return False


def get_string(grid):
    lines = ["" for x in range(height)]
    for col in grid:
        for value, index in itertools.zip_longest(col, range(height), fillvalue=' '):
            lines[index] = lines[index] + value
    return lines
    
