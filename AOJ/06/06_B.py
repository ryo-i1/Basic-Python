spades = list(range(1, 14))
hearts = list(range(1, 14))
clubs = list(range(1, 14))
diamonds = list(range(1, 14))

n = int(input())
for i in range(n):
    suit, num = input().split()
    if suit == 'S':
        spades.remove(int(num))
    elif suit == 'H':
        hearts.remove(int(num))
    elif suit == 'C':
        clubs.remove(int(num))
    elif suit == 'D':
        diamonds.remove(int(num))

[print('S', i) for i in spades]
[print('H', i) for i in hearts]
[print('C', i) for i in clubs]
[print('D', i) for i in diamonds]

