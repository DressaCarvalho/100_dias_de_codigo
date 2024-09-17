def adicao(x,y):
    return x+y

def subtracao(x,y):
    return x-y

def multiplicação(x,y):
    return x*y

def divisao(x,y):
    return x/y

def calculadora():
   print("Selecione a operação.")
   print("1.Adição")
   print("2.Subtração")
   print("3.Multiplicação")
   print("4.Divisão")
   while True:
       escolha = input("Escolha(1/2/3/4):")
       if escolha in ('1','2','3','4'):
            x = int(input("Digite o primeiro numero: "))
            y = int(input("digite o segundo numero: "))
            if escolha == '1':
                print("Resultado: ", adicao(x,y))
            if escolha == '2':
                print("Resultado: ",subtracao(x,y))
            if escolha == '3':
                print("Resultado: ", multiplicação(x,y))
            if escolha =='4':
                if y != 0:
                    print("Resultado: ", divisao(x,y))
                else:
                    print("Não é permitida a divisão por zero")
       else:
           print("EScolha invalida")
       continuar = input("Deseja fazer outra operação? (s/n)")
       if continuar =="n":
        print("Calculadora encerrada")
        break;
calculadora()
   
    
        
                        
    
