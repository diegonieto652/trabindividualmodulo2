#versão 1

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

def filtro(bio,vaga1,vaga2,nome, requis1v1,requis2v1,requis3v1, requis1v2, requis2v2,requis3v2):
    if requis1v1 in bio or requis2v1 in bio or requis3v1 in bio:
        vaga1[nome] = bio
        print('candidato válido para a vaga 1')
    elif requis1v2 in bio or requis2v2 in bio or requis3v2 in bio:
            vaga2[nome] = bio
            print('candidato válido para a vaga 2')

candidatos = {}
vaga1 = {}
vaga2 = {}


print('Digite vaga 1 - para vaga 1 / Digite vaga 2 - para vaga 2')
while True:
    nome = input('Diga seu nome: (Para sair digite 0) ')
    if nome == '0':
        break
    vaga = input('Vaga inscrita? ')
    while vaga != 'vaga 1' and vaga != 'vaga 2':
        vaga = input('Vaga inexistente. Por favor digite: vaga 1 ou vaga 2 ')

    #vaga = input('Vaga desejada ')
    resumo = input('resumo do currículo ').upper()
    candidatos[nome, vaga] = resumo

    filtro(resumo,vaga1,vaga2,nome,'PYTHON', 'PROGRAMAÇÃO','DESENVOLVIMENTO', 'ANÁLISE DE DADOS','DADOS','SQL')



print('vagas',candidatos)
print('vaga1',vaga1)
print('vaga2',vaga2)
print()
aprovadosv1(candidatos)
print('*'*30)
aprovadosv2(candidatos)
print('*'*30)
print('o numero de candidatos aprovados para a vaga 1 é: ',len(vaga1))
print('*'*30)
print('o numero de candidatos aprovados para a vaga 2 é: ',len(vaga2))
print('*'*30)
print('Candidatos aprovados para a vaga 1')
for chave in vaga1:
    print(chave)
print('*'*30)
print('Candidatos aprovados para a vaga 2')
for chave in vaga2:
    print(chave)
