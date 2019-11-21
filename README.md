# Context-Managers-y-WITH
Explicación teórica y programas ejemplo de cómo funcionan los "Context Managers" de WITH


Los "Gestores de Contexto" se encargan de:
 * asignar recursos: método  __enter__
 * liberar esos recursos: método  __exit__
cuando es necesario.

El ejemplo típico es el de WITH, que permite ejecutar dos operaciones relacionadas.
Ejemplo:

    with open('fichero1', 'w') as file:

        fichero1.write('Hola q tal!')

En éste código:

 * se abre el archivo
 
 * se escribe "Hola q tal!" en él
 
 * se cierra.
 
 
Sería equivalente a:

    file = open('some_file', 'w')

    try:

        file.write('Hola!')

    finally:

        file.close()

Aplicando todo esto, podemos hacer nuestras propias clases:

 1.)- Una clase para la gestión de ficheros, con los context manager  __enter__ y __exit__:

    class FileManager(): 

        def __init__(self, filename, mode): 

            self.filename = filename 

            self.mode = mode 

            self.file = None

        def __enter__(self): 

            self.file = open(self.filename, self.mode) 

            return self.file

        def __exit__(self, exc_type, exc_value, exc_traceback): 

            self.file.close() 
          

  #Escribir en el fichero
  
    with FileManager('fichero1.txt', 'w') as f: 

        f.write('Esto es un Test.....') 


 2.)- Una clase para la gestión de la conexión a MongoDB, con los context manager __enter__ y __exit__:
 
    from pymongo import MongoClient 

    class MongoDBConnectionManager(): 

        def __init__(self, hostname, port): 

            self.hostname = hostname 

            self.port = port 

            self.connection = None

        def __enter__(self): 

            self.connection = MongoClient(self.hostname, self.port) 

            return self

        def __exit__(self, exc_type, exc_value, exc_traceback): 

          self.connection.close() 

  #Conexión al localhost 
  
    with MongoDBConnectionManager('localhost', '27017') as mongo: 

        collection = mongo.connection.SampleDb.test 

        data = collection.find({'_id': 1}) 

        print(data.get('name')) 
    
  
  Al ejecutar el bloque with, se ejecutan las siguientes operaciones:
  
    * Se crea un objeto MongoDBConnectionManager con localhost como nombre de hostname y 27017 como puerto, cuando se ejecuta el método
      __init__.
      
    * El método __enter__ abre la conexión mongodb y devuelve el objeto MongoDBConnectionManager a la variable mongo.
    
    * Se accede a la colección de prueba en la base de datos SampleDb y se recupera el documento con _id = 1. Se imprime el campo de
      nombre del documento.
      
    * El método __exit__ se encarga de cerrar la conexión al salir del bloque with.
  
  ==> NOTA: esto es muy usado en Big Data (sábados por la mañana...con sueño)
