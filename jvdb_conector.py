import subprocess

class Jvdb:
    def __init__(self,basededatos):
        self.basededatos = basededatos
    def insertar(self,grupo,documento,contenido):
        self.operacion="insertar"
        self.grupo=grupo
        self.documento=documento
        self.contenido=contenido
        ruta='"C:\\Users\\fonsi\\Desktop\\ESTUDIO\\IMF 2\\ACCESO A DATOS\\Practicas\\Practica5AD\\codigo.exe" '+self.operacion+' '+self.basededatos+' '+self.grupo+' '+self.documento+' "'+self.contenido+'"'
        resultado = subprocess.run(ruta,shell=True,stdout=subprocess.PIPE,text=True)
        if resultado.returncode == 0:
            return("ok")
        else:
            return("ERROR")
    def eliminar(self,grupo,documento):
        self.operacion="eliminar"
        self.grupo=grupo
        self.documento=documento
        ruta='"C:\\Users\\fonsi\\Desktop\\ESTUDIO\\IMF 2\\ACCESO A DATOS\\Practicas\\Practica5AD\\codigo.exe" '+self.operacion+' '+self.basededatos+' '+self.grupo+' '+self.documento
        resultado = subprocess.run(ruta,shell=True,stdout=subprocess.PIPE,text=True)
        if resultado.returncode == 0:
            return("ok")
        else:
            return("ERROR")
    def buscar(self,grupo,documento):
        self.operacion="buscar"
        self.grupo=grupo
        self.documento=documento
        ruta='"C:\\Users\\fonsi\\Desktop\\ESTUDIO\\IMF 2\\ACCESO A DATOS\\Practicas\\Practica5AD\\codigo.exe" '+self.operacion+' '+self.basededatos+' '+self.grupo+' '+self.documento
        resultado = subprocess.run(ruta,shell=True,stdout=subprocess.PIPE,text=True)
        if resultado.returncode == 0:
            print(resultado.stdout)
            return("ok")
        else:
            return("ERROR")
