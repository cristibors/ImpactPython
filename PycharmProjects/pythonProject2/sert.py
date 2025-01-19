from multiprocessing.managers import Value
from tabnanny import check


def print_tac_toe(values):
    print("\n")
    print('\t     |     |' )
    print("\t  {}   |   {}  |   {}".format(values[0], values[1], values[2]))
    print("\t_____|_____|_____")


    print('\t     |     |')
    print("\t  {}   |   {}  |   {}".format(values[3], values[4], values[5]))
    print("\t_____|_____|_____")

    print('\t     |     |')

    print("\t  {}   |   {}  |   {}".format(values[6], values[7], values[8]))
    print('\t     |     |')
    print("\n")

def single_game(cur_player):
    values = ["" for x in range(9)]
    player_pos = {"x" : [], "0" : []}


print_tac_toe(["" for x in range(9)])

while True:
    print_tac_toe(values)

 try:
     print("player", cur_player, " turn. which box? : ", end="")
     move = int(imput())
 except ValueError:
     print("Wrong input!!! Try again")
     continue

if move < 1 or move > 9:
    print("Wrong imput!!! try Again")
    continue

if values[move - 1] != " ":
    print("place already filled. try!!")
    continue

    values[move - 1] = cur_player

    player_pos[cur_player]. append(move)

def check_win(player_pos, cur_player):
    soln=[[1, 2, 3,], [4, 5, 6,], [7, 8, 9],
          [1, 4, 7], [2,5,8], [3, 6, 9],
          [1, 5, 9], [3, 5, 7]]

    for x in soln
        if all(y in player_pos[cur_player]for y in x)

            return True

return False

if check_win(player_pos, cur_player)
