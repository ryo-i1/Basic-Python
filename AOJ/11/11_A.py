top, w, s = 1, 4, 2
labels = list(input().split())
for cmd in input():
    if cmd == 'W':
        top, w = 7-w, top
    elif cmd == 'E':
        top, w = w, 7-top
    elif cmd == 'N':
        top, s = s, 7-top
    elif cmd == 'S':
        top, s = 7-s, top

print(labels[top-1])

