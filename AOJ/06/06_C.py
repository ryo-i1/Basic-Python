buildings = [[[0] * 10 for i in range(3)] for j in range(4)]

n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())
    buildings[b-1][f-1][r-1] += v

for i, b in enumerate(buildings):
    if i != 0:
        print('#' * 20)
    [print('', *floor) for floor in b]

