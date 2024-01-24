"""
Author: Luis Enrique Hermenegildo Avendaño
22-01-2024
El algoritmo que puede utilizarse para saber si un número (n) es primo es el de la división.
Se trata de ir probando para ver si tiene algún divisor propio. Para ello, vamos dividiendo el número (n) entre 2, 3, 4, 5,..., n-1. 

Si alguna de las divisiones es exacta y el residuo es cero, se puede afirmar que el número (n) es
compuesto. Si ninguna de estas divisiones es exacta, el número (n) es primo. 

Este método puede hacerse más eficiente  Sólo hay
que dividir entre 2, 3, 4, 5, ... , √𝑛. En realidad, bastaría hacer las divisiones entre los números primos menores o iguales que √𝑛.

Ejemplo: Para probar que 311 es primo sabiendo que √311 = 17.635192 … basta con ver que no es
divisible entre 2, 3, 5, 7, 11, 13 y 17.



"""
from math import sqrt
"""
El operador % realiza la operación módulo entre los números presentes a la izquierda y la derecha.
Se trata de calcular el resto de la división entera entre ambos números. Es decir, 
si dividimos 10 entre 3, el cociente sería 3 y el resto 1. Ese resto es lo que calcula el módulo.
"""


class MathErr(Exception):
    pass

MAX_NUMBER = 250

def residuo(x,y):
    res = x%y
    #print(f"{x} % {y} = {res}")
    return res

def es_primo(num):
    div_exacta = 0
    for i in range(2, num):
        res = residuo(num,i)
        if res == 0:
            div_exacta +=1
    #        print(f"div exacta {res}")
    #print(f"div exacta {div_exacta}")
    if div_exacta == 0:
        return True
    else:
        return False

def file(text):
    f = open("results.txt", "a")
    f.write(text)
    f.close()

def main():
    print(f"numeros primos del 1 al {MAX_NUMBER}")
    numeros_primos=[]
    if MAX_NUMBER < 1:
        raise MathErr ("el numero no pude ser menor a 1") 
    for i in range (1,MAX_NUMBER +1):
        if es_primo(i):
            numeros_primos.append(i)
            #print(f"el {i} es primo")
    
    print(f"numeros primos {numeros_primos}")
    file(str(numeros_primos))
    
if __name__ == "__main__":
    main()
    
    
