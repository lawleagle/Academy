#2711 PutereBiti
if 0:
    n = int(input())
    print(1 << n)

#2708 VerifParitate
if 0:
    n = int(input())
    a = [int(x) & 1 for x in input().split()]
    [print(x, end=' ') for x in a]

#2577 getbit
if 0:
    t = int(input())
    for _ in range(t):
        [n, b] = [int(x) for x in input().split()]
        print((n >> b) & 1, end='')

#2580 setbit0
if 0:
    [n, b] = [int(x) for x in input().split()]
    print(n & (~(1 << b)))

#2581 setbit1
if 0:
    [n, b] = [int(x) for x in input().split()]
    print(n | (1 << b))

#2589 setlast2
if 0:
    n = int(input())
    print(n | 0b11)

#2590 removelast2
if 0:
    n = int(input())
    print(n & (~0b11))

#2624 invbits
if 0:
    from math import log2

    n = int(input())

    if n == 0:
        print(1)
    else:
        power = (int(log2(n))) + 1
        mask = ((1 << power) - 1)
        print(n ^ mask)

#2910 BitSwap
if 0:
    [n, m] = [int(x) for x in input().split()]
    n ^= m
    m ^= n
    n ^= m
    print(n, m)

#2672 primulbit
if 0:
    from math import log2

    n = int(input())
    if n == 0:
        print(1)
    else:
        print(int(log2(n)))

#3956 erasebits
if 0:
    n = int(input())
    while n:
        n = n & (n-1)
        print(n, end=' ')

#3590 bitdistance
if 0:
    from math import log2

    n = int(input())

    low_bit = 0
    while ((n >> low_bit) & 1) == 0:
        low_bit += 1

    high_bit = 63
    while ((n >> high_bit) & 1) == 0:
        high_bit -= 1

    print(high_bit - low_bit + 1)

#2799 AddOne
if 0:
    n = int(input())

    x = 1
    while n & x:
        n ^= x
        x <<= 1
    n ^= x

    print(n)

#2714 FrecvImp
if 0:
    f = open("frecvimp.in", "r")
    n = int(f.readline())
    a = [int(x) for x in f.readline().split()]

    r = 0
    for i in range(len(a)):
        if (a[i] & (a[i]-1)) == 0:
            r ^= a[i]

    g = open("frecvimp.out", "w")
    g.write(str(r))

#2583 lsbremove
if 0:
    n = int(input())
    print(n & (n-1))

#2586 getsecvbits
if 0:
    n = int(input())
    print((n >> 6) & 0b111)

#2587 swapbytes
if 0:
    n = int(input())

    b1 = n        & 0b11111111
    b2 = (n >> 8) & 0b11111111

    r = (b1 << 8) | b2
    if (r >> 15) & 1:
        r -= 1
        r ^= ((1 << 16) - 1)
        print(~r + 1)
    else:
        print(r)

#2677 puterealui2
if 0:
    n = int(input())
    if n & (n-1) == 0:
        print("DA")
    else:
        print("NU")

#2585 getbymask
if 0:
    [n, k] = [int(x) for x in input().split()]
    print(n & ((1 << k) - 1))

#2735 InsertBiti
if 0:
    [n, m, i] = [int(x) for x in input().split()]

    k = 0
    while (1 << k) <= m:
        k += 1
    k += i

    low = (n & ((1 << i) - 1))
    mid = (m << i)
    high = ((n >> k) << k)

    print(high + mid + low)

#2772 Placinte
#TODO: solve this
# saved for later, really cool problem
if 0:
    [n, k] = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    @dataclass
    class PancakeSet():
        no:    int   # number of pancakes
        speed: float # speed per pancake

#3641 Xorstanta
#TODO: whaat, IOI problem :)
# let's try to solve this later :D
if 0:
    t = int(input())
    for _ in range(t):
        n = int(input())

#3770 Bisectoare
if 0:
    f = open("bisectoare.in", "r")
    lines = f.readlines()
    r = 0
    for line in lines:
        x = int(line)
        r ^= x
    g = open("bisectoare.out", "w")
    g.write(str(r))

#4143 Ghicitoare
if 0:
    from functools import reduce
    from operator import xor

    if 0: # figure out how often the xor of the first n natural numbers is 0
        s = 0
        for i in range(1000000):
            s ^= i
            if s == 0 and i % 4 != 3:
                print(i)
    # turns out the xor of the first n natural numbers is 0 if and only if n % 4 == 3 or if n == 0

    f = open("ghicitoare.in", "r")
    g = open("ghicitoare.out", "w")

    t = int(f.readline())
    for _ in range(t):
        [n, S] = [int(x) for x in f.readline().split()]

        #v1
        if 0:
            s = reduce(xor, [x for x in range(1, n+1)])
            print(s ^ S)

        #v2
        while n % 4 != 3 and n != 0:
            S ^= n
            n -= 1

        g.write(str(S) + '\n')
