__author__ = 'Dennis Qiu'

import time, random, math

def mystery1(n):
    '''What is it's big O?''' #1
    sum = 0
    for i in range(0, 10):
        sum += n
    return sum

def mystery2(n):
    '''What is it's big O?''' #n
    sum = 0
    for i in range(0, n):
        sum += i
    return sum


def mystery3(n):
    '''What is it's big O?''' #n^2
    sum = 0
    for i in range(0, n):
        for j in range(0, n):
            sum += i + j
    return sum

def mystery4(n):
    '''What is it's big O?''' #n
    sum = 0
    for i in range(0, n):
        for j in range(0, 25):
            sum += i + j
    return sum

def mystery5(n):
    '''What is it's big O?''' #log n
    sum = 0
    while n >  0:
        sum += n
        n = n // 2     
    return sum

def mystery6(n):
    '''What is it's big O?''' #n log n
    sum = 0
    for i in range(0, n):
        while n >  0:
            sum += n
            n = n // 2     
    return sum

def mystery7(n):
    '''What is it's big O?''' #1
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    div = 3
    while div < math.sqrt(n):
        if n % div == 0:
            return False
        div += 2   
    return True

def mystery8(n):
    '''What is it's big O?''' #n^2
    sum = 0
    for i in range(0, n):
        sum += mystery2(i)
    return sum

#M1 & M7
#M5
#M2 & M4
#M6
#M3 & M8

# let's generate some experimental times
f = open('mystery.csv', 'w', encoding='UTF-8')
print("N       M1          M2          M3          M4          M5          M6          M7          M8")
f.write('N,M1,M2,M3,M4,M5,M6,M7,M8\n')
for n in range(100, 1001, 25):
    start = time.clock()
    result = mystery1(n)
    time1 = time.clock() - start

    start = time.clock()
    result = mystery2(n)
    time2 = time.clock() - start

    start = time.clock()
    result = mystery3(n)
    time3 = time.clock() - start

    start = time.clock()
    result = mystery4(n)
    time4 = time.clock() - start

    start = time.clock()
    result = mystery5(n)
    time5 = time.clock() - start

    start = time.clock()
    result = mystery6(n)
    time6 = time.clock() - start

    start = time.clock()
    result = mystery7(n)
    time7 = time.clock() - start

    start = time.clock()
    result = mystery8(n)
    time8 = time.clock() - start

    print('{:4d}   {:.3e}   {:.3e}   {:.3e}   {:.3e}   {:.3e}   {:.3e}   {:.3e}   {:.3e}'.format(n, time1, time2, time3, time4, time5, time6, time7, time8))
    f.write('{:4d},{:.7f},{:.7f},{:.7f},{:.7f},{:.7f},{:.7f},{:.7f},{:.7f}\n'.format(n, time1, time2, time3, time4, time5, time6, time7, time8))
f.close()
