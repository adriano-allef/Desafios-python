while True:
    try:
        idade = int(input("Qual sua idade?"))
    
    except:
        print("⚠️ Digite apenas números🔢!)")
        continue
    
    print(f"Idade registrada: {idade} anos.")
    break