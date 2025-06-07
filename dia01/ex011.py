idade = int(input("Qual é a sua idade? "))
if idade < 18:
    print("Idade :", idade, "\nMenor de idade!")
elif idade >= 18 and idade < 60:
    print("Idade :", idade, "\nAdulto!")
else: 
    print("Idade :", idade, "\nIdoso!")