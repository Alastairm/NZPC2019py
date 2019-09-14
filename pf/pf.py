import sys

COLOURS = ['R', 'G', 'B']
SHAPES = ['D', 'O', 'S']
NUMBERS = ['1', '2', '3']
FILLS = ['F', 'S', 'E']
CARD_PROPERTIES = [COLOURS, SHAPES, NUMBERS, FILLS]

stdin_lines = []
for _line in sys.stdin:
    stripped = _line.strip()
    if not stripped: break
    stdin_lines.append(stripped)

n = stdin_lines[0]

def make_card_set(card1, card2):
    card_properties = []
    for i in range(4):
        p1 = card1[i]
        p2 = card2[i]
        ptypes = CARD_PROPERTIES[i]
        card_properties.append(make_property_set(p1, p2, ptypes))
    return card_properties

def make_property_set(p1, p2, ptypes):
    if p1 == p2:
        return p1
    else:
        for ptype in ptypes:
            if p1 != ptype and p2 != ptype:
                return ptype

for line in stdin_lines[1:]:
    card1, card2 = line.split()
    set_card = make_card_set(card1, card2)
    print(''.join(set_card))