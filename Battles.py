'''
боёвка и враги. Задачи: рандомайзер врагов(выполнено),
учёт урона(выполнено частично), дроп в виде монеток (1-10) (выполнено)
'''
player_hp = 100           #не забудь убрать
player_atk = 10           #не забудь убрать
import random
def lightblue(text):
    print("\033[36m {}" .format(text))
player_price = 0
inventory = ['1', 'зелье здоровья']
character = ['удачливый рыбак']
cheat = input()
if cheat == 'cheat':
    character.append('боец')
    player_atk += 5
    #не забудь убрать
enemy_type = random.randint(1, 5)
enemy_hp = 0
enemy_atk = 0
player_action = 0
player_bank = 0

if enemy_type == 1:
    enemy_name = "орка"
    enemy_hp += 20
    enemy_atk += 10

elif enemy_type == 2:
    enemy_name = 'гнома'
    enemy_hp += 25
    enemy_atk += 7

elif enemy_type == 3:
    enemy_name = 'бандита'
    enemy_hp += 15
    enemy_atk += 5

elif enemy_type == 4:
    enemy_name = 'дикого зверя'
    enemy_hp += 10
    enemy_atk += 10

elif enemy_type == 5:
    enemy_name = 'живое растение'
    enemy_hp += 5
    enemy_atk += 10
else:
    enemy_name = 0
print('Вы встретили на пути', enemy_name)

while enemy_hp > 0 and player_hp > 0:

   print('1.Атака 2.Инвентарь 3.Побег')
   player_action = int(input())
   if player_action == 3:
       luck = random.randint(0, 1)
       if luck == 1:
           print('Удачный побег')
           enemy_hp = 0
       elif luck == 0:
           print('Неудача')
           player_hp -= enemy_atk


   elif player_action == 1:
        enemy_hp -= player_atk
        player_hp -= enemy_atk

        print('Получено', enemy_atk, 'единиц урона')# +подробности
        if enemy_hp < 0:
            enemy_hp = 0
        else:
            print('Здоровье врага:', enemy_hp)

   elif player_action == 2:
        print(inventory)
        player_action = input()
        if player_action == 'зелье здоровья':
              if 'зелье здоровья' in inventory:
                  player_hp += 35
                  player_hp -= enemy_atk
                  print('Здоровье игрока', '\033[')
        elif 'зелье здоровья' not in inventory:
            print('нет предмета')

   else:
       print('Ошибка в вводе или пустой ввод ')
   print('здоровье игрока', player_hp)

if player_hp < 0:
    print('Конец игры')

elif enemy_hp == 0:
    player_prize = random.randint(1, 10)
    player_bank += player_prize
    if player_price == 1:
        print('Победа в бою. Заработанa', '\033[33m', player_prize, '\033[0m', "монетa")     #нужно больше узнать по этому поводу
    elif 1 < player_price < 5:
        print('Победа в бою. Заработано', '\033[33m', player_prize, '\033[0m', 'монеты')
    else:
        print('Победа в бою. Заработанo', '\033[33m', player_prize, '\033[0m', 'монет')
    player_prize = 0