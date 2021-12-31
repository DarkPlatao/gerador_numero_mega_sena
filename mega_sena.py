import random

mega_sena = []
for i in range(6):
    x = random.randrange(1, 61)
    while x in mega_sena:
        x = random.randrange(1, 61)
    mega_sena.append(x)
print(mega_sena)
