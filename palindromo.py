# Definición de la clase Palindromos para verificar si un texto es palíndromo.
class Palindromos:
    # Constructor de la clase, inicializa la instancia con el texto a verificar.
    def __init__(self, texto):
        # Almacena el texto proporcionado en una variable de instancia para su uso posterior.
        self.texto = texto

    # Método de instancia para verificar si el texto de la instancia es un palíndromo.
    def esPalindromo(self):
        # Convierte el texto de la instancia a minúsculas para asegurar que la comparación sea insensible a mayúsculas/minúsculas.
        texto_limpiado = self.texto.lower()
        # Compara el texto limpio con su versión invertida para verificar si es palíndromo.
        return texto_limpiado == texto_limpiado[::-1]

    # Método de instancia para mostrar el resultado de la verificación de palíndromo.
    def mostrarResultado(self):
        # Verifica si el texto de la instancia es un palíndromo.
        resultado = self.esPalindromo()
        # Prepara el mensaje según si el texto es o no un palíndromo.
        accion = "es" if resultado else "NO es"
        # Imprime el mensaje indicando el resultado de la verificación.
        print(f"El texto '{self.texto}' {accion} un palíndromo.")
        # Si el texto no es un palíndromo, llama al método destruir para mostrar un mensaje específico.
        if not resultado:
            self.destruir()

    # Método para "destruir" la instancia, en este caso, imprimir un mensaje específico.
    def destruir(self):
        # Imprime un mensaje indicando que el texto se está "eliminando", mostrando el texto en mayúsculas.
        print(f"Eliminando texto: {self.texto.upper()}.")

# Función principal para demostrar el uso de la clase Palindromos con varios ejemplos.
def main():
    # Creación de varias instancias de Palindromos con diferentes textos y muestra de sus resultados.
    verificador1 = Palindromos("Luz azul")
    verificador1.mostrarResultado()

    verificador2 = Palindromos("12321")
    verificador2.mostrarResultado()

    verificador3 = Palindromos("L O L")
    verificador3.mostrarResultado()

    verificador4 = Palindromos("!@#$% %$#@!")
    verificador4.mostrarResultado()

    verificador5 = Palindromos("Ardeyalayedra")
    verificador5.mostrarResultado()

    verificador6 = Palindromos("Arde ya la yedra")
    verificador6.mostrarResultado()

# Verifica si este script es el punto de entrada principal y, de ser así, ejecuta la función main.
if __name__ == "__main__":
    main()
