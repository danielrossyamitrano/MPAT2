import json


def salir():
    return 0


def info():
    with open('LICENSE.txt', 'r') as file:
        print('=== Realizado por Daniel Rossy (c) 2020 ===')
        for line in file.readlines():
            print(line, end='')


def abrir_json(ruta, encoding="utf-8"):
    with open(ruta, 'r', encoding=encoding) as file:
        return json.load(file)


__all__ = [
    "salir",
    "info",
    "abrir_json"
]
