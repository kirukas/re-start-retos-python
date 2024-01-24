class MathErr(Exception):
    pass


def residuo(x,y):
    res = x%2
    print(f"{x} % {y} = {res}")
    return res

def pares_impares(num):
    pares =0
    impares = 0
    for i in range(1, num+1):
        if residuo(i,2) == 0:
            pares+=1
        else:
            impares+=1
    return pares, impares

def main():
    print("Contador de numeros impares")
    number = int( input("Numero entero: ")) 
    if number < 1:
        raise MathErr ("el numero no pude ser menor a 1") 
    pares, impares = pares_impares(number)
    print(f"Numeros pares {pares}")
    print(f"Numeros impares {impares}")
if __name__ == "__main__":
    main()