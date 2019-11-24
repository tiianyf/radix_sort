# generate random integer values

from numpy.random import seed
from numpy.random import randint

# seed random number generator
seed(1)

# generate some integers


size = int(input("Tamanho do vetor: "))
lim = int(input("Limite dos números gerados: "))
values = randint(0, lim, size)

array = list(values)
print(array)
