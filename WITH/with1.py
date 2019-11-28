class Prueba_With():
    def __init__(self, numero):
        self.numero = numero

    def __enter__(self):
        print(" *=> AHORA estoy en:  __enter__")
        self.numero = self.numero + 1
        return

    def __exit__(self, exc_type, exec_value, traceback):
        print("                                               ")
        print(" *=> AHORA estoy en:  __exit__")

    def __repr__(self):
        return f'      -> El valor introducido es: {self.numero} '


# --------

print("                                               ")
print(" ----------------------------------------------")
print(" ----- Prueba para ver cómo funciona with -----")
print("                                               ")

miwith = Prueba_With(77)

with miwith as wt:
    print(miwith)
    print(wt)

print("      -> Fin de la prueba....")
print(" ----------------------------------------------")
print("                                               ")

