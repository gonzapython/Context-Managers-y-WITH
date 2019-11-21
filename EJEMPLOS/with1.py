class Prueba_With():
    def __init__(self, numero):
        self.numero = numero

    def __enter__(self):
        print(" *=> AHORA estoy en:  __enter__")

    def __exit__(self, exc_type, exec_value, traceback):
        print("                                               ")
        print(" *=> AHORA estoy en:  __exit__")

    #def imprimir(self):
    #    print(f'El valor introducido es: {self.numero}')

    def __repr__(self):
        return f'      -> El valor introducido es: {self.numero}'


# --------

print("                                               ")
print(" ----------------------------------------------")
print(" ----- Prueba para ver cómo funciona with -----")
print("                                               ")

miwith = Prueba_With(77)

with miwith as wt:
    print(miwith)


print("      -> Fin de la prueba....")
print(" ----------------------------------------------")
print("                                               ")

