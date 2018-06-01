# solving for n lg n = 40000
from math import log
__author__ = 'Dennis Qiu'
epp = 1e-5
n = 1
while n * log(n,2) < 40000:
    n += 1
print('{:,.3f} * log({:,.3f}, 2) = {:,.3f}'.format(n, n, n*log(n,2)))
n -= 10
while n * log(n,2) - 40000 < epp:
    n += epp
print('{:,.3f} * log({:,.3f}, 2) = {:,.3f}'.format(n, n, n*log(n,2)))


print('\nSome powers to know (5, 6, 9, 10, 14, 15, 20):\nn\t2**n\t\tlg(n)')
for i in (5, 6, 9, 10, 14, 15, 20):
    print('{}\t{:6,}  \t{}'.format(i, 2**i, log(2**i, 2)))
print('\n\n')
for i in range(21):
    print('{}\t{:6,}  \t{}'.format(i, 2**i, log(2**i, 2)))
