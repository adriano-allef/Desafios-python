pessoas = []


for i in range(2):
    nome = input("Qual seu nome?")
    idade = int(input("Qual sua idade?"))
    dados_temporarios =  { "nome": nome, "idade": idade}
    pessoas.append(dados_temporarios)
    
print(pessoas)