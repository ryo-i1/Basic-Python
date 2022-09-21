def roll(d):
    return [[d[0], d[1], d[2], d[4], d[3], d[5]],
            [d[1], d[0], d[3], d[5], d[2], d[4]],
            [d[2], d[0], d[1], d[5], d[4], d[3]],
            [d[3], d[0], d[4], d[5], d[1], d[2]],
            [d[4], d[0], d[2], d[5], d[3], d[1]],
            [d[5], d[1], d[3], d[4], d[2], d[0]]
            ]

def sub_judge(d1, d2):
    if d1[0] != d2[0] or d1[5] != d2[5]:
        return False

    d1_side = d1[1:5]
    if d2[1] not in d1_side:
        return False
    idx = d1_side.index(d2[1])
    if d2[1:5] == (d1_side*2)[idx:idx+4]:
        return True
    else:
        return False

def judge(d1, d2):
    for i in range(6):
        for j in range(6):
            if sub_judge(d1[i], d2[j]):
                return True
    return False

dice1 = list(map(int, input().split()))
dice2 = list(map(int, input().split()))

if judge(roll(dice1), roll(dice2)):
    print("Yes")
else:
    print("No")

