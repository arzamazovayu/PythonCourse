n = int ( input() )
an = input()
a = list(map(int, an.split()))

if (n == 1):
    if (sum(a) == 0):
        print("NO")
    else:
        print("YES")
        print(1)
        print(a.index(a[0])+1, a.index(a[-1])+1)
else:
    i = 1
    l = 0
    resA = []
    resB = []
    while i < n:
        r = l + i
        A = a[l:r]
        B = a[r:n]
        Ai = sum(A)
        Bi = sum(B)
        i += 1
        if Ai != 0 and Bi != 0:
            resA.append([l+1, r])
            resB.append([r+1, n])
    if resA and resB:
        print("YES")
        print(2)
        print(' '.join(map(str, resA[0])))
        print(' '.join(map(str, resB[0])))
    elif (sum(a) != 0):
        print("YES")
        print(1)
        print(1, len(a))
    else:
        print("NO")