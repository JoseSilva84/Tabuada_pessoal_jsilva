def multiplicacao_calculadora():
    print("\n                                           Multiplicação                                                   \n")
    multiplicacao = int(input("Digite um número: "))

    contagem = int(11)

    for i in range(contagem):
        total = multiplicacao * i
        print(f"{multiplicacao} x {i} = {total}")

