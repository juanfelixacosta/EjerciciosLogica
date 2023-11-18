# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 21:43:12 2023

@author: juanf

A number is requested by keyboard and it is indicated whether the number 
is prime or not.

"""

def prime(number):
    
    count = 0
    dividers = [2,3,5]
    
    for divider in dividers:
        if number % divider == 0:
            count += 1
            if number / divider >= 2:
                count += 1
    
    if count < 2:
        return True
    else:
        return False
    
# Pendiente controlar exception cuando usuario coloca otro caracter en vez de 
# un numero
number = int(input('Indicar un numero: '))

if prime(number):
    print('El numero', number,'es un numero primo')
else:
    print('El numero', number,'NO es un numero primo')