from math import sqrt
from dataclasses import dataclass
import math

#1
if 0:
    g = 5
    p = 3

    nr = (g*2) + (p*4) + 2
    print(nr)

#2 
if 0:
    x = 123
    y = 349

    s = x + y
    uc = s % 10
    print(uc)

#3
if 0:
    a = 2
    b = 3
    c = 4

    p = (a + b + c) / 2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print(s)

#4
if 0:
    l = 4
    h = 3
    s = (l * h) / 2
    print(s)

#5
if 0:
    v = 3 # km / week
    d = 5 # m

    v = v * 1000 # m / week
    v = v / 7    # m / day
    v = v / 24   # m / hour

    # v = d / t
    t = d / v
    print(t)

#6
#a)
if 0:
    a = 4
    b = 9
    c = a
    a = b
    b = c
    print(a,b)
#b)
if 0:
    a = 4
    b = 9
    (a, b) = (b, a)
    print(a, b)

#7
if 0:
    x = 20
    l2 = x / 5
    l1 = l2 / 4

    a1 = l1*l1
    a2 = l2*l2
    print(a1, a2)

#8
if 0:
    a = 36
    b = 48
    k = 4
    if a % k == 0 and b % k == 0:
        print("{}/{}".format(a/k, b/k))
    else:
        print("cannot simplify")

#9
if 0:
    z = 25
    if z <= 10:
        print("first decade")
    elif z <= 20:
        print("second decade")
    else:
        print("third decade")

#10
if 0:
    x = 64
    sq = round(sqrt(x))
    if sq * sq == x:
        print("perfect square")
    else:
        print("not perfect square")

#11
if 0:
    x = 125
    cb = round(x ** (1/3))
    if cb * cb * cb == x:
        print("perfect cube")
    else:
        print("not perfect cube")

#12
if 0:
    r1 = 2
    r2 = 7
    h = 4
    v =  (math.pi * h) / 3 * (r1*r1 + r2*r2 + r1 * r2)
    print(v)

#13
if 0:
    r = 2
    g = 9
    a = 2 * math.pi * r * (r + g)
    print(a)

#14
if 0:
    b1 = 2
    b2 = 9
    h = 4
    a = ((b1 + b2) * h) / 2
    print(a)

#15
if 0:
    day = 4
    days = ["Monday", "Tuesday", "Wednessday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(days[zi-1])

#16
if 0:
    l = "A"
    l = l.lower()

    match l:
        case "a" | "e" | "i" | "o" | "u":
            print(l, "is vowel")
        case _:
            print(l, "is not vowel")

#17
if 0:
    a = 5
    b = 12
    op = "+"
    match op:
        case "+": print(a+b)
        case "-": print(a-b)
        case "*": print(a*b)
        case "/": print(a/b)

#18
if 0:
    a = 10 # weeks
    b = 5 # days
    d = 1000 # km
    # v = ? m/s

    a = a * 7 # days
    t = a + b # days
    t = t * 24 # hours
    t = t * 60 # minutes
    t = t * 60 # seconds
    d = d * 1000 # m
    v = d / t
    print(v)

#19
if 0:
    @dataclass
    class Time:
        hour: int = 0
        minute: int = 0
        second: int = 0
        centisecond: int = 0

    t1 = Time(5, 45, 36, 20)
    t2 = Time(1, 30, 29, 90)
    t = Time()

    t.centisecond = t1.centisecond + t2.centisecond
    carry = 0
    if t.centisecond >= 100:
        t.centisecond -= 100
        carry = 1

    t.second = t1.second + t2.second + carry
    carry = 0
    if t.second >= 60:
        t.second -= 60
        carry = 1

    t.minute = t1.minute + t2.minute + carry
    carry = 0
    if t.minute >= 60:
        t.minute -= 60
        carry = 1

    t.hour = t1.hour + t2.hour + carry
    print(t)

#20
if 0:
    def sum_digits(n):
        u = n % 10
        z = (n / 10) % 10
        s = n / 100
        return u + z + s

    a = 321
    b = 263
    if sum_digits(a) > sum_digits(b):
        print(a)
    else:
        print(b)

#21
if 0:
    a = 30
    b = 24
    if a > b:
        print(a)
    else:
        print(b)

#22
if 0:
    a = 34
    b = 12
    c = 43

    if a > b: (a, b) = (b, a) # swap
    if a > c: (a, c) = (c, a) # swap
    if b > c: (b, c) = (c, b) # swap

    print("min is", a)
    print("max is", c)

#23
if 0:
    a = 23
    b = 224
    c = 4
    d = 45

    if a > b: a = b
    if a > c: a = c 
    if a > d: a = d

    print("min is", a)

#24
if 0:
    a = -4
    b = -2
    c = 12
    d = 5

    mx = 0
    if a < 0: mx = a
    if b < 0: mx = b
    if c < 0: mx = c
    if d < 0: mx = d
    if mx == 0:
        print("there are no negative values")
    else:
        if a < 0: mx = max(mx, a)
        if b < 0: mx = max(mx, b)
        if c < 0: mx = max(mx, c)
        if d < 0: mx = max(mx, d)
        print ("biggest negative value:", mx)

    mn = 100
    if a >= 0: mn = a
    if b >= 0: mn = b
    if c >= 0: mn = c
    if d >= 0: mn = d
    if mn == 0:
        print("there are no positive values")
    else:
        if a >= 0: mn = min(mn, a)
        if b >= 0: mn = min(mn, b)
        if c >= 0: mn = min(mn, c)
        if d >= 0: mn = min(mn, d)
        print("smallest positive value:", mn)

#25
if 0:
    x = "a"
    x = x.upper()
    match x: 
        case "A" | "B" | "C": print(2)
        case "D" | "E" | "F": print(3)
        case "G" | "H" | "I": print(4)
        case "J" | "K" | "L": print(5)
        case "M" | "M" | "O": print(6)
        case "P" | "R" | "S": print(7)
        case "T" | "U" | "V": print(8)
        case "W" | "X" | "Y": print(9)
        case _: print("not on phone keyboard")

#26
if 0:
    x = 2000
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        print(x,"is leap year")
    else:
        print(x,"is not leap year")

#27
if 0:
    def is_leap_year(year):
        return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    z = 27
    l = 2
    a = 1990

    if days_in_month[l] >= z or (l == 2 and is_leap_year(a) and z == 29):
        print("correct date")
    else:
        print("not a correct date")

#28
if 0:
    a = 3
    b = 4
    c = 5
    if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
        print("Pythagorean numbers")
    else:
        print("not Pythagorean numbers")

#29
if 0:
    @dataclass
    class Student:
        name: str
        final_grade: float

    e1 = Student("Ionescu", 6.80)
    e2 = Student("Antonescu", 9.40)
    e3 = Student("Popescu", 8.25)

    if e1.final_grade > e2.final_grade: (e1, e2) = (e2, e1) # swap
    if e1.final_grade > e3.final_grade: (e1, e3) = (e3, e1) # swap
    if e2.final_grade > e3.final_grade: (e2, e3) = (e2, e3) # swap

    print(e3.name, e2.name, e1.name)

#30
#TODO: solve this
# skipping for now, as it requires dynamic programming

#31
#a)
if 0:
    a = 85
    b = 34
    c = 67

    # a b c
    # a c b
    # b a c
    # b c a
    # c a b
    # c b a

    if a <= b <= c:
        print(a, b, c)
    elif a <= c <= b:
        print(a, c, b)
    elif b <= a <= c:
        print(b, a, c)
    elif b <= c <= a:
        print(b, c, a)
    elif c <= a <= b:
        print(c, a, b)
    elif c <= b <= a:
        print(c, b, a)

#b)
if 0:
    a = 85
    b = 34
    c = 67

    if a > b: (a, b) = (b, a)
    if a > c: (a, c) = (c, a)
    if b > c: (b, c) = (c, b)

    print(a, b, c)

#32
if 0:
    # 1 - in to cm and m
    # 2 - ft to cm and m
    # 3 - lb to g and kg
    # 4 - oz to g and kg
    # 5 - gal to l

    # 11 - cm to in and ft
    # 12 - m  to in and ft
    # 13 - kg to oz and lb
    # 14 - g  to oz and lb
    # 15 - l  to gal
    value = 13

    a = value * 2.54
    print("{} in = {} cm = {} m".format(value, a, a/100))

    a = value * 0.3084
    print("{} ft = {} m = {} cm".format(value, a, a*100))

    a = value * 0.45359
    print("{} lb = {} kg = {} g".format(value, a, a*100))

    a = value * 28.3495
    print("{} oz = {} g = {} kg".format(value, a, a/100))

    a = value * 3.78541
    print("{} l = {} gal".format(value, a))


    a = value / 2.54
    print("{} cm = {} in = {} ft".format(value, a, a/12))

    a = value / 0.3084
    print("{} m = {} ft = {} in".format(value, a, a*12))

    a = value / 0.45359
    print("{} kg = {} lb = {} oz".format(value, a, a*16))

    a = value / 28.3495
    print("{} g = {} oz = {} lb".format(value, a, a/16))

    a = value / 3.78541
    print("{} l = {} gal".format(value, a))

#33
if 0:
    a = 1 
    b = 2
    c = 3

    d = a
    a = b
    b = c
    c = d 

    print(a, b, c)

#34
if 0:
    a = 1331

    u = a % 10
    z = (a // 10) % 10
    s = (a // 100) % 10
    m = (a // 1000) % 10

    if u == m and s == z:
        print("palindrome number")
    else:
        print("not a palindrome number")

#35
if 0:
    an = 1985
    a = an % 19
    b = an % 4
    c = an % 7
    d = (19 * a + 24) % 30 
    e = (2 * b + 4 * c + 6 * d + 5) % 7

    data = 22 + e + d 

    if data > 31:
        print (data-31, "April")
    else:
        print(data, "March")

#36
if 0:
    a = 1
    b = -3
    c = 2

    delta = b**2 - 4*a*c

    if delta < 0:
        print("no real solutions")
    elif a == 0 and b == 0:
        if c == 0:
            print("infinitely many solutions")
        else:
            print("no real solutions")
    elif a == 0:
        x = - c/b
        print(x)
    else:
        x1 = (-b + sqrt(delta)) / 2*a
        x2 = (-b - sqrt(delta)) / 2*a

        print(x1, x2)

#37
if 0:
    @dataclass
    class Angle:
        degrees: int
        minutes: int
        seconds: int

    a = Angle(30, 50, 45)
    b = Angle(10, 20, 53)

    d = Angle(0, 0, 0)
    d.seconds = a.seconds - b.seconds
    carry = 0
    if d.seconds < 0:
        d.seconds += 60
        carry = -1

    d.minutes = a.minutes - b.minutes + carry
    carry = 0
    if d.minutes < 0:
        d.minutes += 60
        carry = -1

    d.degrees = a.degrees - b.degrees + carry

    print(d)

#38
if 0:
    a = 15
    b = 34
    p = a * b
    uc = p % 10
    pc = (p // 10) % 10
    print(pc, uc)

#39
if 0:
    a = 1
    b = 3
    c = 4
    d = 2

    if a != b and a != c and a != d and b != c and b != d and c != d:
        print("numbers can form a set")
    else:
        print("numbers cannot form a set")

#40
if 0:
    a = 10
    b = 3 
    c = 17

    if a > b: (a, b) = (b, a)
    if a > c: (a, c) = (a, c)
    if b > c: (b, c) = (c, b)

    r = b - a 
    if r == c - b:
        print("arythmetic progression")
    else:
        print("not an arythmetic progression")

#41
if 0:
    a = 6
    b = 7
    c = 6

    if a > b: (a, b) = (b, a)
    if a > c: (a, c) = (a, c)
    if b > c: (b, c) = (c, b)

    if a + b > c:
        if a == c: # a == b == c because a is smallest and c is largest and a == c
            print("equilateral triangle")
        elif a == b or b == c:
            print("isosceles triangle")
        elif a / 3 == b / 4 == c / 5:
            print("right triangle")
        else:
            print("just a triangle")
    else:
        print("not a triangle")

#42
if 0:
    @dataclass
    class v2:
        x: float
        y: float

        def __sub__(self, other):
            if not isinstance(other, v2):
                return NotImplemented
            return v2(self.x - other.x, self.y - other.y)

    b = v2(1, 2)
    c = v2(7, 12)
    a = v2(4, 7)

    d_ab = b - a
    d_ac = c - a

    print(d_ab)
    print(d_ac)

    if d_ab.x / d_ac.x == d_ab.y / d_ac.y:
        print("collinear")
    else:
        print("non collinear")

#43
if 0: 
    a = 55
    b = 40
    c = 85

    if a <= 0 or b <= 0 or c <= 0 or a+b+c != 180:
        print("not a triangle")
    elif a > 90 or b > 90 or c > 90:
        print("obtuse triangle")
    elif a == 90 or b == 90 or c == 90:
        print("right triangle")
    else:
        print("acute triangle")

#44
if 0:
    a = 2
    b = -4

    if a == 0 and b == 0:
        print("origin")
    elif b == 0:
        print("Ox axis")
    elif a == 0:
        print("Oy axis")
    elif a > 0 and b > 0:
        print("quadrant 1")
    elif a < 0 and b > 0:
        print("quadrant 2")
    elif a < 0 and b < 0:
        print("quadrant 3")
    elif a > 0 and b < 0:
        print("quadrant 4")

#45
if 0:
    a = 0
    b = 2
    c = 4 

    if c < 0:
        print("no solution")
    elif a == 0:
        if b == c**2:
            print("infinitely many solutions")
        else:
            print("no solution")
    else:
        x = (c**2 - b) / a
        print(x)

#46 
#TODO: this could use more work
# figure out if there are no solutions or an infinite amount of solutions
if 0:
    a = 2
    b = 5
    c = -37
    d = 14
    e = 35
    f = -259

    # ax + by = c -> y = (c-ax)/b
    # dx + ey = f -> 
    # dx + e(c-ax)/b = f
    # dx + ec/b - aex/b = f
    # dx - aex/b = f - ec/b
    # x(d - ae/b) = f - ec/b

    try:
        x = (f - e*c/b) / (d - a*e/b)
        y = (c-a*x)/b
        print(x, y)
    except:
        print("could not solve. either there is no solution or there are infinitely many solutions")

#47
if 0:
    @dataclass
    class v2:
        x: float
        y: float

        def __sub__(self, other):
            if not isinstance(other, v2):
                return NotImplemented
            return v2(self.x - other.x, self.y - other.y)

        def magnitudeSq(self):
            # mag**2 == x**2 + y**2
            return self.x**2 + self.y**2


    a = v2(2, 2)
    b = v2(2, 5)
    c = v2(10, 5)
    d = v2(10, 2)

    # edges
    ab = b - a
    bc = c - b
    cd = d - c
    da = a - d

    # diagonals
    ac = c - a
    bd = d - b

    abc_right_triangle = (ab.magnitudeSq() + bc.magnitudeSq() == ac.magnitudeSq())
    bcd_right_triangle = (bc.magnitudeSq() + cd.magnitudeSq() == bd.magnitudeSq())
    cda_right_triangle = (cd.magnitudeSq() + da.magnitudeSq() == ac.magnitudeSq())
    if abc_right_triangle and bcd_right_triangle and cda_right_triangle: 
        print("rectangle")
    else:
        print("not a rectangle")

#48
if 0:
    n = 10
    if n % 2 == 0:
        n = -n // 2 
    else:
        n = (n // 2) + 1
    print(n)

#49
if 0:
    # line ab, point c
    # (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x) == 0 -> c is on line ab
    # (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x) < 0  -> c is on one side of line ab
    # (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x) > 0  -> c is on the other side of line ab

    # poit d is inside triangle abc if and only if it is on the same side of lines ab, bc, ca
    @dataclass
    class v2:
        x: float
        y: float

    a = v2(7, 8)
    b = v2(12, 3)
    c = v2(2, 1)

    d = v2(10, 5)

    def side(a, b, c):
        return (b.x - a.x)*(c.y - a.y) - (b.y - a.y)*(c.x - a.x)

    left  = (side(a, b, d) < 0 and side(b, c, d) < 0 and side(c, a, d) < 0)
    right = (side(a, b, d) > 0 and side(b, c, d) > 0 and side(c, a, d) > 0)
    if left or right:
        print("point is inside triangle")
    else:
        print("point is not inside triangle")

#50
#NOTE: romanian written names of numbers up to 9999
if 0:
    denumire = ["zero", "unu", "doi", "trei", "patru", "cinci", "sase", "sapte", "opt", "noua"]

    def masculin(i):
        return denumire[i]

    def feminin(i): # denumirea cifrei i la feminin
        match i:
            case 1: return "o"
            case 2: return "doua"
            case _: return denumire[i]

    def print_in_Romanian(x):
        m = x // 1000        # mii
        s = (x // 100) % 10  # sute
        z = (x // 10) % 10   # zeci
        u = x % 10           # unitati

        res = (denumire[0] if x == 0 else "")
        match m:
            case 0: pass
            case 1: res += feminin(m) + " mie "
            case _: res += feminin(m) + " mii "

        match s:
            case 0: pass
            case 1: res += feminin(s) + " suta "
            case _: res += feminin(s) + " sute "

        match z:
            case 0: pass
            case 1: 
                match u:
                    case 0: res += "zece"
                    case 1: res += "unsprezece"
                    case 2: res += "doisprezece"
                    case 3: res += "treisprezece"
                    case 4: res += "paisprezece"
                    case 5: res += "cincisprezece"
                    case 6: res += "saisprezece"
                    case 7: res += "saptesprezece"
                    case 8: res += "optsprezece"
                    case 9: res += "nouasprezece"
            case 6:
                res += "saizeci "
            case _:
                res += feminin(z) + "zeci "

        if z != 1:
            match u:
                case 0: pass
                case _: res += ("si " if z > 0 else "") + masculin(u)
        print(res)

    for i in range(10000):
        print_in_Romanian(i)

#51
if 0:
    x = 259 
    match x % 4:
        case 1: print(2)
        case 2: print(4)
        case 3: print(8)
        case 0: print(6)

#52 
if 0:
    a = 2
    b = 259

    match a % 10:
        case 1: print(1)
        case 2: 
            r = [6, 2, 4, 8]
            print(r[b%4])
        case 3:
            r = [1, 3, 9, 7]
            print(r[b%4])
        case 4:
            r = [6, 4]
            print(r[b%2])
        case 5: print(5)
        case 6: print(6)
        case 7:
            r = [1, 7, 9, 3]
            print(r[b%4])
        case 8:
            r = [6, 8, 4, 2]
            print(r[b%4])
        case 9:            
            r = [1, 9]
            print(r[b%2])

#53
if 0:
    a = 2379

    r2 = [6, 2, 4, 8]
    r3 = [1, 3, 9, 7]
    r4 = [6, 4]
    r7 = [1, 7, 9, 3]
    r8 = [6, 8, 4, 2]
    r9 = [1, 9]

    uc  = r2[a%4]
    uc += r3[a%4]
    uc += r4[a%2]
    uc += 5
    uc += 6
    uc += r7[a%4]
    uc += r8[a%4]
    uc += r9[a%2]
    uc %= 10

    print(uc)

#54
#TODO: solve this
# skipping for now, as it requires backtracking

#55
if 0: 
    x =  5.5

    if x <= -3:
        f = x*x + 1
    elif -3 < x < 3:
        f = x -2
    else:
        f = x*x - 4 * x + 5
    print(f)

#56
if 0:
    a = 5
    b = -9
    c = 7
    d = 4

    k = 0
    if a > 0: k += 1
    if b > 0: k += 1
    if c > 0: k += 1
    if d > 0: k += 1
    if k >= 3:
        s = 0
        if a > 0: s += a
        if b > 0: s += b
        if c > 0: s += c
        if d > 0: s += d
        if s % 2 == 0:
            print(a + b + c + d)
        else:
            print(a * b * c * d)

#57
if 1:
    a = False
    b = True
    c = False
    d = True
    e = False
    x = 3
    y = 9
    z = 1

    #v1)
    if 1:
        if a < b: (a, b) = (b, a)
        if a < c: (a, c) = (c, a)
        if a < d: (a, d) = (d, a)
        if a < e: (a, e) = (e, a)
        if b < c: (b, c) = (c, d)
        if b < d: (b, d) = (d, b)
        if b < e: (b, e) = (e, b)
        if c < d: (c, d) = (d, c)
        if c < e: (c, e) = (e, c)
        if d < e: (d, e) = (e, d)
        print(a, b, c, d, e)

        if a == b == c == True:
            v = max(x, y, z)
        else:
            v = min(x, y, z)

    #v2)
    if 0:
        k = 0 # accumulator
        if a == True: k += 1
        if b == True: k += 1
        if c == True: k += 1
        if d == True: k += 1
        if e == True: k += 1

        if k >= 3:
            v = max(x, y, z)
        else:
            v = min(x, y, z)

    print(v)

#58
if 0:
    a = -1.4
    b = 6.1
    c = 5
    d = -5

    if c + d > 0:
        f = a + b
    elif c + d == 0:
        f = a - b
    elif c + d < 0:
        f = a * b
    print(f)

#59
if 0:
    x = 27.5
    if x < 5:
        f = x*x - 3
    elif 5 <= x <= 25:
        f = x + 1
    elif x > 25:
        f = x*x - 5*x + 6
    print(f)

#60
#a)
if 0:
    x = 0.5
    if 0 < x < 1:
        print(x + 1)
    else:
        print(x*x - 5*x + 6)
#b)
if 0:
    x = - 2.5
    if x < 1:
        print(sqrt(x*x + x + 2))
    elif 1 <= x <= 2:
        print(3*x - 1)
    else:
        print((5*x - 2) / (x + 2))

#61
if 0:
    n = 5
    c = 130
    c *= 1_000_000

    print(c / (2**(n-1)))

#62
if 0:
    c = 'X'

    n = ord(c)
    g1 = n & 0b11        # first  group of 2 bits
    g2 = (n >> 2) & 0b11 # second group of 2 bits
    g3 = (n >> 4) & 0b11 # third  group of 2 bits
    g4 = (n >> 6) & 0b11 # fourth group of 2 bits

    r = (g3 << 6) | (g4 << 4) | (g1 << 2) | g2
    print(chr(r))

#63
if 0:
    z = 6
    l = 4
    a = 2

    print("{:b}".format(z))
    print("{:b}".format(l))
    print("{:b}".format(a))

    code = (a << 9) | (l << 5) | z

    print("{:b}".format(code))
    print(code)

    nz =  code       & 0b11111
    nl = (code >> 5) & 0b1111
    na = (code >> 9) & 0b1111111

    print(nz)
    print(nl)
    print(na)
