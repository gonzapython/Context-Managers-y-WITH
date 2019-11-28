
INTENTO de EXPLICACIÓN
----------------------
de los tres parámetros:
 * exception_tye
 * exception_value
 * exception_traceback

del método `__exit__`

`__exit__(self, exc_type, exc_value, exc_traceback):`

PRIMERO
--------
Existe un módulo llamado sys: `sys- Parámetros y funciones específicos del sistema`

Este módulo proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete y a funciones que interactúan con el intérprete. Siempre esta disponible.


SEGUNDO
-------
Existe una función de ese módulo, llamada exec_info(): `sys.exc_info( )`

Esta función devuelve una tupla de tres valores `(type, value, traceback)` que proporcionan información sobre la excepción que se está manejando actualmente. Aquí, "manejar una excepción" se define como "ejecutar una cláusula de excepción". Sólo se puede acceder a la información sobre la excepción que se maneja actualmente.

Si no se maneja ninguna excepción, la tupla vale `(None, None, None)`.

Su significado es: 
 * type: obtiene el tipo de excepción que se maneja
 * value: obtiene el valor de la excepción
 * traceback: obtiene un objeto traceback(**) que encapsula la secuencia de llamadas en el punto
   donde se produjo la excepción originalmente.


** Objetos Traceback (rastreo): Los objetos Traceback(de rastreo) representan un rastreo de una excepción. Un objeto de rastreo se crea implícitamente cuando ocurre una excepción. 


--Referencias:

https://docs.python.org/3/library/sys.html#module-sys

https://docs.python.org/3/reference/datamodel.html#traceback-objects
