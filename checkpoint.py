# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def ListaDivisibles(numero, tope):
    '''
    Esta función devuelve una lista ordenada de menor a mayor con los números divisibles 
    por el parámetro número entre uno (1) y el valor del parámetro "tope"
    Recibe dos argumentos:
        numero: Numero entero divisor
        tope: Máximo valor a evaluar a partir de uno (1)
    Ej:
        ListaDivisibles(6,30) debe retornar [6,12,18,24]
        ListaDivisibles(10,5) debe retornar []
        ListaDivisibles(7,50) debe retornar [7,14,21,28,35,42,49]
    '''
    #Tu código aca:
    lista=[]

    i=1
    while numero*i <= tope:
        lista.append(numero*i)
        i+=1
    
    return lista

def Exponente(numero, exponente):
    '''
    Esta función devuelve el resultado de elevar el parámetro "numero" al parámetro "exponente"
    Recibe dos argumentos:
        numero: El número base en la operación exponencial
        exponente: El número exponente en la operación exponencial
    Ej:
        Exponente(10,3) debe retornar 1000
    '''
    #Tu código aca:
    import math
    resultado = math.pow(numero,exponente)
    return resultado

def ListaDeListas(lista):
    '''
    Esta función recibe una lista, que puede contener elementos que a su vez sean listas y
    devuelve esos elementos por separado en una lista única. 
    En caso de que el parámetro no sea de tipo lista, debe retornar nulo.
    Recibe un argumento:
        lista: La lista que puede contener otras listas y se convierte a una 
        lista de elementos únicos o no iterables.
    Ej:
        ListaDeListas([1,2,['a','b'],[10]]) debe retornar [1,2,'a','b',10]
        ListaDeListas(108) debe retornar el valor nulo.
        ListaDeListas([[1,2,[3]],[4]]) debe retornar [1,2,3,4]
    '''
    #Tu código aca:
    listaNueva=[]
    listaFinal=[]
    if(type(lista) != list):
        return None  
    
    
    for i in range (0,len(lista)):
        
        if(type(lista[i]) != list): 
            
            listaNueva.append(lista[i])
            
        else:
            listaNueva.extend(lista[i])
    
    for i in range (0,len(listaNueva)):
        if(type(listaNueva[i]) == list):
            listaFinal.extend(listaNueva[i])
        else:
            listaFinal.append(listaNueva[i])

    return listaFinal

def Factorial(numero):
    '''
    Esta función devuelve el factorial del número pasado como parámetro.
    En caso de que no sea de tipo entero y/o sea menor que 0, debe retornar nulo.
    Recibe un argumento:
        numero: Será el número con el que se calcule el factorial
    Ej:
        Factorial(4) debe retornar 24
        Factorial(-2) debe retornar nulo
        Factorial(0) debe retornar 1
    '''
    #Tu código aca:
    if(type(numero)!= int or numero < 0):
        return None
    
    factorial=1
    
    while numero >1:
        factorial*=numero
        numero-=1
    return factorial

def ListaPrimos(desde, hasta):
    '''
    Esta función devuelve una lista con los números primos entre los valores "desde" y "hasta"
    pasados como parámetro, siendo ambos inclusivos.
    En caso de que alguno de los parámetros no sea de tipo entero y/o no sea mayor a cero, debe retornar nulo.
    En caso de que el segundo parámetro sea mayor al primero, pero ambos mayores que cero,
    debe retornar una lista vacía.
    Recibe un argumento:
        desde: Será el número a partir del cual se toma el rango
        hasta: Será el número hasta el cual se tome el rango
    Ej:
        ListaPrimos(7,15) debe retornar [7,11,13]
        ListaPrimos(100,99) debe retornar []
        ListaPrimos(1,7) debe retonan [1,2,3,5,7]
    '''
    #Tu código aca:
    if(type(desde) != int or type(hasta) != int or desde <= 0 or hasta <= 0):
        return None
        
    listaPrimos=[]
    
    for i in range(desde,hasta+1):
        esPrimo=True
        j=2
        while(j<=i/2):
            if(i%j == 0):
                esPrimo=False
            j+=1
        if(esPrimo==True):
            listaPrimos.append(i)
        i+=1
        
    return listaPrimos

def ListaRepetidos(lista):
    '''
    Esta función recibe como parámetro una lista y devuelve una lista de tuplas donde cada 
    tupla contiene un valor de la lista original y las veces que se repite. Los valores 
    de la lista original no deben estar repetidos. 
    Debe respetarse el orden original en el que aparecen los elementos.
    En caso de que el parámetro no sea de tipo lista debe retornar nulo.
    Recibe un argumento:
        lista: Será la lista que se va a evaluar.
    Ej:
        ListaRepetidos([]) debe retornar []
        ListaRepetidos(['hola', 'mundo', 'hola', 13, 14]) 
            debe retornar [('hola',2),('mundo',1),(13,1),(14,1)]
        ListaRepetidos([1,2,2,4]) debe retornar [(1,1),(2,1),(4,1)]
    '''
    #Tu código aca:
    if(type(lista) != list):
        return None
        
    listaRepetidos=[]
    listaTuplas=[]
    
    i=0
    j=0
    while i < len(lista):
        j=i+1
        listaRepetidos.append([lista[i],1])
        while j < len(lista):
            if(lista[i] == lista[j]):
                listaRepetidos[i][1] = listaRepetidos[i][1] + 1
                lista.pop(j)
                j-=1
            j+=1
    
        i+=1
        
    i=0
    while i < len(listaRepetidos):
        listaTuplas.append((listaRepetidos[i][0],listaRepetidos[i][1]))
        i+=1
        
    return listaTuplas

def ClaseVehiculo(tipo, color):
    '''
    Esta función devuelve un objeto instanciado de la clase Vehiculo, 
    la cual debe tener los siguientes atributos:
        Tipo:       Un valor dentro de los valores posibles: ['auto','camioneta','moto']
        Color:      Un valor de tipo de dato string.
        Velocidad:  Un valor de tipo de dato float, que debe inicializarse en cero.
    y debe tener el siguiente método:
        Acelerar(): Este método recibe un parámetro con el valor que debe incrementar a la
                    propiedad Velocidad y luego retornarla.
                    Si la propiedad Velocidad cobra un valor menor a cero, debe quedar en cero.
                    Si la propiedad Velocidad cobra un valor mayor a cien, debe quedar en cien.
    Recibe dos argumento:
        tipo: Dato que se asignará al atributo Tipo del objeto de la clase Vehiculo
        color: Dato que se asignará al atributo Color del objeto de la clase Vehiculo
    Ej:
        a = ClaseVehículo('auto','gris')
        a.Acelerar(10) -> debe devolver 10
        a.Acelerar(15) -> debe devolver 25
        a.Acelerar(-10) -> debe devolver 15
    '''
    #Tu código aca:
    class Vehiculo:
        def __init__(self,tipo,color):
            self.tipo = tipo
            self.color = color
            self.velocidad = 0

        def Acelerar(self,acelerar):
            self.velocidad += acelerar

            if(self.velocidad < 0):
                self.velocidad = 0
            elif(self.velocidad > 100):
                self.velocidad = 100
            return self.velocidad

    a = Vehiculo(tipo,color)
    return a 

def OrdenarDiccionario(diccionario_par, clave, descendente=True):
    '''
    Esta función recibe como parámetro un diccionario, cuyas listas de valores tienen el mismo
    tamaño y sus elementos enésimos están asociados. Y otros dos parámetros que indican
    la clave por la cual debe ordenarse y si es descendente o ascendente.
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la
    relación entre los elementos enésimos.
    Recibe tres argumentos:
        diccionario:    Diccionario a ordenar.
        clave:          Clave del diccionario recibido, por la cual ordenar.
        descendente:    Un valor booleano, que al ser verdadero indica ordenamiento descendente y 
                        ascendente si es falso. 
                        Debe tratarse de un parámetro por defecto en True.
    Si el parámetro diccionario no es un tipo de dato diccionario ó el parámetro clave no 
    se encuentra dentro de las claves del diccionario, debe devolver nulo.
    Ej:
        dicc = {'clave1':['c','a','b'],
                'clave2':['casa','auto','barco'],
                'clave3':[3,1,2]}
        OrdenarDiccionario(dicc, 'clave1')          debe retornar {'clave1':['a','b','c'],
                                                                'clave2':['auto','barco','casa'],
                                                                'clave3':[1,2,3]}
        OrdenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1':['c','b','a'],
                                                                'clave2':['casa','barco','auto'],
                                                                'clave3':[3,2,1]}
    '''
    #Tu código aca:
    return 'Funcion incompleta'   
