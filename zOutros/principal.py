
x = input("Digite um número: ")
y = input("Digite outro número: ")
x = float(x)
y = float(y)
"""
import calculadora
print("Soma = ", calculadora.somar(x, y))
print("Subtração = ", calculadora.subtrair(x, y))
print("Multiplicação = ", calculadora.multiplicar(x, y))
print("Divisão = ", calculadora.dividir(x, y))
print("Resto = ", calculadora.resto(x, y))
print("Exponencial = ", calculadora.exponencial(x, y))
print("Raiz = ", calculadora.raiz(x, y))
"""
"""
from calculadora import somar

print(somar(x, y))
"""
"""
import calculadora as c

print("Soma = ", c.somar(x, y))
print("Subtração = ", c.subtrair(x, y))
print("Multiplicação = ", c.multiplicar(x, y))
print("Divisão = ", c.dividir(x, y))
print("Resto = ", c.resto(x, y))
print("Exponencial = ", c.exponencial(x, y))
print("Raiz = ", c.raiz(x, y))
"""
from calculadora import somar as s

print("Soma = ", s(x, y))