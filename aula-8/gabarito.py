import os

GABARITO = ['b','c','a','e','d']
answers = []
acertos = 0
for i in range(5):
    answers.append(input(f'Resposta {i+1}: ').strip().casefold())
    if answers[i] == GABARITO[i]:
        acertos += 1
sla = {
    True : 'CORRETA',
    False: 'ERRADA'
}

bab = lambda x, y: f' -> {sla[x==y]}\n'

os.system('cls')
print(f'Acertos: {acertos}')
for i in range(5):
    print(f'Resposta {i+1}: {answers[i].upper()} | Gabarito: {GABARITO[i].upper()}',end=bab(answers[i],GABARITO[i]))