# Definición de la clase Logger, responsable de gestionar el registro de mensajes en un archivo.
class Logger:
    def __init__(self, filename='log.txt'):
        # Inicialización de la clase Logger con un nombre de archivo predeterminado 'log.txt'.
        self.filename = filename
        # Contador para llevar la cuenta de cuántos mensajes se han registrado.
        self.log_count = 0
        # Apertura (y creación si no existe) del archivo en modo escritura para iniciar el log.
        # Esto borrará el contenido previo del archivo si ya existía.
        with open(self.filename, 'w') as file:
            file.write("--Start log--\n")  # Escritura de la línea inicial en el archivo de log.

    def log(self, mensaje):
        # Método para añadir un mensaje al archivo de log.
        # Cada llamada a este método incrementa el contador de mensajes.
        with open(self.filename, 'a') as file:  # Apertura del archivo en modo 'append' para añadir mensajes.
            file.write(f"{mensaje}\n")  # Escritura del mensaje recibido en el archivo.
        self.log_count += 1  # Incremento del contador de mensajes.

    def __del__(self):
        # Método especial que se llama automáticamente cuando la instancia de Logger se destruye.
        with open(self.filename, 'a') as file:  # Nuevamente, apertura en modo 'append'.
            # Escritura de la línea final que indica el número total de mensajes registrados.
            file.write(f"--End log: {self.log_count} log(s)--")

# Definición de la clase Test, que utiliza un objeto Logger para registrar mensajes.
class Test:
    def __init__(self):
        # Al crear una instancia de Test, se crea también una instancia de Logger.
        self.logger = Logger()

    def llamada(self, mensaje):
        # Método para registrar un mensaje a través del objeto Logger asociado.
        self.logger.log(mensaje)  # Llama al método log de la instancia de Logger.

# Ejemplo de uso de las clases Logger y Test.
def main():
    test = Test()  # Creación de una instancia de Test, lo que a su vez crea una instancia de Logger.
    for i in range(1, 6):  # Bucle para realizar cinco llamadas de prueba.
        if i == 1:
            # Para la primera iteración, se registra un mensaje especial "Primera llamada".
            test.llamada("Primera llamada")
        else:
            # Para las siguientes iteraciones, se registra un mensaje con el número de la llamada.
            test.llamada(f"{i}a llamada")

if __name__ == "__main__":
    main()
