class Persona:

    def __init__(self, codigo, nombre, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Paciente(Persona):

    def __init__(self, codigo, nombre, edad, dni):
        super().__init__(codigo, nombre, edad)
        self.dni = dni

    def mostrar(self):
        super().mostrar()
        print("DNI:", self.dni)


class Medico(Persona):

    def __init__(self, codigo, nombre, edad, especialidad):
        super().__init__(codigo, nombre, edad)
        self.especialidad = especialidad

    def mostrar(self):
        super().mostrar()
        print("Especialidad:", self.especialidad)


class Consulta:

    def __init__(self, codigo, paciente, medico, motivo):
        self.codigo = codigo
        self.paciente = paciente
        self.medico = medico
        self.motivo = motivo

    def mostrar(self):
        print("Codigo de consulta:", self.codigo)
        print("Paciente:", self.paciente.nombre)
        print("Medico:", self.medico.nombre)
        print("Motivo:", self.motivo)


lista_pacientes = []
lista_consultas = []

paciente1 = Paciente(1, "Juan", 20, 12345678)
lista_pacientes.append(paciente1)

medico1 = Medico(1, "Carlos", 35, "Medicina")

consulta1 = Consulta(1,paciente1,medico1,"Dolor")
lista_consultas.append(consulta1)

while True:

    print("\nPOSTA DE SALUD SAN MIGUEL")
    print("1. Mostrar medico")
    print("2. Agregar nuevo paciente")
    print("3. Registrar Nueva Consulta")
    print("4. Mostrar todas las consultas")
    print("5. Mostrar todos los pacientes")
    print("6. Salir")

    opcion = int(input("Ingrese opcion: "))

    if opcion == 2:
      print("\n--- REGISTRAR NUEVO PACIENTE ---")
      codigo = int(input("Ingrese código: "))
      nombre = input("Ingrese nombre: ")
      edad = int(input("Ingrese edad: "))
      dni = int(input("Ingrese DNI: "))
        
      nuevo_paciente = Paciente(codigo, nombre, edad, dni)
      lista_pacientes.append(nuevo_paciente)
      print("¡Paciente agregado con éxito!")

    elif opcion == 5:
        
        print("\n--- LISTA DE PACIENTES ---")
        if len(lista_pacientes) == 0:
            print("No hay pacientes registrados.")
        else:
            for paciente in lista_pacientes:
                paciente.mostrar()
                print("-" * 20)  

    elif opcion == 3:
        print("\n--- REGISTRAR NUEVA CONSULTA ---")
        
        print("Pacientes disponibles:")
        for p in lista_pacientes:
            print(f"Código: {p.codigo} - Nombre: {p.nombre}")
            
        cod_p = int(input("Ingrese el código del paciente para la consulta: "))
        
        paciente_encontrado = None
        for p in lista_pacientes:
            if p.codigo == cod_p:
                paciente_encontrado = p
                break
        
        if paciente_encontrado != None:
            cod_c = int(input("Ingrese código de consulta: "))
            motivo = input("Ingrese motivo de la consulta: ")
            
            nueva_consulta = Consulta(cod_c, paciente_encontrado, medico1, motivo)
            lista_consultas.append(nueva_consulta)
            print("¡Consulta registrada con éxito!")
        else:
            print("Error: El código de paciente no existe.")

    elif opcion == 4:
      
        print("\n--- LISTA DE CONSULTAS ---")
        if len(lista_consultas) == 0:
            print("No hay consultas registradas.")
        else:
            for consulta in lista_consultas:
                consulta.mostrar()
                print("-" * 20)   

    elif opcion == 1:
        medico1.mostrar()

    elif opcion == 6:
        print("Fin del programa")
        break

    else:
        print("Opcion incorrecta")