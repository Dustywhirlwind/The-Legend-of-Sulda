from Colores import *
player_hp = 100
player_atk = 10

print('Вы хотите начать игру или тренировку?')
error = 0
yellow_с('Если хотите начать тренировку напишите "t" если хотите начать полную игру напишите "g"')
menu = input()

if menu == 't':
    white('Вы появляетесь в симуляции, вокруг вас пустота. Преред вами есть небольшой шкафчик.')
    yellow_с('Чтобы открыть его напишите "e"')
    player_action = input()
    if player_action == 'e':
        white('Вы открываете его, внутри лежат рваные тряпки очень похожие на одежду и старый деревянный меч')
        yellow_с('Напишите "f" чтобы взять содержимое  сундука ')
        player_action = input()
        if player_action == 'f':
            white('Вы собираете всё что находилось внутри себе.')
            white('Сейчас вы обнаруживаете полное отсутстивие одежды на себе')
            lightblue('Не стоит ходить голышом, всё таки тут довольно холодно'), white('Думаете вы про себя')
            yellow_с('Откройте инвентарь на кнопку "i"')
            player_action = input()
            if player_action == "i":
                print("Здоровье:", player_hp)
                print("Сила:", player_atk)
            white('Вдруг перед вами, из-под земли появляется  табличка, на ней есть надпись:')
            white('"Пройдись вверх"')
            yellow_с('Напишите "u"')
        else:
            error += 1
    else:
        error += 1
    motion = input()
    if motion == 'u':
        white('Вы немного прошлись, но так ничего и не изменилось. Вы почувствовали тревогу. Кажется кто-то или что-то'
              ' наблюдает за вами.')
        yellow_с('Напишите "d" чтобы пойти назад')
        motion = input()
        if motion == 'd':
            white('Обернувшись вы заметили, позади показался силует. Он выглядит как человек, но он или оно выглятит '
                  'значительно выше, чем обычный человек.')
            white('"Мне нужно подойти поближе" говорите вы себе')
