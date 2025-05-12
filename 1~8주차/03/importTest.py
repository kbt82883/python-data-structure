import FindMinMax
from SumRange import sum_range 
import random

A= []
for _ in range(10):
    A.append(random.randint(1,100))

print("(min, max) :", FindMinMax.find_min_max(A))
print(sum_range(A[0],A[9]))