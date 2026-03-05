
def func():
    print('''o que vai fazer de manhã?
          dormir / estudar / planejar''')
    m = input('\n> ').casefold()

    print('''o que vai fazer de tarde?
          jogar / treinar / trabalhar''')
    t = input('\n> ').casefold()

    # (X) dormir jogar
    # (X) dormir treinar
    # (X) dormir trabalhar
    # (X) estudar jogar
    # (X) estudar treinar
    # (X) estudar trabalhar
    # (X) planejar jogar
    # (X) planejar treinar
    # (X) planejar trabalhar

    print('\n\n')
    if not m or not t:
        print('você precisa dizer o que vai fazer!')
        input('tente denovo!\n> ')
        return func()
    if 'dormir' in m and 'jogar' in t:
        print('você está desperdiçando seu dia!')
    elif ('estudar' in m or 'planejar' in m) and 'jogar' in t:
        print(f'uma recompensa depois de {m} bastante!')
    elif 'estudar' in m and 'treinar' in t:
        print('que bom, você irá se aperfeiçoar!')
    elif ('estudar' in m or 'planejar' in m or 'dormir' in m) and ('treinar' in t or 'trabalhar' in t):
        print(f'para {t} melhor, você deve {m}')
    else:
        print('o que quiz dizer com isso?')
        input('tente outra resposta!\n> ')
        return func()
    print('\n\n')
func()