senha = input('Crie uma senha: ')
while True:
    verifica_senha = input('Digite a senha: ')
    if verifica_senha == senha:
        break
    else:
        print('Senha incorreta, tente novamente!')