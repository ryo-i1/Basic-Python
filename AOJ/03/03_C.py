x, y = map(int, input().split())
while x != 0 or y != 0:
    if x >= y:
        print(y, x)
    else:
        print(x, y)
    x, y = map(int, input().split())

