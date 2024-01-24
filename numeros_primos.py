class MathErr(Exception):
    pass


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


def main():
    number = int( input("Numero entero: ")) 
    if number < 1:
        raise MathErr ("el numero no pude ser menor a 1") 
    if es_primo(number):
        print(f"el {number} es primo")
    else:
        print(f"el {number} No es primo")
    
if __name__ == "__main__":
    main()
    
    