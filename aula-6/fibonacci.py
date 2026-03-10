import time
sequence = [0,1]
while len(sequence) < 2000:
    sequence.append(sequence[len(sequence)-1]+sequence[len(sequence)-2])
    print(sequence[len(sequence)-1])
print(len(sequence))
