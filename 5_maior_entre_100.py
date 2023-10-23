#Obtém o maior valor da lista
def maior(lista):
    return max(lista) 

    
def main():

    #Os números digitados são adicionados à lista
    lista = []
    
    #Entrada de Dados
    for i in range(100):
        lista.append(int(input()))

    maior_valor = maior(lista)   

    #Saída de Dados
    print(f'{maior_valor}')

if __name__ == '__main__':
    main()
