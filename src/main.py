print("DEBUG 1: Arrancando el script...")

from logica import cargar_tareas, guardar_tareas, agregar_tarea, mostrar_tarea, completar_tarea, eliminar_completadas

print("DEBUG 2: Las importaciones de logica funcionaron correctamente.")

def main():
    print("DEBUG 3: Entramos a la función main()")
    tareas = cargar_tareas()
    print(f"DEBUG 4: Tareas cargadas con éxito. Cantidad: {len(tareas)}")
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tareas completadas")
        print("5. Salir")
        
        opcion = input("Elige una opción (1-3): ")
        
        if opcion == "1":
            mostrar_tarea(tareas)
            
        elif opcion == "2":
            texto = input("Escribe lo que tienes que hacer: ")
            agregar_tarea(tareas, texto)
            print("¡Tarea agregada con éxito!")

        elif opcion == "3":
            mostrar_tarea(tareas)
            if tareas:
                try:
                    indice = int(input("Ingresa el número de tarea que completaste: ")) -1
                    completar_tarea(tareas, indice)
                except ValueError:
                    print("Por favor, ingrese un número válido")

        elif opcion == "4":
            eliminar_completadas(tareas)

        elif opcion == "5":
            print("¡Hasta luego! Saliendo del programa...")
            break
            
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 3.")

if __name__ == "__main__":
    main()