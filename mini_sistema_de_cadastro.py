'''
O Grande Desafio Final 🏆
Você já tem todas as "Joias do Infinito" da programação básica:

Variáveis (nome = "Adriano")

Interação (input, print)

Condicionais (if/else)

Listas ([ ])

Loops (for)

Funções (def)

Dicionários ({ })

Vamos juntar tudo isso para construir um Mini Sistema de Cadastro? É aqui que a programação vira "vida real".

Imagine que queremos guardar os dados de várias pessoas.
No passo anterior, colocamos uma lista dentro de um dicionário.
Agora, vamos inverter: vamos colocar dicionários dentro de uma lista.

Seu Desafio:

Crie uma lista vazia chamada usuarios.

Crie um dicionário chamado pessoa1 com chaves "nome" e "idade" (invente os dados).

Crie um segundo dicionário pessoa2 com dados diferentes.

Adicione (use o .append()) esses dois dicionários dentro da lista usuarios.

Mande imprimir a lista usuarios.

(Dica: É como guardar várias fichas cadastrais dentro de uma única pasta).
'''
usuarios = []

pessoa1 = {
    "nome": "Rafael",
    "idade": 36
}

pessoa2 = {
    "nome": "Suzi",
    "idade": 16
}


usuarios.append(pessoa1)
usuarios.append(pessoa2)

print(usuarios)