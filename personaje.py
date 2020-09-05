from escenario import Objeto


class Personaje:
    def __init__(self):
        self.inventario = Inventario()
        self.posicion = 'recibidor'

    def este(self):
        if self.posicion == 'recibidor':
            self.posicion = 'sala'
        elif self.posicion == 'sala':
            print('la pared se pone en tu camino')

        return self.posicion

    def oeste(self, habitacion):
        if self.posicion == 'recibidor':
            if habitacion.flags['puerta'] == 1:
                print('has logrado salir! fin del juego')
            else:
                print('la puerta está cerrada')
        elif self.posicion == 'sala':
            self.posicion = 'recibidor'

        return self.posicion

    def agarrar(self, objeto):
        self.inventario.incorporar(objeto)

    def mirar(self, habitacion):
        if habitacion.nombre == self.posicion:
            habitacion.see()

    @staticmethod
    def examinar(objeto):
        print(objeto.examinar)

    def usar(self, nombre, habitacion):
        if nombre in habitacion.objetos:
            objeto = habitacion.objetos[nombre]
        elif nombre in self.inventario:
            objeto = self.inventario[nombre]
        else:
            return

        objeto.usar(self, habitacion)


class Inventario:
    def __init__(self):
        self._contenido = []

    def __contains__(self, item):
        if type(item) is str:
            return item in [i.nombre.upper() for i in self._contenido]
        else:
            return item in self._contenido

    def __getitem__(self, item):
        if type(item) is str:  # by name
            idx = [i.nombre for i in self._contenido].index(item.title())
            return self._contenido[idx]

    def replace_item(self, old, new):
        old_item = self[old]
        new_item = Objeto(new, old_item.habitacion)
        self._contenido[self._contenido.index(old_item)] = new_item

    def __call__(self):  # ver el inventario
        print('Tienes ' + ', '.join([i.articulo + ' ' + i.nombre.lower() for i in self._contenido]))

    def incorporar(self, objeto):  # añadir objetos al inventario.
        self._contenido.append(objeto)

    def usar(self, objeto):  # usar un objeto desde el inventario
        if objeto in self._contenido:
            objeto.usar()
