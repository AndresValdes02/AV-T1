#Potencias de números aleatorios
import random

count = 0

while count < 10:
    e = random.randint(1, 5)
    b = random.randint(1, 10)
    result = b**e
    count += 1
    print(result)

