import sqlite3 as sql
from tkinter import *

class Security:

    def __init__(self, hello):
        self.hello = hello

        self.get_name()
        self.password()

    def get_name(self):
        print(self.hello)
        self.enter_name = input("Ingresa tu nombre: ")

    def password(self):
        self.enter_password = input(f"{self.enter_name}, por favor ingrese una contraseña nueva para crear: ")

        if len(self.enter_password) >= 8:
            for i in self.enter_password:
                if "$" in i:
                    print("Contraseña creada")
                    self.login = input("Ingrese su contraseña para acceder: ")
                    break
            else:
                print(f'La contraseña {self.enter_password} debe tener al menos un "$"')
        else:
            print(f"La contraseña {self.enter_password} es menor de 8 carácteres")

        try:
            if self.login == self.enter_password:
                print("Acceso concedido")
            else:
                print("Acceso denegado")
        except AttributeError:
            pass

if __name__ == '__main__':
    app = Security("Hola usuario bienvenido o bienvenida")
