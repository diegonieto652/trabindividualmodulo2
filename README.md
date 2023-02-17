# Gerenciador de curriculos

Neste código foi criada a função aprovadosv1 e aprovadosv2 que retornam o numero de candidatos aprovados para a vaga 1 e para a vaga 2 e a funão filtro, que faz um filtro com palavra chaves digitadas pelo usuário no resumo do currículo dele fazendo assim com que ele seja inserido na vaga 1 ou na vaga 2 

No corpo do código, dentro do laço de repetição while, é solicitado ao usuário seu nome caso o usuário digite 0 o programa é encerrado por uma condicional

Logo após é perguntado a vaga para qual o candidato deseja se inscrever a resposta é atribuída à variável vaga. abaixo da variável foi criado um laço while em que força o usuário a digita somente o nome das vagas disponívies, pois enquanto ele digita uma vaga não disponível uma mensagem de erro aparece na tela

No próximo passo foi criada a variável resumo, nela o usuário entra com uma mini bio um breve resumo de seu currículo, logo abaixo as variáveis nome e vaga são adicionadas como chaves ao dicionário candidatos e o resumo é adicionado como valor

Logo abaixo é chamada a função filtro, explicada logo acima desse readme

Para finalizar, são printados na tela os resultados 




