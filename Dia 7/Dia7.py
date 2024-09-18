def gerar_tabuada(numero):
    print(f"Tabuada do {numero}")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x  {i} = {resultado}")
# Solicita ao usuario que insira um numero
numero = int(input("Digite um numero para gerar a tabuada:"))

# chama a função para gerar a tabuada
gerar_tabuada(numero)