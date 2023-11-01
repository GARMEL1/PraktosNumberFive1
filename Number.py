a = float(input("Введите число №1: "))
b = float(input("Введите число №2: "))
c = float(input("Введите число №3: "))
if a>=b and a>=c:
  print("Максимальное число №1:", a)
elif b>=a and b>=c:
  print("Максимальное число №2:", b)
else:
  print("Максимальное число №3:", c)