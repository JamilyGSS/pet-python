n1 = float(input("Qual é a primeira nota? "))
n2 = float(input("Qual é a segunda nota? "))
n3 = float(input("Qual é a terceira nota? "))

m = (n1 + n2 + n3)/3
print("A média é",m)
if m >= 6:
    print("Situação: APROVADO!")
else:
    print("Situação: REPROVADO!")