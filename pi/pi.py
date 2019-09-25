import sys
stdin_lines = []
for _line in sys.stdin:
    stripped = _line.strip()
    if not stripped: break
    stdin_lines.append(stripped)

guesses = stdin_lines[1:]

L = ['A', 'B', 'C', 'D', 'E', 'F']

def create_s():
    s = []
    for a in range(6):
        for b in range(6):
            for c in range(6):
                for d in range(6):
                        s.append(f"{L[a]}{L[b]}{L[c]}{L[d]}")
    return s

def score(code, guess):

    def black_score(code, guess):
        hit = 0
        mask = [0, 0, 0, 0]
        for i in range(4):
            if code[i] == guess[i]:
                hit += 1
                mask[i] = 1
        return (hit, mask)

    def white_score(code, guess, mask):
        hit = 0
        guess_list = []
        code_list = []

        for i in range(4):
            if mask[i] != 1:
                guess_list.append(guess[i])
                code_list.append(code[i])
        
        for g in guess_list:
            if g in code_list:
                code_list.remove(g)
                hit += 1
        return hit


    black_hit, hit_mask = black_score(code, guess)
    white_hit = white_score(code, guess, hit_mask)
    return (black_hit, white_hit)

S = create_s()
guess_number = 0
for guess in guesses:
    if len(S) == 1:
        break

    guess_number += 1
    guess, black, white = guess.split()
    black = int(black)
    white = int(white)

    for code in S.copy():
        if score(code, guess) != (black, white):
            S.remove(code)

print(S[0])
print(guess_number)