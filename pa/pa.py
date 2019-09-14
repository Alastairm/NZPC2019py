import sys
lines = []
for _line in sys.stdin:
    stripped = _line.strip()
    if not stripped: break
    lines.append(stripped)


def carpark(n, day1, day2):
    out = 0
    for i in range(int(n)):
        if day1[i] == 'O' and day2[i] == 'O':
            out += 1
    return out

print(carpark(*lines))