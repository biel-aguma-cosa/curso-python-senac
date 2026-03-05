avaliacao = input("Digite a nota (0.0 - 10.0): ")
presenca = input("Digite a presença (em %): ")

if '%' in presenca:
    presenca.replace('%','')

try:
    if (avaliacao := float(avaliacao)) and (presenca := float(presenca)):

        if avaliacao >= 6 and presenca >= 75:
            print('\naprovado! :D')
        elif avaliacao < 6 and presenca < 75:
            print('\nreprovado! D:')
        else:
            print('\nrecuperação! :(')
except:
    if not avaliacao or not presenca:
        print('você não digitou nada! >:(')
    else:
        print('você não digitou um número! >:O')