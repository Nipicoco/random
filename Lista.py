import os


contacts = list()

for i in contacts:
    i.lower()

class Person:
    def __init__(self, primero, segundo, edad, numero_telefono):
        self.primero = primero
        self.segundo = segundo
        self.edad = edad
        self.numero_telefono = numero_telefono
 
    def nombre_completo(self):
        return f'{self.primero} {self.segundo}'
 
    def __str__(self):
        return f"{self.primero} {self.segundo} : {self.edad} : {self.numero_telefono}"
 



        
input_usuario = ""




print("Welcome to the address book program")


while input_usuario != "0":
    print("Opciones")
    print("1 - Ingresar nuevo contacto")
    print("2 - Mostrar contactos")
    print("3 - Encontrar contacto por nombre")
    #print("4 - Encontrar contacto por id")#POR TERMINAR/Pendiente
    #print("5 - Editar agenda")#POR TERMINAR/Pendiente
    #print("6 - Borrar contacto")#POR TERMINAR/Pendiente
    print("0 - Salir del programa")
    input_usuario = input("Seleccionar opcion: ")
    
    if input_usuario == "1":
        print("Ingresar informacion de contacto")
 
        primer_nombre = input("Primer Nombre = ")
        segundo_nombre = input("Segundo Nombre/Apellido = ")
        edad = input("edad = ")
        numero_telefono = input("Telefono = ")
 
        nuestro_contacto = Person(primer_nombre, segundo_nombre, edad, numero_telefono)
        contacts.append(nuestro_contacto)
        print("Se ha guardado la informacion de contacto")
        
    elif input_usuario == "2":
        for contact in contacts:
            print(contact)
        input("Informacion Mostrada, Enter para continuar")
    elif input_usuario == "3":
        to_lookup = input("Nombre de usuario que desea encontrar\n")
        for contact in contacts:
            if to_lookup in contact.nombre_completo():
                print(contact)
    elif input_usuario.lower() == "0":
        break
 
with open("contactos.txt", "w") as f:
    for contact in contacts:
        f.write(f"{contact.primero},{contact.segundo},{contact.edad},{contact.numero_telefono}\n")


if os.path.isfile("contactos.txt"):
    with open("contactos.txt") as f:
        lista_txt = f.readlines()
        for contact_line in lista_txt:
            contact_data = contact_line.rstrip().split(",")
            contact = Person(contact_data[0],
                             contact_data[1], 
                             contact_data[2],
                             contact_data[3])
            contacts.append(contact)
print("Gracias por usar el libro de contactos.")