import json
import os

dir = (os.path.dirname(__file__))
with open(os.path.join(dir,'dossie.json'),'r') as file:
    people = json.load(file)
    file.close()

def start():
    global people
    os.system('cls')
    match selection := input('SELECIONE UMA OPÇÃO\n1. adicionar usuário\n2. ver usuarios\n3. editar usuário\n4. finalizar\n\n> selecionar: '):
        case '1':
            new_user()
        case '2':
            view_user()
        case '3':
            edit_user()
        case '4':
            return
        case _:
            start()
def new_user():
    global people
    os.system('cls')
    try:
        name = input('NOVO USUÁRIO\nNome:')
        people[name] = {
        'name' : name,
        'email' : input('EMail: '),
        'pass' : input('Senha: '),
        'birth' : [
            int(input("NASCIMENTO\n- Dia: ")),
            int(input("- Mês: ")),
            int(input("- Ano: "))
        ],
        'access' : input("ACESSO\nNível: ")
        }
        with open(os.path.join(dir,'dossie.json'),'w') as file:
            json.dump(people,file)
            file.close()
    except:
        start()
    input(f'\n> USUÁRIO [{name}] ADICIONADO COM SUCESSO')
    start()
def edit_user():
    global people
    os.system('cls')
    people_list = [person for person in people]
    print('SELECIONE UM USUÁRIO')
    for i, user in enumerate(people):
        people_list.append(user)
        print(f'{i+1}. {user}')
    try:
        user = people_list[int(input('\n> usuário: '))-1]
        value = input('\nSELECIONE UM VALOR\n1. nome\n2. email\n3. senha\n4. nascimento\n5. acesso\n6. deletar\n\n> valor: ')
        match value:
            case '1':
                people[user]['name'] = input('> novo valor: ')
                people[people[user]['name']] = people[user]
                del people[user]
            case '2':
                people[user]['email'] = input('> novo valor: ')
            case '3':
                people[user]['pass'] = input('> novo valor: ')
            case '4':
                people[user]['birth'] = [
                    int(input('> novo valor: \n- dia: ')),
                    int(input('- mês: ')),
                    int(input('- ano: '))
                    ]
            case '5':
                people[user]['access'] = input('> novo valor: ')
            case '6':
                del people[user]
            case _:
                edit_user()

        with open(os.path.join(dir,'dossie.json'),'w') as file:
            json.dump(people,file)
            file.close()
        start()
    except:
        edit_user()

def view_user():
    global people
    os.system('cls')
    people_list = [person for person in people]
    print('SELECIONE UM USUÁRIO')
    for i, user in enumerate(people):
        people_list.append(user)
        print(f'{i+1}. {user}')

    try:
        user = people[people_list[int(input('\n> usuário: '))-1]]
        input(f'''
Nome: {user['name']}
Nascimento: {user['birth'][0]}/{user['birth'][1]}/{user['birth'][2]}

EMail: {user['email']}
Senha: {user['pass']}

Nível de acesso: {user['access']}

> ''')
    except:
        view_user()
    start()
start()