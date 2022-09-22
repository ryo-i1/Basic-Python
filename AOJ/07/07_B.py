for dataset in iter(input, '0 0'):
    n, x = map(int, dataset.split())
    s = {(a, b, c) for a in range(1, n-1) for b in range(a+1, n) for c in range(b+1, n+1) if a+b+c == x}
    print(len(s))

