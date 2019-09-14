import sys
lines = []
for _line in sys.stdin:
    stripped = _line.strip()
    if not stripped: break
    lines.append(stripped)

team1_name = lines[0]
team2_name = lines[1]

scores = lines[2].split()
scores = [int(x) for x in scores]
shots = int(lines[3])
moves = lines[4]

active_team = 0

for i in range(shots):
    move = moves[i]
    if move in ['H', 'P']:
        scores[active_team] += 1
    if move == 'M':
        active_team += 1
        active_team = active_team % 2

print(f"{team1_name} {scores[0]} {team2_name} {scores[1]}")