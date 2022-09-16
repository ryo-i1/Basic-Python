def div(a, b):
    return a/b

def rem(a, b):
    return a % b

a, b = map(int, input().split())
print(
    int(div(a, b)),
    rem(a, b),
    "{:.6f}".format(div(a, b))
    )

