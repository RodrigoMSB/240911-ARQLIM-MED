from controladores.controlador_tarea import ControladorTarea

def mostrar_menu():
    print("\nGestión de Tareas")
    print("1. Crear Tarea")
    print("2. Listar Tareas")
    print("3. Completar Tarea")
    print("4. Salir")
    return input("Selecciona una opción: ")

def main():
    controlador = ControladorTarea()

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            tarea = controlador.crear_tarea(titulo, descripcion)
            print(f"Tarea creada: {tarea}")
        
        elif opcion == "2":
            tareas = controlador.listar_tareas()
            if tareas:
                for tarea in tareas:
                    print(tarea)
            else:
                print("No hay tareas registradas.")
        
        elif opcion == "3":
            id_tarea = input("ID de la tarea a completar: ")
            if id_tarea.isdigit():
                tarea = controlador.completar_tarea(int(id_tarea))
                if tarea:
                    print(f"Tarea completada: {tarea}")
                else:
                    print("Tarea no encontrada.")
            else:
                print("Por favor, ingresa un número válido para el ID de la tarea.")
        
        elif opcion == "4":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()