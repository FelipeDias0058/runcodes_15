
def main():
    #Exibe na tela uma lista de 10 em 10 números, até 1000.
    for i in range(10, 1001, 10):
        if i == range(10, 1001, 10)[-1]:
            print(i, end = '.')
        else:
            print(i, end = ', ')


if __name__ == '__main__':
    main()
