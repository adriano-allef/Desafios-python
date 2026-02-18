pessoas = [
    {
        "nome": "Ronaldo",
        "idade": 15 
    },
    {
        "nome": "Agnaldo",
        "idade": 36 
    },
    {
        "nome": "Cleiton",
        "idade": 24 
    },
    {
        "nome": "Ana",
        "idade": 21 
    },
    {
        "nome": "Luiza",
        "idade": 98 
    }
]

for i in pessoas:
    if i["idade"] >= 18 :
        print("🟩Liberando passagem para: ")
        print(f"{i["nome"]} por que tem {i["idade"]} anos")

