import sys
import math

LIMITE = 10**7
es_primo = bytearray([1]) * (LIMITE + 1)
es_primo[0] = es_primo[1] = 0
for i in range(2, int(math.isqrt(LIMITE)) + 1):
    if es_primo[i]:
        es_primo[i*i:LIMITE+1:i] = b'\x00' * ((LIMITE - i*i)//i + 1)

primos_prefix = [0] * (LIMITE + 1)
count = 0
for i in range(LIMITE + 1):
    if es_primo[i]:
        count += 1
    primos_prefix[i] = count

datos = list(map(int, sys.stdin.read().split()))
if datos:
    t = datos[0]
    idx = 1
    for _ in range(t):
        a, b = datos[idx], datos[idx+1]
        idx += 2
        if a > b:
            a, b = b, a
        print(primos_prefix[b] - (primos_prefix[a-1] if a > 0 else 0))
