n, m, y = map(int, input().split())

c =  []
for x in range(0,  m):
    if pow(x, n, m) == y:
        c.append(str(x))
print(" ".join(c) if len(c) > 0 else -1)
