'''
Objetivo del programa (descripción del problema que resuelve): Desarrollar un programa de un juego en el que un jugador intente adivinar un numero al azar
de 3 digitos.

Autor/es: Flores Delgado Anahi

Versión: 1

Casos de análisis y prueba (número, estado inicial, transformación, estado final):

Ingrese un numero entero positivo de 3 digitos o enter para finalizar:123
378

Pico 
quedan 6 intentos
Ingrese un numero entero positivo 3 digitos:789

Pico Pico 
quedan 5 intentos
Ingrese un numero entero positivo 3 digitos:456


Panecillos
quedan 4 intentos
Ingrese un numero entero positivo 3 digitos:789

Pico Pico 
quedan 3 intentos
Ingrese un numero entero positivo 3 digitos:456


Panecillos
quedan 2 intentos
Ingrese un numero entero positivo 3 digitos:789

Pico Pico 
quedan 1 intentos
Ingrese un numero entero positivo 3 digitos:456
Perdiste el numero correcto era 378
¿Desea volver a jugar?.Ingrese un numero positivo de 3 digitos o enter para finalizar:

Datos (variables del programa -nombre, propósito, y si son constantes o variables en el programa)

    A solicitar al usuario (sea en el prólogo o sea durante la resolución):
    
    n, valor que el usuario ingresa para adivinar el numero en cadena

    Auxiliares (necesarios para transformaciones intermedias):
    
    c, valor de num en lista de enteros
    d, valor de n en lista de enteros
    e, valor para saber si tiene un digito correcto usando la funcion pico
    f, valor para saber si tiene un digito y posicion correcta usando la funcion fermi
    intentos, numero de intentos que tiene el usuario
    x, variable para determinar la cantidad dedevuelve la longitud de una cadena o el número de elementos de una lista usando la funcion len
    y, variable para determinar la cantidad dedevuelve la longitud de una cadena o el número de elementos de una lista usando la funcion len
    
    Resultados (a informar sea durante el desarrollo o en el epílogo):
    num, numero al azar que el usuario debe adivinar el usuario
    


'''
# Funciones

import random
def numero():       #Obtiene un numero al azar en cadena
    a=random.randint(100, 999)
    b=str(a)
    return b

def lista(b):     #Convierte el numero en una lista de enteros
    lista=[]
    for i in b:
        i=int(i)
        lista.append(i)
    return lista

#1 PRÓLOGO
#1.1 Presentación
#1.1.1 Impresión del título del programa en pantalla
print('Panecillos')
print()
#1.1.2 Descripción o aclaraciones al usuario (opcional)
print('Se solicita al usuario adivinar un numero al azar teniendo en cuenta que sean positivos y de 3 digitos')
print('el programa le informara si el numero ingresado es correcto con las siguientes pistas:')
print()
print('Pico             Un dígito es correcto pero en la posición incorrecta.')
print('Fermi            Un dígito es correcto y en la posición correcta.')
print('Panecillos       Ningún dígito es correcto.')
print()
print('Si el programa muestra en pantalla 2 o 3 veces pico o fermi, significa que mas de un digito ingresado es el correcto y esta en la pocision correcta')
print('tienes 7 intentos')

#1.2 Datos iniciales 
#1.2.1 Solicitud e ingreso de datos desde teclado (opcional, si los datos se piden durante la resolución)


#1.2.2 Establecimiento de valores iniciales para datos auxiliares o que se transformarán en resultados (opcional)

#2 RESOLUCIÓN
# Descomposición del problema en subproblemas 2.x que a su vez pueden requerir ingreso o inicialización de datos o mostrar resultados

n=input('Ingrese un numero entero positivo de 3 digitos o enter para finalizar:')

    
while n!='' :
    num=numero()
    print(num)       
    c=lista(num)
    intentos=7
    while n!=num and intentos!=1: #condicion para saber si el valor ingresado es correcto o la cantidad de intentos que quedan
        d=lista(n)
        lista1=[]
        lista2=[]
        indice=0
        for j in d:   #condion para saber si un algun digito esta en la posicion correcta
            j==d[indice]
            if j==c[indice]:
                lista2.append(j)
            indice+=1
        y=len(lista2)
                 
        for i in d: #condicion para saber si un algun digito pertenece al numero correcto
            if i in c:
                lista1.append(i)
        x=len(lista1)
        z=x-y
        print(y*'Fermi ')
        print(z*'Pico ')
        
        if x==0:    #Condicion para saber si ningun digito pertenece al numero correcto
            print('Panecillos')
            
        intentos=intentos-1
        print('quedan',intentos,'intentos')
        n=input('Ingrese un numero entero positivo 3 digitos:')
    

    if n==num:
        print('Ganaste,el numero correcto es',num)
    else:
        print('Perdiste el numero correcto era',num)
        

    n=input('¿Desea volver a jugar?.Ingrese un numero positivo de 3 digitos o enter para finalizar:')
    
    




#3 EPÍLOGO

#3.2 Finalización (pausa para ver resultados en pantalla que se puede obviar, si los resultados se van mostrando durante la resolución)
print() # salto de línea
input('Pulse tecla de ingreso para terminar el programa...') # pausa forzada

            




