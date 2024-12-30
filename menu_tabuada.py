import soma, subtracao, multiplicacao, divisao

print("\n                                   TABUADA                                     \n")

escolha = input("\nMenu:\nSoma = 1\nSubtração = 2\nMultiplicação = 3\nDivisão = 4\n\nEscolha a opção por número: ")

if escolha == "1":
    soma.soma_calculadora()
elif escolha == "2":
    subtracao.subtracao_calculadora()
elif escolha == "3":
    multiplicacao.multiplicacao_calculadora()
elif escolha == "4":
    divisao.divisao_calculadora()
else:
    exit