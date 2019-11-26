PRIMERO:
--------
Existe un módulo llamado sys

sys- Parámetros y funciones específicos del sistema 

Este módulo proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete. Siempre esta disponible.


SEGUNDO
-------
Existe una función de ese módulo, llamada exec_info()

sys.exc_info( ) 

Esta función devuelve una tupla de tres valores que proporcionan información sobre la excepción
que se está manejando actualmente. 
La información devuelta es específica tanto para el subproceso actual como para el marco de pila actual. 
Si el marco de la pila actual no está manejando una excepción, la información se toma del marco de la
pila que llama, o de su llamador, y así sucesivamente hasta que se encuentra un marco de la pila 
que maneja una excepción. Aquí, "manejar una excepción" se define como "ejecutar una cláusula de excepción". 
Para cualquier marco de pila, solo se puede acceder a la información sobre la excepción que
se maneja actualmente.

Si no se maneja ninguna excepción en ninguna parte de la pila, se devuelve una tupla que contiene
tres valores "None". De lo contrario, los valores devueltos son (type, value, traceback).
Su significado es: 
 * type: obtiene el tipo de excepción que se maneja (una subclase de ); 
 * value: obtiene la instancia de excepción (una instancia del tipo de excepción);
 * traceback: obtiene un objeto traceback(**) que encapsula la pila de llamadas en el punto donde se produjo
la excepción originalmente.


** Objetos Traceback (rastreo): Los objetos Traceback(de rastreo) representan un rastreo de pila de una excepción. Un objeto de rastreo se crea implícitamente cuando ocurre una excepción.
