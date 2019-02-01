from random import sample
from itertools import product


number_of_bombs = 6
number_of_lines = 8
number_of_rows = 8
CountEmoji = ['       ',':one:',':two:',':three:',':four:',':five:',':six:',':seven:',':eight:']

grid = [x for x in product(range(0,number_of_lines), range(0,number_of_rows))]
bombs = sample(grid, number_of_bombs)

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

output = ''
for i in range(number_of_lines):
    for j in range(number_of_rows):
        output += '||'
        if((i,j) in bombs):
            output += ':boom:'
        else:
            output += CountEmoji[count_neighboors((i,j), bombs)]
        output += '||'
    output += '\n'
print(output)