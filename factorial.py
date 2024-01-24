class MathErr(Exception):
    pass

def factorial(x):
    res = 1
    for i in range(1, x+1):
        res= res*i
    return res

def main():
    print("Calculadora Factorial")
    again =True
    while again:
        number = int( input("Numero entero: ")) 
        if number >= 0:
            again = False
            print(f"el factorial de {number}! = {factorial(number)}")    
        else :
            print("El numero no es positivo")   
if __name__ == "__main__":
    main()
    