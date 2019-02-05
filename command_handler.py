
from demineur import get_minesweeper

def handle(message):
    command = message.content.split()
    if command[0] == "!mine":
        try:
            return get_minesweeper(int(command[1]), int(command[2]), int(command[3]))
        except:
            return "Usage : !mine [nb bombs] [nb line] [nb rows]"

    