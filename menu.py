# Add resourcesr
from main import *
from consulta import*
#Definicion menu
def menu():
     print('Hola, Como te puedo ayudar ? \n')
     print('1. Subir Archivo')
     print('2. Ver Historial')
     print('0. Salir')

menu()

#Input menu
opcion = int(input('\nSelecciona la accion que deseas realizar:  '))

#Validacion de la entrada menu
while opcion != 0:
     if opcion == 1:
          main()
     elif opcion == 2:
          print('\n****************************************')
          print('********* este es el Historial *********')
          print('****************************************\n')
          dataBase.viweHistorial()
     else:
          print('\n*******************************************************')
          print('********* Porfavor escoje una opcion correcta *********')
          print('*******************************************************\n')

     print()
     menu()
     opcion = int(input('Selecciona la accion que deseas realizar:  '))


print('\n************************************************')
print('********* Gracias por usar el programa *********')
print('************************************************\n')