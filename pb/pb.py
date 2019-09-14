import sys
lines = []
for _line in sys.stdin:
    stripped = _line.strip()
    if not stripped: break
    lines.append(stripped)

n1 = lines[0]
n2 = lines[1]

def arithmetic(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    print(f"{n1} + {n2} = {n1 + n2}")
    print(f"{n1} + {n2} = {n1 - n2}")
    print(f"{n1} + {n2} = {n1 * n2}")
    quotient = lambda a, b: int(a / b)
    remainder = lambda a, b: a - (int(a / b) * b)
    print(f"{n1} divided by {n2} is {quotient(n1, n2)} remainder {remainder(n1, n2)}")

arithmetic(*lines)