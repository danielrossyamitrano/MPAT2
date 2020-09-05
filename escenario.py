from util import abrir_json


class Objeto:
    def __init__(self, nombre, habitacion):
        data = abrir_json('objetos.json')[nombre.upper()]
        self.nombre = nombre
        self.habitacion = habitacion
        self.agarrable = data.get('es_agarrable', False)
        uso = data.get('USAR', False)
        if not uso:
            self.uso = "No parece tener ningún uso."
        else:
            self.uso = data['USAR']

        self.examinar = data['EXAMINAR']
        self.accion = data.get('accion', None)
        self.articulo = data.get('articulo', '')
        self.triggers = data.get('triggers', None)

    def __repr__(self):
        return self.nombre

    def usar(self, char, habitacion):
        accion = 'USAR ' + self.nombre.upper()

        for key in self.uso:
            if key == char.posicion:
                habitacion.set_flag(self.uso[key].lower())
                print(habitacion.objetos[self.uso[key]].accion[accion])

            elif key.isupper():
                if key in char.inventario:
                    data = abrir_json('objetos.json')[key]
                    print(data['accion'][accion])
                    new = self.uso[key]

                    char.inventario.replace_item(key, new)


class Habitacion:
    objetos = None
    flags = []

    def __init__(self, nombre):
        self.nombre = nombre
        self.data = abrir_json("habitaciones.json")[nombre]

        self.objetos = {}
        self.base = self.data["des"]
        self.variables = self.data["variables"]
        self.flags = dict(zip(self.variables.keys(), [0] * len(self.variables)))

        for item in self.data["objetos"]:
            self.objetos[item.upper()] = Objeto(item, self)

        print(str(self))

    def __getitem__(self, item):
        if type(item) is str:
            if item not in self.objetos:
                return False
            else:
                return self.objetos[item].agarrable

    def see(self):
        for idx in self.data['on_seen']:
            self.set_flag(idx)

        print(str(self))

    def set_flag(self, key):
        self.flags[key] = 1

    def __str__(self):
        v = self.variables
        return self.base.format(**dict(zip(v.keys(), [v[key][self.flags[key]] for key in v])))
