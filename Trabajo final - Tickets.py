# Trabajo final 1: App de tickets

import random

# Cargar Tickets desde el archivo

def cargar_tickets():
    tickets = {}

    try:
        with open('tickets.txt', "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if not linea:
                    continue

                numero, nombre, sector, asunto, problema = linea.split("|")

                tickets[int(numero)] = {
                    "nombre": nombre,
                    "sector": sector,
                    "asunto": asunto,
                    "problema": problema
                }
    except FileNotFoundError: # Si el archivo no existe
        with open('tickets.txt', "w", encoding="utf-8") as archivo:
            pass 

    return tickets

# Guardar Tickets en el archivo

def guardar_tickets(tickets):
    tickets_existentes = cargar_tickets()

    with open('tickets.txt', "a", encoding="utf-8") as archivo:
        for numero, t in tickets.items():
            if numero not in tickets_existentes:
                linea = f"{numero}|{t['nombre']}|{t['sector']}|{t['asunto']}|{t['problema']}\n"
                archivo.write(linea)

# Carga Tickets
tickets = cargar_tickets()

# Alta de Tickets

def alta_ticket():
    global tickets
    while True:
        print(f"\nIngrese los datos para generar un nuevo Ticket")

        nombre = input("Ingrese su Nombre: ")
        sector = input("Ingrese su Sector: ")
        asunto = input("Ingrese Asunto: ")
        problema = input("Ingrese un Mensaje: ")

        numero = random.randint(1000, 9999)

        tickets[numero] = {
            "nombre": nombre,
            "sector": sector,
            "asunto": asunto,
            "problema": problema
        }

        guardar_tickets(tickets)

        # Muestra de Ticket
        linea = "=" * 60
        print(f"\n{linea}\n             Se generó el siguiente Ticket\n{linea}")
        print(f"\n   Su nombre: {nombre}      N°Ticket: {numero}")
        print(f"   Sector: {sector}")
        print(f"   Asunto: {asunto}\n")
        print(f"   Mensaje: {problema}\n")
        print("             Recordar su numero de Ticket\n")

        seguir = input("¿Desea generar un nuevo Ticket? (s/n): ").lower()
        if seguir != "s":
            break

# Leer Tickets 

def leer_ticket(tickets):
    print("\nLectura de Tickets")

    # Si no hay Tickets guardados
    if not tickets:
        print("\nNo hay tickets guardados.")  
        while True:
            opcion = input("\n¿Querés volver al menú (v) o salir (s)?: ").lower()
            
            if opcion == "v":
                return 
            elif opcion == "s":
                print("Programa finalizado.")
                exit()
            else:
                print("Opción inválida. Ingrese 'v' o 's'.")

    while True:
        numero = input("\nIngrese el número del Ticket: ")
        if not numero.isdigit():
            print("Debe ingresar un número válido.")
            continue
        
        numero = int(numero)
        if numero in tickets: # Muesra de Tickets guardados
            t = tickets[numero]
            linea = "=" * 60
            print(f"\n{linea}\n               Información del Ticket \n{linea}")
            print(f"\n  Nombre: {t['nombre']}       N°Ticket: {numero}")
            print(f"  Sector: {t['sector']}")
            print(f"  Asunto: {t['asunto']}\n")
            print(f"  Mensaje: {t['problema']}\n")
        else: # No existe el Ticket
            print(f"\nEl Ticket número {numero} no existe.")

        while True:
            seguir = input("¿Desea leer otro Ticket? (s/n): ").lower()

            if seguir == "s":
                break   
            elif seguir == "n":
                return   
            else:
                print("Respuesta inválida. Ingrese 's' o 'n'.\n")    

# Menú general

def menu():
    while True:
        print("\nHola bienvenido al sistema de Tickets\n\n")
        print("1 - Generar un Nuevo Ticket")
        print("2 - Leer un Ticket")
        print("3 - Salir")

        opcion = input("Seleccione: ")

        if opcion == "1":
            alta_ticket()
        elif opcion == "2":
            leer_ticket(tickets)
        elif opcion == "3":
            while True:
                confirmar = input("\n¿Seguro que desea salir? (s/n): ").lower()
                if confirmar == "s":
                    print("Programa finalizado.")
                    return
                elif confirmar == "n":
                    break   
                else:
                    print("\nRespuesta inválida. Ingrese 's' o 'n'.\n")    
        else:
            print("Opción inválida.")

menu()