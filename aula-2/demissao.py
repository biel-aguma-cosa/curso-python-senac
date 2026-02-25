company = input('Empresa: ')
manager = input('Gestor/Responsável: ')
role = input('Cargo atual: ')
date = [
    [
        input('PERIODO DE\n- dia:'),
        input('- mês:'),
        input('- ano:')
    ],
    [
        input('A:\n- dia:'),
        input('- mês:'),
        input('- ano:')
        ]
]
location_date = [
    input('Local: '),
    [
        input('DATA ATUAL:\n- dia:'),
        input('- mês:'),
        input('- ano:')
    ]
]
signature = input('assinatura: ')
name = input('nome completo: ')

print(
f'''
\n\n\n
À {company}

Presado(a) {manager}.
Venho por meio desta carta comunicar formalmente
o meu pedido de demissão do cargo de: {role}.
Estarei a disposição da empresa, no período de {date[0][0]}/{date[0][1]}/{date[0][2]} a {date[1][0]}/{date[1][1]}/{date[1][2]}

{location_date[0]}, {location_date[1][0]}/{location_date[1][1]}/{location_date[1][2]}
{signature}

{name}
''')