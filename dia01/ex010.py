a = float(input("Digite o valor de a = "))
b = float(input("Digite o valor de b = "))
c = float(input("Digite o valor de c = "))

delta = b**2 - (4 * a * c)
x1 = (-b + (delta ** (1/2))) / 2 * a
x2 = (-b - (delta ** (1/2))) / 2 * a

print("As raízes dessa equação quadrática são: ", x1, "e",x2)