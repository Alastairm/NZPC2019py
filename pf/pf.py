import sys
lines = []
for _line in sys.stdin:
    stripped = _line.strip()
    if not stripped: break
    lines.append(stripped)

n = lines[0]

Colour = ['R', 'G', 'B']
Shape = ['D', 'O', 'S']
Number = ['1', '2', '3']
Fill = ['F', 'S', 'E']

for line in lines[1:]:
    Colour = ['R', 'G', 'B']
    Shape = ['D', 'O', 'S']
    Number = ['1', '2', '3']
    Fill = ['F', 'S', 'E']

    card1, card2 = line.split()