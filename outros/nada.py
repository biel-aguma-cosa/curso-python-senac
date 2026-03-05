import random
print(x := [
    random.randint(1,10),
    random.randint(1,10),
    random.randint(1,10),
    random.randint(1,10),
    random.randint(1,10)
])
index = random.randint(0,4)
print(f'x[{index}] = {x[index]}')