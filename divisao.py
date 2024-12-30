def divisao_calculadora():
    print("\n                                           Divisão                                                  \n")
    divisao = int(input("Digite um número: "))

    contagem = int(10)
    for i in range(contagem):
        divisao2 = divisao * i
        total = divisao2 // divisao
        print(f"{divisao2} / {divisao} = {total}")

