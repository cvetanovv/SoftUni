team_a = []
team_b = []

for i in range(1, 12):
    team_a.append(f"A-{i}")
    team_b.append(f"B-{i}")

sent_off_players = input().split()
team_a_red_cards_counter = 0
team_b_red_cards_counter = 0
isterminated = False

for player in sent_off_players:
    if player in team_a:
        team_a.remove(player)
        team_a_red_cards_counter += 1
    if player in team_b:
        team_b.remove(player)
        team_b_red_cards_counter += 1
    if team_a_red_cards_counter == 5 or team_b_red_cards_counter == 5:
        isterminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if isterminated:
    print("Game was terminated")