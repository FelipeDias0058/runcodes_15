#Cálculo da média
def media(lista):
    return sum(lista) / len(lista) 

    
def main():

    #Os números digitados são adicionados à lista
    lista = []
    
    #Entrada de Dados
    for i in range(100):
        lista.append(int(input()))

    med = media(lista)   

    #Saída de Dados
    print(f'{med:.2f}')

if __name__ == '__main__':
    main()
