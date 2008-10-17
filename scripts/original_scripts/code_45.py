def fac_01(n):
    result = 1
    for i in xrange(2, n+1):
        result *= i
    return result

def fac_02(n):
    value = reduce(lambda i, j : i * j, range(1, n + 1))
    return value

def fac_03(n):
    import operator
    value = reduce(operator.mul, xrange(2, n + 1))
    return value

def fac_04(n):
    fac = lambda n:n-1 + abs(n-1) and fac(n-1)*long(n) or 1
    return fac(n)

def fac_05(n):
    fac = lambda n:[1,0][n&gt;0] or fac(n-1)*n
    return fac(n)

def fac_06(n):
    fac = lambda n:reduce(lambda a,b:a*(b+1),range(n),1)
    return fac(n)

def fac_07(n):
    fac=lambda n: [1, 0][n &gt; 0] or reduce(lambda x, y: x*y, xrange(1,n + 1))
    return fac(n)

def fac_08(n):
    fac = lambda n: n &lt;= 0 or reduce(lambda a, b: a*b, xrange(1,n + 1))
    return fac(n)

def fac_09(n):
    fac = lambda n: [[[j for j in (j * i,)][0] for i in range(2, n+1)][-1] for j in (1,)][0]
    return fac(n)

def fac_10(n):
    fac = lambda n: [j for j in [1] for i in range(2, n+1) for j in [j * i]] [-1]
    return fac(n)
