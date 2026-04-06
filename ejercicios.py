# Ejercicio 2

# Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente
# constructor que recibe ambos valores.
# ● Definir métodos tales como:
# ○ eje_x
# ○ eje_y
# ○ impresion (método que devuelve en representación de string ambos valores)
# ○ opuesto (método que devuelve el punto opuesto -es decir con los atributos
# negativos-)
# ○ Cualquier otro método que considere importante

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eje_x(self):
        print(f"El eje X es: {self.x}")

    def eje_y(self):
        print(f"El eje Y es: {self.y}")

    def eje_x_negativo(self):
        print(f"Valor negativo de eje x: {-self.x}")

    def eje_y_negativo(self):
        print(f"Valor negativo de eje y: {-self.y}")


p1 = Punto(5, 7)
p2 = Punto(3, 8)

p1.eje_x()
p1.eje_x_negativo()

# Ejercio 3

# Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que
# pasa la línea en un espacio de dos dimensiones.

# La clase dispondrá de los siguientes métodos:
# ● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase
# Punto, que son utilizados para inicializar los atributos.
# ● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
# ● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
# ● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
# ● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique.


class Línea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a
        self._punto_b = punto_b

    def mueve_derecha(self, d):
        self._punto_a.x += d
        self._punto_b.x += d
        print(self._punto_a.x, self._punto_b.x)

    def mueve_izquierda(self, d):
        self._punto_a.x -= d
        self._punto_b.x -= d
        print(self._punto_a.x, self._punto_b.x)

    def mueve_arriba(self, d):
        self._punto_a.y += d
        self._punto_b.y += d
        print(self._punto_a.y, self._punto_b.y)

    def mueve_abajo(self, d):
        self._punto_a.y -= d
        self._punto_b.y -= d
        print(self._punto_a.y, self._punto_b.y)


l = Línea(p1, p2)

l.mueve_abajo(8)


# Ejercicio 4:
# Desarrolla una clase Cancion con los siguientes atributos:
# ● titulo: una variable String que guarda el título de la canción.
# ● autor: una variable String que guarda el autor de la canción.
# Con los siguientes métodos:
# ● Cancion(String, String): constructor que recibe como parámetros el título y el autor de la
# canción (por este orden).
# ● get_titulo(): devuelve el título de la canción.
# ● get_autor(): devuelve el autor de la canción.
# ● set_titulo(String): establece el título de la canción.
# ● set_autor(String): establece el autor de la canción


class Cancion:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def set_titulo(self, titu):
        self.titulo = titu
        return self.titulo

    def set_autor(self, aut):
        self.autor = aut
        return self.autor


c1 = Cancion("Agent Orange", "Sodom")
c2 = Cancion("Frost", "Celtic Frost")

print(c1.get_titulo())
print(c1.get_autor())

print(c2.set_titulo("Goetia"))
print(c2.set_autor("Triptykon"))

# Ejercicio 5:
# ● Crea una clase Libro que modele la información que se mantiene en una biblioteca sobre
# cada libro: título, autor (usa la clase Persona), ISBN, páginas, edición, editorial , lugar
# (ciudad y país) y fecha de edición (como texto). La clase debe proporcionar los siguientes
# servicios: getters y setters, método para leer la información y método para mostrar la
# información.
# ● Este último método mostrará la información del libro con este formato:

# Título: Introduction to Java Programming 3a. edición
# Autor: Liang, Y. Daniel
# ISBN: 0-13-031997-X
# Prentice-Hall, New Jersey (USA)
# viernes 16 de noviembre de 2001
# 784 páginas


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


a1 = Persona("Lucas Perez")


class Libro:
    def __init__(self, titulo, autor, editorial, lugar, ISBN, fecha_edicion, paginas):
        self.titulo = titulo
        self.ISBN = ISBN
        self.autor = autor
        self.editorial = editorial
        self.lugar = lugar
        self.fecha_edicion = fecha_edicion
        self.paginas = paginas

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def set_titulo(self, titulo2):
        self.titulo = titulo2

    def set_autor(self, autor2):
        self.autor = autor2

    def mostrar_info_completa(self):
        print(f"""Título: {self.titulo}
Autor: {self.autor.nombre}
ISBN: {self.ISBN}
{self.editorial}, {self.lugar}
{self.fecha_edicion}
{self.paginas} Paginas""")


li = Libro("Cthulhu", a1, "Mann", "Tailandia",
           "XXXXX", "23 de Enero de 2005", "200")

li.mostrar_info_completa()
