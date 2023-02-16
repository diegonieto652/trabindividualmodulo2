def aprovadosv1(candidatos):
    nomechave = 'vaga 1'
    numerochave = 0
    for chave1, chave2 in candidatos:
        if chave2 == nomechave:
            numerochave += 1
    print(f'O número de candidatos inscritos para a vaga 1 é {numerochave}')

def aprovadosv2(candidatos):
    nomechave = 'vaga 2'
    numerochavev2 = 0
    for chave1, chave2 in candidatos:
        if chave2 == nomechave:
            numerochavev2 += 1
    print(f'O número de candidatos inscritos para a vaga 2 é {numerochavev2}')

candidatos = {}
vaga1 = {}
vaga2 = {}

'''opc = int(input('Digite-1 para vaga 1 Digite-2 para vaga2'))

vagas = {1: 'vaga1', 2: 'vaga2'}'''

print('Digite vaga 1 - para vaga 1 / Digite vaga 2 - para vaga 2')
while True:
    nome = input('Diga seu nome: ')
    if nome == '0':
        break
    vaga = input('Vaga inscrita? ')
    while vaga != 'vaga 1' and vaga != 'vaga 2':
        vaga = input('Vaga inexistente. Digite novamente a vaga inscrita: ')

    #vaga = input('Vaga desejada ')
    resumo = input('resumo do currículo ')
    candidatos[nome, vaga] = resumo

    if 'python' in resumo or 'programação' in resumo or 'desenvolvimento' in resumo:
        vaga1[nome] = resumo
        print('candidato válido para a vaga 1')
    elif 'analise de dados' in resumo or 'dados' in resumo or 'sql' in resumo:
            vaga2[nome] = resumo
            print('candidato válido para a vaga 2')

print('vagas',candidatos)
print('vaga1',vaga1)
print('vaga2',vaga2)

aprovadosv1(candidatos)
print('*'*30)
aprovadosv2(candidatos)
print('*'*30)
for chave in vaga1:
    print('o numero de candidatos aprovados para a vaga 1 é: ',len(vaga1))
print('*'*30)
for chave in vaga2:
    print('o numero de candidatos aprovados para a vaga 2 é: ',len(vaga2))

print('*'*30)
print('Candidatos aprovados para a vaga 1')
for chave in vaga1:
    print(chave)
print('*'*30)
print('Candidatos aprovados para a vaga 2')
for chave in vaga2:
    print(chave)