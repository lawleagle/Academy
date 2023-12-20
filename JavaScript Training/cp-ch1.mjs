// Carmen Popescu Programming Challenges 2002
// Chapter 1 - Elementele de bază ale limbajului

// 1
if ( false ) {
    let g = 5
    let p = 3
    console.log(2*g + 4*p + 2)
}


// 2
if ( false ) {
    let x = 123
    let y = 349
    console.log( (x+y) % 10 )
}


// 3
if ( false ) {
    let a = 2
    let b = 3
    let c = 4
    let sp = (a + b + c) / 2
    let aria = Math.sqrt(sp * (sp - a) * (sp - b) * (sp - c))
    console.log(aria)
}


// 4
if ( false ) {
    let l = 4
    let h = 3
    console.log(l * h / 2)
}


// 5
// km / week
// km / 7 days
// 1/7 km / day
// 1000/7 m / day
// 1000/(7*24) m / hour
// 5 km/week = 5000/(7*24) m/hour
// v = d/t <=> t = d/v
if ( false ) {
    let v = 3
    let d = 5
    v = v*1000/(7*24)
    let t = d/v
    console.log(t)
}


// 6
// a)
if ( false ) {
    let a = 5
    let b = 7

    let c = a
    a = b
    b = c
    console.log(a, b)
}
// b)
// a  a-b   a-b        a-b-a=-b
// b   b   b+a-b==a      a
if ( false ) {
    let a = 5
    let b = 7

    a = a-b
    b = a+b
    a = -a+b
    console.log(a, b)
}


// 7
// a+a+a+a = b
// a+a+a+a + b+b+b+b = x
if ( false ) {
    let x = 20
    let l2 = x / 5
    let l1 = l2 / 4
    console.log(l1 * l1, l2 * l2)
}


// 8
if ( false ) {
    // let a = 36
    // let b = 48
    let a = 12
    let b = 89
    let k = 4

    if (a % k == 0 && b % k == 0) {
        console.log(a+'/'+b+' se simplifica cu '+k+' si da '+a/k+'/'+b/k)
    } else {
        console.log(a+'/'+b+' nu se simplifica cu '+k)
    }
}


// 9
if ( false ) {
    // let day = 13
    let day = 25
    if (day <= 10) {
        console.log('prima decada')
    } else if (day <= 20) {
        console.log('a doua decada')
    } else {
        // deoarece a treia decadă este ultima decadă,
        // am presupus că ziua 31 e tot în a treia decadă
        console.log('a treia decada')
    }
}


// 10
if ( false ) {
    // let x = 64
    let x = 35
    let sqRootInt = Math.floor(Math.sqrt(x))
    if (sqRootInt * sqRootInt === x) {
        console.log('perfect square')
    } else {
        console.log('not perfect square')
    }
}


// 11
if ( false ) {
    let x = 125
    let cbRtInt = Math.floor(Math.cbrt(x))
    if (cbRtInt * cbRtInt * cbRtInt === x) {
        console.log('perfect cube')
    } else {
        console.log('not perfect cube')
    }
}


// 12
if ( false ) {
    let R1 = 2
    let R2 = 7
    let h = 4
    console.log((Math.PI * h / 3) * (R1*R1 + R2*R2 + R1*R2))
}


// 13
if ( false ) {
    let R = 2
    let G = 9

    let A = 2 * Math.PI * R * (R + G)
    console.log(A)
}


// 14
if ( false ) {
    let b1 = 2
    let b2 = 9
    let h = 4

    let A = (b1 + b2) * h / 2
    console.log(A)
}


// 15
if ( false ) {
    let day = 5
    switch (day) {
        case 1: {
            console.log('luni')
        } break

        case 2: {
            console.log('marti')
        } break

        case 3: {
            console.log('miercuri')
        } break

        case 4: {
            console.log('joi')
        } break

        case 5: {
            console.log('vineri')
        } break

        case 6: {
            console.log('sambata')
        } break

        case 7: {
            console.log('duminica')
        } break
    }
}


// 16
if ( false ) {
    let letter = 'x'
    if ('aeiou'.includes(letter)) {
        console.log('vocala')
    } else {
        console.log('consoana')
    }
}


// 17
if ( false ) {
    let a = 5
    let b = 12
    let op = '*'

    switch (op) {
        case '+': {
            console.log(a+b)
        } break

        case '-': {
            console.log(a-b)
        } break

        case '*': {
            console.log(a*b)
        } break

        case '/': {
            console.log(a/b)
        } break
    }
}


// 18
if ( false ) {
    let a = 10
    let b = 5
    let d = 1000

    d *= 1000
    let t = a * 7 + b
    t *= 24 * 3600

    let v = d / t
    console.log(v)
}


// 19
if ( false ) {
    let t1 = [5, 45, 36, 20]
    let t2 = [1, 30, 29, 90]

    let z = t1[3] + t2[3], carry = 0
    if (z >= 100) { z -= 100; carry = 1 }

    let s = t1[2] + t2[2] + carry; carry = 0
    if (s >= 60) { s -= 60; carry = 1 }

    let m = t1[1] + t2[1] + carry; carry = 0
    if (m >= 60) { m -= 60; carry = 1 }

    let o = t1[0] + t2[0] + carry;

    let t3 = [o, m, s, z]
    console.log(t3)
}


// 20
if ( false ) {
    let a = 321
    let b = 263

    let sumCif = x => (x % 10) + (Math.floor(x / 10) % 10) + (Math.floor(x / 100))

    let sa = sumCif(a)
    let sb = sumCif(b)
    if (sa > sb) {
        console.log(a)
    } else {
        console.log(b)
    }
}


// 21
if ( false ) {
    // let a = 30
    // let b = 24o
    let a = 2
    let b = 32

    if (a < b) {
        [a, b] = [b, a]
    }
    console.log(a)
}


// 22
if ( false ) {
    let a = 30
    let b = 12
    let c = 43

    if (a < b) [a, b] = [b, a]
    if (a < c) [a, c] = [c, a]
    if (b < c) [b, c] = [c, b]

    console.log('max', a)
    console.log('min', c)
}


// 23
if ( false ) {
    let a = 23
    let b = 224
    let c = 4
    let d = 45

    if (a > b) [a, b] = [b, a]
    if (a > c) [a, c] = [c, a]
    if (a > d) [a, d] = [d, a]

    console.log('min', a)
}


// 24
if ( false ) {
    let a = -4
    let b = -2
    let c = 12
    let d = 5

    if (a > b) [a, b] = [b, a]
    if (a > c) [a, c] = [c, a]
    if (a > d) [a, d] = [d, a]
    if (b > c) [b, c] = [c, b]
    if (b > d) [b, d] = [d, b]
    if (c > d) [c, d] = [d, c]

    // maximul valorilor negative
    if (a >= 0) {
        console.log('nu avem valori negative')
    } else {
        if (b < 0) a = b
        if (c < 0) a = c
        if (d < 0) a = d
        console.log('maximul valorilor negative', a)
    }

    // minimul valorilor pozitive
    if (d < 0) {
        console.log('nu avem valori pozitive')
    } else {
        if (c >= 0) d = c
        if (b >= 0) d = b
        if (a >= 0) d = a
        console.log('minimul valorilor pozitive', d)
    }
}


// 25
if ( false ) {
    let l = 'W'
    if ('ABC'.includes(l)) console.log(2)
    if ('DEF'.includes(l)) console.log(3)
    if ('GHI'.includes(l)) console.log(4)
    if ('JKL'.includes(l)) console.log(5)
    if ('MNO'.includes(l)) console.log(6)
    if ('PRS'.includes(l)) console.log(7)
    if ('TUV'.includes(l)) console.log(8)
    if ('WXY'.includes(l)) console.log(9)
    if ('QZ'.includes(l)) console.log('letter not on keyboard')
}


// 26
if ( false ) {
    let y = 1600
    if (y % 4 === 0 && y % 100 !== 0 || y % 400 === 0) {
        console.log('an bisect')
    } else {
        console.log('anul nu este bisect')
    }
}


// 27
if ( false ) {
    let day = 29
    let month = 2
    let year = 1992

    let isBisect = y => {
        if (y % 4 === 0 && y % 100 !== 0 || y % 400 === 0) {
            return 1
        }
        return 0
    }

    let daysInMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (isBisect(year)) daysInMonth[2] = 29

    if (1901 <= year && year <= 2000 &&
        1 <= month && month <= 12 &&
        1 <= day && day <= daysInMonth[month]) {
        console.log('valid date of century XX')
    } else {
        console.log('not a valid date of century XX')
    }
}


// 28
if ( false ) {
    let a = 3
    let b = 4
    let c = 5

    if (a*a + b*b === c*c ||
        a*a + c*c === b*b ||
        b*b + c*c === a*a) {
        console.log('numere pitagorice')
    } else {
        console.log('nu sunt numere pitagorice')
    }
}


// 29
if ( false ) {
    let a = {
        n: 'Ionescu',
        m: 6.80
    }
    let b = {
        n: 'Antonescu',
        m: 9.40
    }
    let c = {
        n: 'Popescu',
        m: 8.25
    }

    if (a.m < b.m) [a, b] = [b, a]
    if (a.m < c.m) [a, c] = [c, a]
    if (b.m < c.m) [b, c] = [c, b]
    console.log(a.n, b.n, c.n)
}


// 30
if ( true ) {
    let s = 120
    let t1 = 20
    let t2 = 100
    let t3 = 1

    // problema e np completă și necesită backtracking pentru rezolvare
    // există cazuri în care t1, t2, t3 sunt prime între ele și e nevoie
    // de un număr exact de monede t1, t2 și t3 pentru a rezolva problema.
    // greedy se poate să nu găsim soluție chiar dacă există soluție, deci
    // chiar dacă știm că tot timpul există soluție, nu putem rezolva fără
    // backtracking

    // uu, if we solve this problem I think we break encryption,
    // which in turn breaks the internet
}


// 31
// a)
if ( false ) {
    let a = 5
    let b = 2
    let c = 3

    if (a <= b && a <= c) {
        if (b <= c) {
            console.log(a, b, c)
        } else {
            console.log(a, c, b)
        }
    } else if (b <= a && b <= c) {
        if (a <= c) {
            console.log(b, a, c)
        } else {
            console.log(b, c, a)
        }
    } else {
        if (a <= b) {
            console.log(c, a, b)
        } else {
            console.log(c, b, a)
        }
    }
}
// b)
if ( false ) {
    let a = 5
    let b = 2
    let c = 3

    if (a > b) [a, b] = [b, a]
    if (a > c) [a, c] = [c, a]
    if (b > c) [b, c] = [c, b]
    console.log(a, b, c)
}


// 32
if ( false ) {
    let inToCm = x => x*2.54
    let cmToIn = x => x/2.54

    let galToL = x => x*3.78541
    let lToGal = x => x/3.78541

    let lbToKg = x => x*0.45359
    let kgToLb = x => x/0.45359

    let ftToM = x => x*0.3048
    let mToFt = x => x/0.3048

    let ozToG = x => x*38.3495
    let gToOz = x => x/38.3495

    console.log('13 in to cm = ', inToCm(13))
}


// 33
if ( false ) {
    let a = 1
    let b = 2
    let c = 3

    let d = a
    a = b
    b = c
    c = d

    console.log(a, b, c)
}


// 34
if ( false ) {
    let x = 1331
    let y = (x % 10) * 1000 + (Math.floor(x/10)%10) * 100 + (Math.floor(x/100)%10) * 10 + Math.floor(x/1000)
    if (x === y) {
        console.log('palindrom')
    } else {
        console.log('nu e palindrom')
    }
}


// 35
if ( false ) {
    let an = 1985

    let a = an % 19
    let b = an % 4
    let c = an % 7
    let d = (19 * a + 24) % 30
    let e = (2 * b + 4 * c + 6 * d + 5) % 7

    let z = 22+e+d
    if (z > 31) {
        console.log(z-31, 'Aprilie', an)
    } else {
        console.log(z, 'Martie', an)
    }
}


// 36
if ( false ) {
    let a = 1
    let b = -3
    let c = 2

    let delta = b*b - 4*a*c
    if (delta < 0) {
        console.log('sistemul nu are solutie')
    } else if (delta === 0) {
        console.log('x1=x2=', -b/(2*a))
    } else {
        console.log('x1=', (-b-delta)/(2*a))
        console.log('x2=', (-b+delta)/(2*a))
    }
}


// 37
if ( false ) {
    let a = [30, 50, 45]
    let b = [10, 20, 53]

    let s = a[2] - b[2]
    if (s < 0) {
        s += 60
        a[1]--
    }

    let m = a[1] - b[1]
    if (m < 0) {
        m += 60
        a[0]--
    }

    let g = a[0] - b[0]

    console.log(g, m, s)
}


// 38
if ( false ) {
    let a = 15
    let b = 34
    console.log(Math.floor(a*b/10)%10, a*b%10)
}


// 39
if ( false ) {
    let a = 5
    let b = 6
    let c = 8
    let d = 9

    if (a === b || a === c || a === d || b === c || b === d || c === d) {
        console.log('numerele nu sunt multime')
    } else {
        console.log('numerele sunt multime')
    }
}


// 40
if ( false ) {
    let a = 10
    let b = 3
    let c = 17

    if (a > b) [a, b] = [b, a]
    if (a > c) [a, c] = [c, a]
    if (b > c) [b, c] = [c, b]

    let r = b - a
    if (b + r === c) {
        console.log('numerele sunt în progresie aritmetică')
        console.log(a, b, c)
        console.log('r=', r)
    } else {
        console.log('numerele nu sunt în progresie aritmetică')
    }
}


// 41
if ( false ) {
    let a = 6
    let b = 6
    let c = 2

    if (a > b) [a, b] = [b, a]
    if (a > c) [a, c] = [c, a]
    if (b > c) [b, c] = [c, b]

    if (a + b <= c) {
        console.log('nu este triunghi')
    } else if (a === b && b === c) {
        console.log('triunghi echilateral')
    }  else if (a === b || b === c) {
        console.log('triunghi isoscel')
    } else if (a * a + b * b === c * c) {
        console.log('triunghi dreptunghic')
    } else {
        console.log('triunghi oarecare')
    }
}


// 42
if ( false ) {
    let a = {x: 1, y: 2}
    let b = {x: 7, y: 12}
    let c = {x: 4, y: 7}

    if (a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y) === 0) {
        console.log('points are collinear')
    } else {
        console.log('points are not collinear')
    }
}


// 43
if ( false ) {
    let a = 55
    let b = 40
    let c = 85

    if (a > b) [a, b] = [b, a]
    if (a > c) [a, c] = [c, a]
    if (b > c) [b, c] = [c, b]

    if (a <= 0 || a+b+c !== 180) {
        console.log('nu e triunghi')
    } else {
        if (c > 90) {
            console.log('truinghi obtuz-unghic')
        } else if (c === 90) {
            console.log('triunghi dreptunghic')
        } else if (c <= 90) {
            console.log('truinghi ascuțit-unghic')
        }
    }
}


// 44
if ( false ) {
    let x = -2
    let y = 4

    if (x === 0 && y === 0) {
        console.log('origine')
    } else if (x === 0) {
        console.log('axa Oy')
    } else if (y === 0) {
        console.log('axa Oy')
    } else if (x > 0 && y > 0) {
        console.log('cadranul 1')
    } else if (x < 0 && y > 0) {
        console.log('cadranul 2')
    } else if (x < 0 && y < 0) {
        console.log('cadranul 3')
    } else if (x > 0 && y < 0) {
        console.log('cadranul 4')
    }
}


// 45
if ( false ) {
    let a = 5
    let b = 6
    let c = 9

    if (c < 0) {
        console.log('ecuatie imposibilă')
    } else if (a === 0) {
        if (b === c*c) {
            console.log('o infinitate de solutii')
        } else {
            console.log('ecuatie imposibila')
        }
    } else {
        let x = (c*c-b)/a
        console.log('x=', x)
    }
}


// 46 --- unfinished
if ( true ) {
    let a = 2
    let b = 5
    let c = -37
    let d = 14
    let e = 35
    let f = -259

    // ax + by = c
    // x = (c-by)/a

    // dx + ey = f
    // d ((c-by)/a) + ey = f
    // d (c/a - by/a) + ey = f
    // dc/a - dby/a + ey = f
    // -dby/a + ey = f - dc/a
    // y(-db/a + e) = f - dc/a
    // y = (f-dc/a) / (-db/a + e)

    if ((-d*b/a + e) === 0) {
        console.log('zero')
    }
    let y = (f - d*c/a) / (-d*b/a + e)
    let x = (c - b*y)/a
    console.log(x, y)
}


// 47 --- todo
if ( true ) {

}


// 48
if ( false ) {
    let n = 10

    if (n % 2 === 1) {
        console.log(Math.ceil(n/2))
    } else {
        console.log(-n/2)
    }
}


// 49 --- todo
if ( true ) {

}


// 50 --- todo
if ( true ) {

}


// 51
if ( false ) {
    // 1 0
    // 2 1
    // 4 2
    // 8 3
    // 6 4
    // 2 5

    let x = 259

    if (x === 0) {
        console.log(1)
    } else if (x % 4 === 1) {
        console.log(2)
    } else if (x % 4 === 2) {
        console.log(4)
    } else if (x % 4 === 3) {
        console.log(8)
    } else if (x % 4 === 0) {
        console.log(6)
    }
}


// 52
if ( false ) {
    let a = 124
    let b = 59

    if (b == 0) {
        console.log(1)
    } else {
        let uc = a % 10
        switch (uc) {
            case 0: {
                console.log(0)
            } break

            case 1: {
                console.log(1)
            } break

            case 2: {
                if (b % 4 === 1) {
                    console.log(2)
                } else if (b % 4 === 2) {
                    console.log(4)
                } else if (b % 4 === 3) {
                    console.log(8)
                } else if (b % 4 === 0) {
                    console.log(6)
                }
            } break

            case 3: {
                if (b % 4 === 1) {
                    console.log(3)
                } else if (b % 4 === 2) {
                    console.log(9)
                } else if (b % 4 === 3) {
                    console.log(7)
                } else if (b % 4 === 0) {
                    console.log(1)
                }
            } break

            case 4: {
                if (b % 2 === 1) {
                    console.log(4)
                } else if (b % 2 === 0) {
                    console.log(6)
                }
            } break

            case 5: {
                console.log(5)
            } break

            case 6: {
                console.log(6)
            } break

            case 7: {
                if (b % 4 === 1) {
                    console.log(7)
                } else if (b % 4 === 2) {
                    console.log(9)
                } else if (b % 4 === 3) {
                    console.log(3)
                } else if (b % 4 === 0) {
                    console.log(1)
                }
            }

            case 8: {
                if (b % 4 === 1) {
                    console.log(8)
                } else if (b % 4 === 2) {
                    console.log(4)
                } else if (b % 4 === 3) {
                    console.log(2)
                } else if (b % 4 === 0) {
                    console.log(6)
                }
            } break

            case 9: {
                if (b % 2 === 1) {
                    console.log(9)
                } else if (b % 2 === 0) {
                    console.log(1)
                }
            } break
        }
    }
}


// 53
if ( false ) {
    let u = [
        [0],
        [1],
        [6, 2, 4, 8],
        [1, 3, 9, 7],
        [6, 4],
        [5],
        [6],
        [1, 7, 9, 3],
        [6, 8, 4, 2],
        [1, 9]
    ]

    let a = 2379

    let uc = (base, power) => {
        base = base % 10
        return u[base][power % u[base].length]
    }

    let rez = uc(2, a) + uc(3, a)
        + uc(4, a) + uc(5, a) + uc(6, a) + uc(7, a)
        + uc(8, a) + uc(9, a)

    console.log(rez % 10)
}


// 54 --- nope
if ( false ) {
    // whaat? backtracking again? and string parsing? and while loops?
    // I think this problem should not be here :)
}


// 55
if ( false ) {
    let x = 5.5
    if (x <= -3) {
        console.log(x*x + 1)
    } else if (x < 3) {
        console.log(x - 2)
    } else {
        console.log(x*x - 4*x + 5)
    }
}


// 56
if ( false ) {
    let a = -5
    let b = 9
    let c = 7
    let d = 4

    let accum = 0
    let nrAccumulated = 0
    if (a > 0) {
        accum += a
        nrAccumulated++
    }
    if (b > 0) {
        accum += b
        nrAccumulated++
    }
    if (c > 0) {
        accum += c
        nrAccumulated++
    }
    if (d > 0) {
        accum += d
        nrAccumulated++
    }

    if (nrAccumulated >= 3) {
        if (accum % 2 === 0) {
            console.log(a+b+c+d)
        } else {
            console.log(a*b*c*d)
        }
    }
}


// 57
if ( false ) {
    let a = true
    let b = false
    let c = false
    let d = false
    let e = true

    let x = 3
    let y = 9
    let z = 1

    if (x > y) [x, y] = [y, x]
    if (x > z) [x, z] = [z, x]
    if (y > z) [y, z] = [z, y]

    let accumTrue = 0
    let accumFalse = 0
    if (a) accumTrue++; else accumFalse++
    if (b) accumTrue++; else accumFalse++
    if (c) accumTrue++; else accumFalse++
    if (d) accumTrue++; else accumFalse++
    if (e) accumTrue++; else accumFalse++

    if (accumTrue > accumFalse) {
        console.log(z)
    } else {
        console.log(x)
    }
}


// 58
if ( false ) {
    let a = -1.4
    let b = 6.1
    let c = 5
    let d = -5

    if (c+d > 0) {
        console.log(a+b)
    } else if (c+d === 0) {
        console.log(a-b)
    } else {
        console.log(a*b)
    }
}


// 59
if ( false ) {
    let x = 27.5
    if (x < 5) {
        console.log(x*x - 3)
    } else if (x <= 25) {
        console.log(x+1)
    } else {
        console.log(x*x - 5*x + 6)
    }
}



// 60
// a)
if ( false ) {
    let x = 0
    if (0 < x && x < 1) {
        console.log(x+1)
    } else {
        console.log(x*x - 5*x + 6)
    }
}
// b)
if ( false ) {
    let x = 5
    if (x < 1) {
        console.log(Math.sqrt(x*x + x + 2))
    } else if (x <= 2) {
        console.log(3*x - 1)
    } else {
        console.log((5*x - 2) / (x+2))
    }
}


// 61
if ( false ) {
    let n = 5
    let s = 130

    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }
    if (n > 1) { n--; s /= 2 }

    console.log(s)
}


// 62
if ( false ) {
    let letter = 'X'
    let charCode = letter.charCodeAt(0)

    // abcd -> badc
    // 4 - 16 - 64
    let newCharCode =
        (Math.floor(charCode/16)%4) * 64 +
        Math.floor(charCode/64) * 16 +
        (charCode%4) * 4 +
        (Math.floor(charCode/4)%4)

    console.log(String.fromCharCode(newCharCode))
}


// 63
if ( false ) {
    let year = 2 // 7 bits
    let month = 4 // 4 bits
    let day = 6 // 5 bits

    let code = year

    code <<= 4
    code += month

    code <<= 5
    code += day

    console.log(code)

    day = code & 0b11111
    code >>= 5
    console.log(day)

    month = code & 0b1111
    console.log(month)
    code >>= 4

    year = code
    console.log(year)
}
