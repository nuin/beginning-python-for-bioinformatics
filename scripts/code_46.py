#!/usr/bin/env python

import timeit

def fac(n, m):
    result1 = 1
    for i in xrange(2, n + 1):
        result1 *= i
    result2 = 1
    for i in xrange(2, m + 1):
        result2 *= i
    result3 = 1
    for i in xrange(2, (n - m) + 1):
        result3 *= i 

    return  result1 / (result2 * result3) 

def binom(n, m):
    b = [0] * (n + 1)
    b[0] = 1
    for i in xrange(1, n + 1):
        b[i] = 1
        j = i - 1
        while j &gt; 0:
            b[j] += b[j - 1]
            j -= 1
    return b[m] 

def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        #print ntok // ktok
        return ntok // ktok
    else:
        return 0

if __name__ == "__main__":

    stmt = "fac(3000, 7)"
    t = timeit.Timer(stmt = stmt, setup='from __main__ import fac')
    stmt2 = "binom(3000, 7)"
    t2 = timeit.Timer(stmt = stmt2, setup = 'from __main__ import binom')
    stmt3 = "choose(3000, 7)"
    t3 = timeit.Timer(stmt = stmt3, setup = 'from __main__ import choose')

    print 'fac: %.9f' % (t.timeit(100)/100)
    print 'binom: %.2f' % (t2.timeit(10)/10)
    print 'choose %.9f' % (t3.timeit(100)/100)
