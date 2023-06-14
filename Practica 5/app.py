#Importacion del framework a utilizar
from flask import Flask
from flask_mysqldb import MySQL

#Inicializacion de la aplicacion 
app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='dbflask'
mysql=MySQL(app)

#Inicialización de las ruta http://127.0.0.1:5000
@app.route('/') #Se le conoce como ruta index (por ser la unica ruta con esa diagonal)
def index():
    return "Hola Mundo FLASK"

@app.route('/guardar')
def guardar():
    return "Se guardo en la BD"

@app.route('/eliminar')
def eliminar():
    return "Se elimino en la BD"

#Ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
    
