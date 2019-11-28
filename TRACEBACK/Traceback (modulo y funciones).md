
traceback- Imprimir o recuperar un seguimiento de pila 
------------------------------------------------------

Código fuente: Lib / traceback.py

Este módulo proporciona una interfaz estándar para extraer, formatear e imprimir rastros 
de pila de programas Python.

El módulo define las siguientes funciones:

    traceback.print_tb(tb, limit=None, file=None)

    traceback.print_exception(etype, value, tb, limit=None, file=None, chain=True)

    traceback.print_exc(limit=None, file=None, chain=True)

    traceback.extract_tb(tb, limit=None)

    traceback.format_exception(etype, value, tb, limit=None, chain=True)

    traceback.format_exc(limit=None, chain=True)

    traceback.format_tb(tb, limit=None)

