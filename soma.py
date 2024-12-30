def soma_calculadora():
    print("\n                                           Soma                                                   \n")
    multiplicador = int(input("Digite um número: "))

    contagem = int(11)

    for i in range(contagem):
        total = multiplicador + i
        print(f"{multiplicador} + {i} = {total}")
