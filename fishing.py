    #Рыбалка
    #Задачи:случайные рыбы, степени редкости: обычная, редкая, легендарная, эпическая.
#import os
#os.startfile (r'F:\Codes\WORK\map.png') # ВАЖНО НЕ ЗАБУДЬ СКОПИРОВАТЬ, А ПОТОМ УДАЛИТЬ
errors = 0
fishing_perk_stat = 0
fishing_perk = input()
if fishing_perk == 'cheat':
    fishing_perk_stat += 5
import random
player_power = 10        #Удалить

fish_luck = 1
while fish_luck != 0:
    fish_type = random.randint(1, 4)
    fish_rare = random.randint(1, 100)
    if fish_type == 1:
        fish_name = " окунь "
    elif fish_type == 2:
        fish_name = " треска "
    elif fish_type == 3:
        fish_name = " сом "
    else:
        fish_name = " щука "
    if fish_rare > 0 and fish_rare < 51 - (fishing_perk_stat*3):
        if fish_type == 3 or fish_type == 1:
            fish_rare_type = " обычный "
        elif fish_type == 2 or fish_type == 4:
            fish_rare_type = "обычная"
    elif fish_rare > 50 - (fishing_perk_stat * 3) and fish_rare <76 - (fishing_perk_stat*2):
        if fish_type == 3 or fish_type == 1:
            fish_rare_type = "редкий"
        elif fish_type == 2 or fish_type == 4:
            fish_rare_type = "редкая"
    elif fish_rare > 75 - (fishing_perk_stat * 2) and fish_rare <96 - fishing_perk_stat:
        if fish_type == 3 or fish_type == 1:
            fish_rare_type = "легендарный"
        elif fish_type == 2 or fish_type == 4:
            fish_rare_type = "легендарная"
    else:
        if fish_type == 3 or fish_type == 1:
            fish_rare_type = "эпический"
        elif fish_type == 2 or fish_type == 4:
            fish_rare_type = "эпическая"
        else:
            errors+=1
    print( 'Ты поймал рыбу! Это:', fish_rare_type, fish_name)
    fish = [fish_rare_type, fish_name]
    inventory = ['молот', 'зелье']         #удалить
    inventory.append (fish)
    print('Твой инвентарь:', *list(inventory))
    fish_luck = 0

