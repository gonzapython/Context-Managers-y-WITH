# Context Managers y WITH
Explicación teórica y programas ejemplo de cómo funcionan los "Context Managers" de WITH


Los "Gestores de Contexto" se encargan de:
 * asignar recursos: método  "__enter__"
 * liberar esos recursos: método  "__exit__"
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

Aplicando todo esto, podemos hacer nuestras propias clases utilizando los context manager "__enter__" y "__exit__":

Una clase para la GESTION de FICHEROS, 

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

  
  -- Fuentes consultadas (he copiado información):
  
    * https://github.com/yasoob/intermediatePython/blob/master/context_managers.rst
      (Merece la pena mirar los repositorios de M.Yasoob Ullah Khalid)
    * https://www.geeksforgeeks.org/context-manager-in-python/
    
    
