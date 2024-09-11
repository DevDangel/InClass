#Declaracion un diccionario
print("DECLARACION UN DICCIONARIO")
conDicDiccionario = dict(nombre = "Angel",edad = 20)
segundaForma = dict([("nombre","Juan"),("edad",30)])
diccinario = {"NOMBRE":"ANGEL","EDAD":44}
print(conDicDiccionario["nombre"])
print(conDicDiccionario["edad"])
print("\n")
print(segundaForma["nombre"])
print(segundaForma["edad"])
print("\n")
print(diccinario["NOMBRE"])
print(diccinario["EDAD"])
#TECNICAS DE ITERACION
print("\n")
print("TECNICAS DE ITERACION")
calificaciones = {
    "Nombre":"Angel",
    "Nota Final":5.0
}
calificaciones = {
    "Sandra":5.0,
    "Miguel":4.0,
    "Messi":4.5,
    "Dibu":2.5
}
for i,j in calificaciones.items():#El método .items() en un diccionario de Python se utiliza para obtener una vista de todos los pares clave-valor en el diccionario. Devuelve una vista que se comporta como un iterable de tuplas, donde cada tupla contiene un par clave-valor.
    print(i,j)
print("\n") 
print("TECNINCAS DE ITERAR LOS DICCIONARIOS")
print("\n")
print("TECNICAS POR CLAVE")
for i in calificaciones.keys():#El método .keys() en un diccionario de Python se utiliza para obtener una vista de todas las claves en el diccionario. 
    print(i)
print("\nITERAR POR VALOR")
for j in calificaciones.values():
    print(j)
print("\n")
nombres = ["Maradona","Messi","Pele","Pedro",]
edades = [22,23,45,30]
for n,e in zip(nombres,edades):
    print("Tu nombre es {0} y tu edad {1}".format(n,e))
print("\n") 
print("RAIZ CUDRADA")  
numero = {x:x**2 for x in(2,4,6)}    
print(numero)
print("\n")
print("IMPRIMIR NUMEROS EN REVERSA")
for i in reversed(range(1,11,1)):
    print(i)
print("\n")
print("BORRAR UN ELEMENTO DEL DICCIONARIO")
del(calificaciones["Miguel"])
for i,j in calificaciones.items():
    print(i,j)