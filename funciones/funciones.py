from menssage.menssage import *
from module.DatosJSON import *




#---------------------------------------------------------------------------------------------------------------------------------------
#CASE 1_Camper.................................................................
def getInt(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except Exception:
            print('Opcion Invalida, ingrese un valor valido.')

def getStr(mensaje):
    entrada = str(input(mensaje))
    if entrada.isalpha(): # isAlpha es para el str
        return entrada
    else:
        print("ingrese un caracter valido.")
        return getStr(mensaje)

def getStr1(mensaje):
    return input(mensaje).strip() 

def getDosDigitos(mensaje):
    while True:
        letra = str(getStr(mensaje))
        num = str(getInt("Ingrese el numero: "))
        if len(letra) == 1 and len(num) == 1:
            grupo = letra + num
            return grupo.upper()
        else:
            print("El valor solo permite dos digitos ('M1')")

def pressEnter ():
    print ("Hecho")
    input('Press Enter...........................')



def intDosDigitos(mensaje):
    while True:
        numero = getInt(mensaje)
        cad =str(numero)
        if len(cad)== 2: 
            return cad
        elif len(cad)== 2 and cad[0] == '0': 
            return cad
        elif len(cad)== 4:
            cad = int(cad)
            if (cad >= 1900) and (cad <= 2006):
                return str(cad)
        else : print("El  numero tiene que tener 2 o 4 digitos")

        
def showFind(baseDatos, buscar, mensaje):
    while True: 
        contJ = 0
        for m in baseDatos[buscar].values():
            contJ += 1
            print(f"{contJ}. {m}")
        jor = getInt(mensaje)
        jor = str(jor)  
        if jor in baseDatos[buscar]:
            answer = jor
            return answer
        else:
            print("Valor no válido. Intenta nuevamente.")