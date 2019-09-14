import sys
stdin_lines = []
for _line in sys.stdin:
    stripped = _line.strip()
    if not stripped: break
    stdin_lines.append(stripped)

n = stdin_lines[0]

expressions = stdin_lines[1:]

def calculate(expression):
    expression = expression.split(' ')
    stack = []  # Store of numbers to operate on
    for x in expression:
        try:
            xi = int(x)
            stack.append(xi)
        except ValueError:
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(math(x, n1, n2))

    if len(stack) == 1:
        return (int(stack[0]))
    else:
        raise Exception('Operator value mismatch')

def math(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return int(n1 // n2)



for e in expressions:
    print(calculate(e))