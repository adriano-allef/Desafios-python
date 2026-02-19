carrinho = []
total = 0
while  True:
    try:
        #o codigo vai rodar para sempre
        entrada_nome = str(input("\nDigite o nome do produto: "))

        entrada_preco = input("Digite o preço do produto: ")

        entrada_preco = entrada_preco.replace(",",".")

        preco = float(entrada_preco)

        add_carrinho = {"produto": entrada_nome, "preco": preco}

        carrinho.append(add_carrinho)

        total += preco

    except:
        print("⚠️ Opa! Isso não é um número váido. Tente novamente.")
        continue

    continuar = input("Deseja continuar?s/n")

    if continuar == "s" or continuar == "S":
            print(f"🛒Subtotal {total}")
    else:
        print("\n-----------------------")
        print("\n---O Cupom Fiscal 🧾---\n")
        
        for i in carrinho:
            print(f"Produto: {i['produto']} Preço: {i['preco']}")

        print("\n-----------------------\n")
        print(f"\n🛒 total da compra: {total}")

        while True:
            try:
                valor_recebido = input("\n💰 Valor recebido: ")
                print("\n-----------------------")
                
                valor_recebido = valor_recebido.replace(",",".")
                
                valor_recebido_tratado = float(valor_recebido)
                break
            except:
                print("⚠️ Opa! Isso não é um número váido. Tente novamente.")
                continue

        troco = valor_recebido_tratado - total

            

        print(f"🛒 Total da compra: {total}")
        print(f"💵 Valor pago: {valor_recebido_tratado}")
        print(f"🪙 Troco: {troco}")
            
                
        print("❌Encerrando o sistema...")
        break  # <--- O freio de mão! Quebra o loop.