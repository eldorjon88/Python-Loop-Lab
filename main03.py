s = []
for _ in range(5):
    x = int(input("Son kiriting: "))
    s.append(x)
m = s[0]
for n in s:
    if n < m:
        m = n
print("Eng kichik son:", m)
