# Add resources
import pymysql
from getpass4 import getpass

# Information needed to connect the database
print('Para Iniciar porfavor escribe los siguentes datos')
dbName = input('nombre base de datos: ')
dbUser = input('Usuario base de datos: ')
dbCont = getpass('Contraseña base de datos: ')


# function creation
class DataBase:
     def __init__(self):

          try:
               self.connection = pymysql.connect(
                    host='localhost',
                    user= dbUser,
                    password= dbCont,
                    db= dbName
               )

               self.cursor = self.connection.cursor()

               print('')
               print('')
               print('************************************')
               print('********* Conexion Exitosa *********')
               print('************************************')
               print('')
               print('')

          except pymysql.Error as er:
               print(er)         
               print('oh no, existe un problema de conexion')

     # validar data to database MySQL

     def validacion( self, archivo, person, vis ):

          sql = 'SELECT idDrive FROM datos'

          try:
               self.cursor.execute(sql)
               info = self.cursor.fetchall()

               for i in info:
                    if i[0] == archivo['id']:
                         val = True
                         break
                    else:
                         val = False

               if val == True:
                    print('No es posible Insertar este registro porque ya existe')
               else:
                    # Add data to database MySQL
                    sql = """
                    insert into `datos` (idDrive, nombre, extension, owner, visibilidad, modificacion)
                    values (%s, %s, %s, %s, %s, %s) 
                    """

                    try:
                         self.cursor.execute(sql , (archivo['id'], archivo['name'] , archivo['fileExtension'] , person , vis , archivo['modifiedTime']))
                         print ('\nEl archivo se subio correctamente')
                         self.connection.commit()
                    except pymysql.Error as er:
                         print(er)
                         print("Error al insertar en la base de datos")
          except pymysql.Error as er:
               print(er)
               print("Error al consultar los datos")
          

     def viweHistorial( self ):    

          sql = 'SELECT * FROM datos'

          try:
               self.cursor.execute(sql)
               info = self.cursor.fetchall()

               for i in info:
                    print('idDrive: ', i[1] + ' | ' + 'nombre: ', i[2] + ' | ' + 'extension: ', i[3] + ' | ' + 'owner: ', i[4] + ' | ' + 'visibilidad: ', i[5]+ ' | ' + 'modificacion: ', i[6] + '\n')
          except pymysql.Error as er:
               print(er)
               print("Error al consultar los datos")
          
dataBase = DataBase()