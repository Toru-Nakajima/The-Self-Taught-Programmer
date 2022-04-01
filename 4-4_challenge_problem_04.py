"""
Retuns n/2 and m*4.
:param n: float.
:param m: float.

:def div_it:
:input: n.
:print: n/2.

:def mul_it: 
:m = n.
:print: m*4.
"""

m = 1
n = 2

def div_it():
    global n
    n = input("type a number:")
    n = float(n)
    n = n / 2
    print(n)

def mul_it():
    global m,n
    m = n
    m = m * 4
    print(m)


div_it()
mul_it()


