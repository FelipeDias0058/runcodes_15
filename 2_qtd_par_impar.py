
def main():

    #Define as variáveis que dizem quantos números pares/impares
    q_par = 0
    q_impar = 0

    #Calcula quantos pares/ímpares entre 100 números digitados
    for num in range(1, 101):
        num = int(input())
        if num % 2 == 0:
            q_par += 1
        else:
            q_impar += 1

    #Saída de Dados
    print(q_par)
    print(q_impar)    


if __name__ == '__main__':
    main()