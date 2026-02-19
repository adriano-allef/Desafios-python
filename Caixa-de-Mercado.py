total = 0
while  True:
    try:
        #o codigo vai rodar para sempre
        entrada = input("Digite o preço do produto:")

        entrada = entrada.replace(",",".")

        preco = float(entrada)

        total += preco
    except:
        print("⚠️ Opa! Isso não é um número váido. Tente novamente.")
        continue

    continuar = input("Deseja continuar?s/n")

    if continuar == "s" or continuar == "S":
            print(f"🛒Subtotal {total}")
    else:
        print(f"💰Total da compra: {total}")
        print("❌Encerrando o sistema...")
        break  # <--- O freio de mão! Quebra o loop.