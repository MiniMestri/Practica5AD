import subprocess

class Jvdb:
    def __init__(self,basededatos):
        self.basededatos = basededatos
    def insert(self,grupo,documento,contenido):
        self.operacion="insert"
        self.grupo=grupo
        self.documento=documento
        self.contenido=contenido
        ruta='"C:\\Users\\fonsi\\Desktop\\ESTUDIO\\IMF 2\\ACCESO A DATOS\\Practicas\\Practica5AD\\jvdb.exe" '+self.operacion+' '+self.basededatos+' '+self.grupo+' '+self.documento+' "'+self.contenido+'"'
        resultado = subprocess.run(ruta,shell=True,stdout=subprocess.PIPE,text=True)
        if resultado.returncode == 0:
            return("ok")
        else:
            return("ERROR")

conexion1= Jvdb("miempresa")
conexion1.insert("clientes","cliente1","Datos cliente 1")
