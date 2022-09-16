def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return int(a / b)

S = open(0)
a, op, b = S.readline().split()
a, b = map(int, [a, b])

while op != '?':
    if op == '+':
        print(plus(a, b))
    elif op == '-':
        print(minus(a, b))
    elif op == '*':
        print(multi(a, b))
    elif op == '/':
        print(div(a, b))

    a, op, b = S.readline().split()
    a, b = map(int, [a, b])

