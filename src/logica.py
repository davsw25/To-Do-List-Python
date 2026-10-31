import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_ARCHIVO = os.path.join(BASE_DIR, "..", "data", "tareas.json")

def cargar_tareas():
    if not os.path.exists(RUTA_ARCHIVO):
        return[]
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return[]

def guardar_tareas(tareas):
    os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(tareas, archivo, indent=4, ensure_ascii=False)

def agregar_tarea(tareas, texto):
    nueva_tarea = {
        "texto": texto,
        "completada": False
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)

def mostrar_tarea(tareas):
    if not tareas:
        print("\nNo hay tareas guardadas todavía")
        return

    print("\n---TUS TAREAS---")
    for indice, tarea in enumerate(tareas, start=1):
        estado = "[✓]" if tarea["completada"] else "[ ]"
        print(f"{indice}. {estado} {tarea['texto']}")

def completar_tarea(tareas, indice):
    if 0 <= indice < len(tareas):
        tareas[indice]["completada"] = True
        guardar_tareas(tareas)
        print("Tarea marcada como completada!")
    else:
        print("Número de tarea invalido")

def eliminar_completadas(tareas):
    tareas_pendientes = [t for t in tareas if not t.get("completada", False)]
    eliminadas = len(tareas) - len(tareas_pendientes)

    if eliminadas > 0:
        tareas.clear()
        tareas.extend(tareas_pendientes)
        guardar_tareas(tareas)
        print(f"Se eliminaron {eliminadas} tarea(s) completada(s)!")
    else:
        print("No hay tareas completadas")