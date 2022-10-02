from itertools import product
from random import random

def AND(*a):
    return int(all(a))

def OR(*a):
    return int(any(a))

def NOT(x):
    return int(not x)

def NAND(*a):
    return NOT(AND(*a))

def NOR(*a):
    return NOT(OR(*a))

def XOR(*a):
    s = 0
    for x in a:
        s += x
    if s == 1:
        return 1
    else:
        return 0

def XNOR(*a):
    return NOT(XOR(*a))

def TABLE(f,r=1):
    n = f.__code__.co_argcount
    args = f.__code__.co_varnames[:n]
    print(args)
    for p in assigniter(f,r):
        y = f(*p)
        #s = f.__name__ + ": " + ",".join([f"{a}={v}" for a,v in zip(args,p)])
        #s += f" -> y={y}"
        #print(s)
        print(f"{f.__name__}{p} = {y}")

def EQCHECK(f, g):
    n = f.__code__.co_argcount
    #args = f.__code__.co_varnames[:n]
    res = True
    for p in product([0,1], repeat=n):
        y1 = f(*p)
        y2 = g(*p)
        if not y1 == y2:
            res = False
            print(f"{p}: {f.__name__}={y1}, {g.__name__}={y2}")
    if res:
        print("YES")
    else:
        print("NO")
    return res

def assigniter(f,r=1):
    n = f.__code__.co_argcount
    #args = f.__code__.co_varnames[:n]
    for p in product([0,1], repeat=n):
        if random()>r:
            continue
        yield p


