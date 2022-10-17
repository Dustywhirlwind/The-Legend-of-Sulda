player_position_X = 0
player_position_Y = 0
fin = 0
error = 0
while fin == 0:
    player_motion = input()
    if player_motion == 'вверх':
        player_position_Y += 1
        print(player_position_X, player_position_Y)
    elif player_motion == 'вниз':
        player_position_Y -= 1
        print(player_position_X, player_position_Y)
    elif player_motion == 'вправо':
        player_position_X += 1
        print(player_position_X, player_position_Y)
    elif player_motion == 'влево':
        player_position_X -= 1
        print(player_position_X, player_position_Y)
    else:
        error += 1

