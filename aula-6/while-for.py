x = int(input('input: '))
results = []

while len(results) < 10:
    for i in range(1,x):
        results.append(x*i)

if 10 // x != 0:
    lines = [results[:9],results[9:]]
else:
    lines=[results,[0 for i in range(x)]]

for i in range(9):
    text = ""
    try:
        if lines[0][i] < 10:
            text = f' {lines[0][i]} | '
        else:
            text = f'{lines[0][i]} | '
        
        if lines[1][i] < 10:
            text += f' {lines[1][i]}'
        else:
            text += f'{lines[1][i]}'
    except:
        if lines[0][i] < 10:
            text = f' {lines[0][i]} | ??'
        else:
            text = f'{lines[0][i]} | ??'
    print(text)