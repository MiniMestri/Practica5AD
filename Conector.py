from jvdb_conector import Jvdb

def formulario():
    
    global tabla
    global documento
    global cadena
    print("Introduzca nombre de la tabla")
    tabla=input()
    print("Introduzca el nombre del documento")
    documento=input()
    if(dato =="insertar"):
        print("Introduzca su contenido")
        nombre=input("Nombre: ")
        apellidos=input("Apellidos: ")
        edad=input("Edad: ")
        cadena="{nombre: "+nombre+", apellidos: "+apellidos+", edad: "+edad+"}\n"
        
global dato
print("Selecciona la base de datos que desea acceder")
dato = input()
conexion= Jvdb(dato)
print("Desea insertar, eliminar o buscar un registro")
dato=input()
if(dato == "insertar"):
    formulario()  
    conexion.insertar(tabla,documento,cadena)
elif(dato=="eliminar"):
    formulario()
    conexion.eliminar(tabla,documento)
elif(dato=="buscar"):
    formulario()
    conexion.buscar(tabla,documento)
else:
    print("Operacion no completada")
