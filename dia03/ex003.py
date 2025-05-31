saldo = 1000
while True:
    res = int(input('Digite: \n[1] para sacar \n[2] para depositar \n[3] para mostrar o saldo \n[4] para sair \n'))
    if res == 1:
        saque = float(input('Qual valor você quer sacar? R$'))
        if saque > saldo:
            print('Saldo insuficiente!')
        else:
            saldo -= saque
    elif res == 2:
        deposito = float(input('Qual valor você quer depositar? R$'))
        saldo += deposito
    elif res == 3:
        print(f'O saldo atual é de R${saldo:.2f}\n')
    else:
        break