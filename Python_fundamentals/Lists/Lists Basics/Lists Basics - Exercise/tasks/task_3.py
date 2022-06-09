team_A = 11
team_B = 11
cards_team_A = []
cards_team_B = []
cards_input = input().split()

for red_cards in cards_input:
    team, player = red_cards.split('-')
    player = int(player)

    if team == 'A':
        if player in cards_team_A:
            continue
        team_A -= 1
        cards_team_A.append(player)

    elif team == 'B':
        if player in cards_team_B:
            continue
        team_B -= 1
        cards_team_B.append(player)

print(f"Team A - {team_A}; Team B - {team_B}")

if team_A < 7 or team_B < 7:
    print('Game was terminated')


# # # # solution with function

team_A = 11
team_B = 11
cards_team_A = []
cards_team_B = []
cards_input = input().split()


def remove_player(player, team, red_card_player):
    if player in red_card_player:
        return team
    team -= 1
    red_card_player.append(player)
    return team


for red_cards in cards_input:
    team, player = red_cards.split('-')
    player = int(player)

    if team == 'A':
        team_A = remove_player(player, team_A, cards_team_A)

    elif team == 'B':
        team_B = remove_player(player, team_B, cards_team_B)

print(f"Team A - {team_A}; Team B - {team_B}")

if team_A < 7 or team_B < 7:
    print('Game was terminated')
