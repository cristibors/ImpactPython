from operator import truediv

fighters =[]
header_power = 10
class characters():
    name='Valera'
    hp = 0
    armor = 0
    power = 0
    def __init__(self, name, hp, armor, power):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.power = power

class game(characters):
    def heal(self):
        global heal_power
        self.hp += heal_power
        print(self.name + 'have', self.hp,'hp left')

def attacked(self,damage):
        if self. hp- damage > 0:
            self. hp -= damage
            print(self.name+'have', self.hp, 'hp left')
            return True
        else:
          print(self.name, 'is death')
        return  False
while 1:
    try:
        nr = int(input('how many personage are in gone?'))
        break

    except:
          print('wrong date type')
          continue

for i in range (0, nr):
    name = imput('name:')
    hp = int

for 1 in range(0, nr):
    name = imput ('name')
    hp= int(imput('armor:'))
    armor= int(imput('armor:'))
    power= int(input('power'))
    fighters.append(game(name,hp,armor,power))

alive= true
player1 = figthers [0]
player2 = fighters [1]

cur_player= player1
next_player = player2

whyle alive

print('turn to chose for', cur_player. name)
print('enter 1 for attack other player')
print('enter 2 for haell')
move = int(imput())

if move == 1:
    alive = next_player.attacked( cur_player.power)
alif move ==2:
    cur_player.heal()
alif move == 3:
 continue
