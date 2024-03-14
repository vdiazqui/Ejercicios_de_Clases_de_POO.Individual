class A:
    def z(self):
        # Devuelve la instancia actual
        return self

    def y(self, t):
        # Devuelve la longitud de t
        return len(t)

# Crear una instancia de A
aa = A()

# Compara si aa es la misma instancia que una nueva instancia de A()
# Siempre será False, ya que son dos instancias diferentes
result_1 = aa is A()  # False

# Llama a y con una tupla vacía, la longitud de una tupla vacía es 0
result_2 = aa.y(())  # 0

# Llama a y con una tupla que contiene la instancia aa, longitud de 1
result_3 = aa.y((aa,))  # 1

# Llama a y con una tupla que contiene aa y el método z (sin invocar),
# por lo que se cuentan como dos elementos, longitud de 2
result_4 = aa.y((aa, aa.z))  # 2

# Llama a y con una tupla que contiene el método z (sin invocar), el entero 1,
# y la cadena 'z', sumando tres elementos en total, longitud de 3
result_5 = aa.y((aa.z, 1, 'z'))  # 3

# Imprime los resultados
print(result_1, result_2, result_3, result_4, result_5)
