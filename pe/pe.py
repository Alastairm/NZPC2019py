import sys
lines = []
for _line in sys.stdin:
    stripped = _line.strip()
    if not stripped: break
    lines.append(stripped)

ew = lines[0].split()
ew = [int(x) for x in ew]
total = sum(ew) * 10
ex = ['A', 'B', 'C', 'D', 'E']
weights = {}
for i in range(len(ex)):
    weights[ex[i]] = ew[i]

n = int(lines[1])
student_names = {}
ids = []
results = {}
for student in lines[2:n+2]:
    sid = student[:4]
    name = student[5:]
    ids.append(sid)
    student_names[sid] = name
    results[sid] = {'A':'', 'B':'', 'C':'', 'D':'', 'E':''}

for test in lines[n+2:]:
    if test == '0 # #': break
    sid = test[:4]
    results[sid][test[5]] += test[7]

scores = {}
passed = {}
for student in student_names.keys():
    result = results[student]
    pscores = [10, 7, 4]
    student_score = 0
    for e in ex:
        if 'P' in result[e]:
            f, p = result[e].split('P')
            f = len(f)
            if f > 2:
                f = 2
            student_score += pscores[f] * weights[e]
    scores[student] = student_score
    if student_score / total >= 0.5:
        passed[student] = 'Pass'
    else:
        passed[student] = 'Fail'

for sid in ids:
    print(f"{student_names[sid]} {passed[sid]}")