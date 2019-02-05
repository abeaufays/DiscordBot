width = 7
height = 6
connection_needed = 4

player_sign = [":heart:", ":blue_heart:"]

current_game = None

class game(object):
    def game(self):
        self.grid = [[] for x in range(width)]
        self.player = []


    def play(self, user, play):
        if len(self.player) < 2:
            self.player.append(user)

        if user in self.player: 
            self.grid[play].append( player_sign[ self.player.index(user) ] )
            if self.is_winning_move(user,play):
                self.end_game()

    def end_game(self):
        current_game = None

    def is_winning_move(self, user, play):
        sign = player_sign[ self.player.index(user) ]
        level = len(self.grid[play]) -1 

        buffer = 0
        for i in self.grid[play]:
            if test(i,sign, buffer)
                return True
        buffer = 0
        for i in range(width):
            if test(self.grid[i].get(level), sign,buffer):
                return True

        buffer = 0
        w_parse = range( max(0, play-level), min(width, play+level) )
        h_parse = range( max(0, level-play), min(height, level + (width-play)))

        for i, j in zip(w_parse, h_parse):
            if test(self.grid[i][j], sign, buffer):
                return True

        buffer = 0

        for i, j in zip(w_parse, reversed(h_parse)):
            if test(self.grid[i][j], sign, buffer):
                return True


        return False

    @staticmethod
    def test(element,sign):
        if element == sign:
            buffer += 1
        else 
            buffer = 0
        if buffer == 4:
            return True
        

