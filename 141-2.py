def reversible(n):
    m = n
    a = []
    while n != 0:
        a.append(n % 10)
        n = n // 10
    a = ''.join(str(x) for x in a)
    if a == m:
        print(m, "la so thuan nghich")
    else:
        print(m, "khong la so thuan nghich")


name = "Luc Phi Khanh"
name_split = name.split()
n = []
for i in name_split:
    n.append(len(i))
n = int(''.join(str(x) for x in n))
reversible(n)
