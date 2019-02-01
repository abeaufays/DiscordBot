from random import sample
from itertools import product


count_emoji = ['       ',':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:']


def count_neighboors(pos, bombs):
    neighboors = [(pos[0] - 1, pos[1] - 1),
                  (pos[0] - 1, pos[1]),
                  (pos[0], pos[1] - 1),
                  (pos[0] + 1, pos[1] + 1),
                  (pos[0], pos[1] + 1),
                  (pos[0] + 1, pos[1]),
                  (pos[0] + 1, pos[1] - 1),
                  (pos[0] - 1, pos[1] + 1)]
    return sum([(i in bombs) for i in neighboors])



def get_minesweeper(nb_bombs, nb_lines, nb_rows):
    grid = [x for x in product(range(0,nb_lines), range(0,nb_rows))]
    bombs = sample(grid, nb_bombs)
    output = ''
    for i in range(nb_lines):
        for j in range(nb_rows):
            output += '||'
            if((i,j) in bombs):
                output += ':boom:'
            else:
                output += count_emoji[count_neighboors((i,j), bombs)]
            output += '||'
        output += '\n'
    return output