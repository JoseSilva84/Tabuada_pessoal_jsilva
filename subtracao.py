def subtracao_calculadora():
    print("\n                                           Subtração                                                   \n")
    subtracao = int(input("Digite um número: "))

    contagem = int(11)

    for i in range(1, 11):
        n_subt = i + subtracao
        total = n_subt - subtracao
        print(f"{n_subt} - {subtracao} = {total}")
