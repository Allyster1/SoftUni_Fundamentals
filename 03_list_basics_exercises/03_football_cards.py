my_list = [f"A-{number}" for number in range(1,12)]
my_list = [f"B-{number}" for number in range(1,12)]
team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
is_terminated = False

players = input().split()

for player in players:
    # if the player is found in the team, remove him
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    # if a team has less than 7 players, break
    if len(team_a) < 7 or len(team_b) < 7:
        is_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if is_terminated:
    print("Game was terminated")