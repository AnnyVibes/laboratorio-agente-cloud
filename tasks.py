CATEGORIA_POR_DEFECTO = "general"


def _siguiente_id(tareas):
    return max((t["id"] for t in tareas), default=0) + 1


def agregar_tarea(tareas, titulo, categoria=CATEGORIA_POR_DEFECTO):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El título es obligatorio")
    categoria = (categoria or "").strip()
    if not categoria:
        raise ValueError("La categoría es obligatoria")
    tarea = {
        "id": _siguiente_id(tareas),
        "titulo": titulo,
        "categoria": categoria,
        "completada": False,
    }
    tareas.append(tarea)
    return tarea

def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")

def eliminar_tarea(tareas, tarea_id):
    for indice, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            return tareas.pop(indice)
    raise ValueError("Tarea no encontrada")

def pendientes(tareas, categoria=None):
    resultado = [t for t in tareas if not t["completada"]]
    if categoria is None:
        return resultado
    buscada = categoria.strip().casefold()
    return [
        t for t in resultado
        if t.get("categoria", CATEGORIA_POR_DEFECTO).casefold() == buscada
    ]
