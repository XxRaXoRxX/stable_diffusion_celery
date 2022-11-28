#importar funcion que creara la app
from main import create_app
import os
from dotenv import load_dotenv

#Llamar a la funcion y devolver la app
app = create_app()
#Hacer push sobre el contexto de la aplicacion
#Esto permite acceder a las popiedades de la app
# app.app_context().push()
load_dotenv()

if __name__=='__main__':
    app.run(debug=True, port = os.getenv('PORT'))
##hola
