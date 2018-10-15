import numpy as np
import random

# a = np.random.choice(100, 100, replace=True)
# b = np.random.choice(100, 100, replace=True)
a = [random.choice(range(100)) for i in range(10)]
b = [random.choice(range(100)) for j in range(10)]
aa = []
for a_el in a:
    if a_el not in aa:
        aa.append(a_el)
bb = []
for b_el in b:
    if b_el not in bb:
        bb.append(b_el)

c = [aa_el for aa_el in aa if aa_el in bb]

print(a)
print(b)
print(aa)
print(bb)
print(c)