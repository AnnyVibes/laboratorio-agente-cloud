import unittest
from tasks import agregar_tarea, completar_tarea, pendientes

class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertFalse(tarea["completada"])

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_agregar_tarea_con_categoria_valida(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Estudiar", "  Universidad  ")
        self.assertEqual(tarea["categoria"], "Universidad")

    def test_agregar_tarea_sin_categoria_usa_general(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Estudiar")
        self.assertEqual(tarea["categoria"], "general")

    def test_agregar_tarea_con_categoria_vacia(self):
        tareas = []
        for categoria in ("", "   ", None):
            with self.assertRaises(ValueError):
                agregar_tarea(tareas, "Estudiar", categoria)
        self.assertEqual(tareas, [])

    def test_pendientes_filtra_por_categoria_sin_distinguir_mayusculas(self):
        tareas = []
        agregar_tarea(tareas, "Leer", "Estudio")
        agregar_tarea(tareas, "Comprar pan", "Hogar")
        agregar_tarea(tareas, "Resumir", "ESTUDIO")
        agregar_tarea(tareas, "Practicar", "estudio")
        completar_tarea(tareas, 4)
        titulos = [t["titulo"] for t in pendientes(tareas, "eStUdIo")]
        self.assertEqual(titulos, ["Leer", "Resumir"])

    def test_pendientes_sin_categoria_devuelve_todas(self):
        tareas = []
        agregar_tarea(tareas, "Leer", "Estudio")
        agregar_tarea(tareas, "Comprar pan", "Hogar")
        self.assertEqual(len(pendientes(tareas)), 2)

    def test_pendientes_categoria_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Leer", "Estudio")
        self.assertEqual(pendientes(tareas, "Trabajo"), [])

    def test_pendientes_categoria_solo_espacios_devuelve_vacio(self):
        tareas = []
        agregar_tarea(tareas, "Leer", "Estudio")
        agregar_tarea(tareas, "Ordenar")
        self.assertEqual(pendientes(tareas, "   "), [])

if __name__ == "__main__":
    unittest.main()
