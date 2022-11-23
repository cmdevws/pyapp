# Add resources
from __future__ import print_function
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from consulta import *

# Import os 
import os 
import os.path

    
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

#hide unnecessary information
def delProps( obj ):
    del obj['kind']
    del obj['mimeType']
    del obj['id']
    return obj

# main Start
def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
     
    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name, fileExtension, shared, modifiedTime, owners)").execute()
        items = results.get('files', [])

        if not items:
            print('\nNo files found.')
            return
        print('\nFiles:')
        i = 0

        # add word Archivo and number
        for  item in items:

            file = service.files().get(fileId=item['id']).execute()

            file = delProps(file)

            print( 'Archivo ' + str(i + 1) , file )

            i = i + 1
            
        oFile = int(input('\nSelecciona el archivo que quieres guardar:  '))

        # show information of the selected file and the information is saved in the database
        while oFile != 0:
            archivo = items[oFile - 1]
            print('\nHaz Seleccionado el archivo ' + archivo['name'])
            nombre = archivo['name']
            idD = archivo['id']
            extension = archivo['fileExtension']
            owern = archivo['owners']

            for x in owern:
                person = x["displayName"]

            vis = archivo['shared']
            if archivo['shared'] == True:
                vis = 'Publico'
            else:
                vis = 'Privado'

            modificacion = archivo['modifiedTime']
            # Informacion que se actualizara
            print('\n' + nombre + '  |  ' + idD + '  |  ' + extension + '  |  ' + person + ' | ' + vis + '  |  ' + modificacion + '\n')
            # Accion para Insertar la Informacion
            dataBase.validacion(archivo, person, vis)
            break
    
    # exception if an error occurs        
    except HttpError as error:
        #Handle errors from drive API.
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    main()