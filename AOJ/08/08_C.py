ln = [0] * (ord('z') - ord('a') + 1)
for line in open(0).read():
    for s in line.strip().lower():
        if ord(s) in range(ord('a'), ord('z')+1):
            ln[ord(s) - ord('a')] += 1

for i in range(len(ln)):
    print(chr(i + ord('a')), ':', ln[i])

