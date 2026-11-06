"""E2: preparar el desayuno con tareas concurrentes y un solo hilo."""

import asyncio
import time


async def preparar_desayuno():
    actividades = [("Preparar café", 3), ("Tostar pan", 2), ("Servir jugo", 1)]
    inicio = time.perf_counter()

    def mostrar(mensaje):
        transcurrido = time.perf_counter() - inicio
        print(f"[{transcurrido:5.2f} s] {mensaje}", flush=True)

    async def realizar_actividad(nombre, segundos):
        mostrar(f"INICIO: {nombre}")
        for paso in range(1, segundos + 1):
            # Cede el control: otras tareas pueden avanzar durante la espera.
            await asyncio.sleep(1)
            mostrar(f"  {nombre}: avance {paso}/{segundos}")
        mostrar(f"FIN: {nombre}")

    print("=== E2: EJECUCIÓN CONCURRENTE CON ASYNCIO ===")
    print("Las actividades avanzan aprovechando las esperas de las otras.\n")

    # gather programa las actividades concurrentemente y espera a todas.
    await asyncio.gather(
        *(realizar_actividad(nombre, segundos) for nombre, segundos in actividades)
    )

    duracion = time.perf_counter() - inicio
    print(f"\nDesayuno listo. Tiempo total: {duracion:.2f} segundos.")
    print("Las esperas se superponen: aproximadamente 3 segundos en total.")
    print("Concurrencia en un solo hilo; no implica paralelismo de CPU.")


if __name__ == "__main__":
    asyncio.run(preparar_desayuno())
