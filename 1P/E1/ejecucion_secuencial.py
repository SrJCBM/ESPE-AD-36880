"""E1: preparar un desayuno ejecutando una actividad a la vez."""

import time


def preparar_desayuno():
    actividades = [("Preparar café", 3), ("Tostar pan", 2), ("Servir jugo", 1)]
    inicio = time.perf_counter()

    def mostrar(mensaje):
        transcurrido = time.perf_counter() - inicio
        print(f"[{transcurrido:5.2f} s] {mensaje}", flush=True)

    print("=== E1: EJECUCIÓN SECUENCIAL ===")
    print("Una actividad debe terminar antes de comenzar la siguiente.\n")

    # El for no avanza a la siguiente actividad hasta acabar la actual.
    for nombre, segundos in actividades:
        mostrar(f"INICIO: {nombre}")
        for paso in range(1, segundos + 1):
            time.sleep(1)  # Simula el tiempo que requiere la actividad.
            mostrar(f"  {nombre}: avance {paso}/{segundos}")
        mostrar(f"FIN: {nombre}")

    duracion = time.perf_counter() - inicio
    print(f"\nDesayuno listo. Tiempo total: {duracion:.2f} segundos.")
    print("Las esperas se suman: 3 + 2 + 1 = aproximadamente 6 segundos.")


if __name__ == "__main__":
    preparar_desayuno()
