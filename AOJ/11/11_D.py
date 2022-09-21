def roll(d):
    return [[d[0], d[1], d[2], d[4], d[3], d[5]],
            [d[1], d[0], d[3], d[5], d[2], d[4]],
            [d[2], d[0], d[1], d[5], d[4], d[3]],
            [d[3], d[0], d[4], d[5], d[1], d[2]],
            [d[4], d[0], d[2], d[5], d[3], d[1]],
            [d[5], d[1], d[3], d[4], d[2], d[0]]
            ]

def compare(d1, d2):
    if d1[0] != d2[0] or d1[5] != d2[5]:
        return False

    d1_side = d1[1:5]
    if d2[1] not in d1_side:
        return False
    idx = d1_side.index(d2[1])
    if d2[1:5] == (d1_side*2)[idx:idx+4]:
        return True
    return False

def judge(d1, d2):
    _d1 = roll(d1)
    _d2 = roll(d2)
    for sub_d1 in _d1:
        for sub_d2 in _d2:
            if compare(sub_d1, sub_d2):
                return True
    return False

n = int(input())
dices = []
judge_end = False
for _n in range(n):
    dice_new = list(map(int, input().split()))
    for dice in dices:
        if judge(dice_new, dice):
            print("No")
            judge_end = True
            break
    if judge_end:
        break
    dices.append(dice_new)

if not judge_end:
    print("Yes")

