
# -*- coding: utf-8 -*-
# Equação do Segundo Grau

# a2 + bx + c
# ((-b)+-sqtr(b2-4ac))/2

from math import sqrt

a = input ("Insira o numero de a: ")
b = input ("Insira o numero de b: ")
c = input ("Insira o numero de c: ")

delta = b**2 -4*a*c
raiz_delta = sqrt(delta)

x1 = (-b + raiz_delta)/2*a
x2 = (-b - raiz_delta)/2*a

print ("x1 = %d" %x1)
print ("x2 = %d" %x2)