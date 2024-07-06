lista_agregar_estudiante=[]

import csv 
def proceso_estudiante():
    with open("ListaCurso5B.csv","r") as archivo:
        datos = csv.DictReader(archivo)
        for dato in datos :
            print(dato)
            

def registrar_estudiante():

    try:
        Rut = int(input("Ingrese rut: "))
        nombre = ""
        while nombre == "":
            nombre = input("Ingrese Nombre :").strip()
            try:
                nombre_t = int(nombre)
                nombre = ""
            except:
                break        
        nota1 = int(input("Ingrese nota1: "))
        nota2= int(input("Ingrese nota2: "))      
        resultado = {"Rut":Rut ,'nombre':nombre,'nota 1':nota1,'nota2':nota2}
        
        
        return resultado
         
    except:
        print("Fallo")
        
def modificar_nota():
    mod=(input("ingrese rut de alumno: "))
    nota =(input("que nota desea eliminar: "))
    if nota == 1:
        pass
    elif nota ==2:
        pass

def eliminar_estudiante():
    elim=(input("ingrese rut de alumno que desea eliminar"))
    
    pass

def generar_promedio():
    pass
    
def cierre_curso():
    pass


def salir_programa():
    print('ingreso terminado')


def programa():
    menu=int(input('1.mostrar estudiantes \n 2.registrar estudiante\n 3. modificar nora \n4.eliminar estudiante \n 5. generar promedio de notas \n 6.generar acta de cierre \n 7. salir \n '))
    return menu 

while True:
    a = programa()
    if a == 1:
        proceso_estudiante()
    elif a == 2:
        lista_agregar_estudiante.append(registrar_estudiante())
    elif a == 3:
        modificar_nota()
        
    elif a == 4:
        eliminar_estudiante()
        
    elif a == 5:
        generar_promedio()
        
    elif a == 6:
        cierre_curso()
    elif a == 7:
        salir_programa()
        break
    else:
       
        print('ingrese un valor valido del menu')
       
       
