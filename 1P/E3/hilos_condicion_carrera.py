"""E3: dos cajeros actualizan una caja compartida, sin y con Lock."""

import threading
import time


def ejecutar_cobros(proteger):
    caja = {"saldo": 0}  # Ambos hilos acceden al mismo objeto en memoria.
    bloqueo_caja = threading.Lock()
    bloqueo_consola = threading.Lock()
    barrera_lectura = threading.Barrier(2)
    inicio = time.perf_counter()

    def mostrar(mensaje):
        # Este bloqueo solo evita que se mezclen las líneas de la terminal.
        with bloqueo_consola:
            transcurrido = time.perf_counter() - inicio
            nombre = threading.current_thread().name
            print(f"[{transcurrido:5.2f} s] {nombre}: {mensaje}", flush=True)

    def actualizar_caja():
        # Leer, calcular y escribir son pasos separados de una transacción.
        saldo_leido = caja["saldo"]
        mostrar(f"lee saldo ${saldo_leido}; va a registrar una venta de $10")

        if not proteger:
            # Fuerza un intercalado problemático: ambos leen antes de escribir.
            # Así la pérdida de una actualización se observa en cada ejecución.
            barrera_lectura.wait()

        time.sleep(1)  # Simula el tiempo de registrar el cobro.
        caja["saldo"] = saldo_leido + 10
        mostrar(f"escribe saldo ${saldo_leido + 10}")

    def cobrar():
        if proteger:
            # El bloqueo cubre TODA la operación de leer, calcular y escribir.
            with bloqueo_caja:
                actualizar_caja()
        else:
            actualizar_caja()

    hilos = [threading.Thread(target=cobrar, name=f"Cajero {i}") for i in (1, 2)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()  # Espera a los dos cajeros antes de mostrar el resultado.

    print(f"Saldo esperado: $20 | Saldo registrado: ${caja['saldo']}")
    print(f"Actualizaciones perdidas: ${20 - caja['saldo']}")
    return caja["saldo"]


def main():
    print("=== E3: HILOS Y CONDICIÓN DE CARRERA ===")
    print("Dos cajeros registran una venta de $10 cada uno en la misma caja.")
    print("La caja empieza en $0 en cada escenario.\n")

    print("--- SIN LOCK: condición de carrera ---")
    sin_bloqueo = ejecutar_cobros(proteger=False)
    print("Ambos leyeron $0 y escribieron $10: una venta quedó sin registrar.\n")

    print("--- CON LOCK: actualización protegida ---")
    con_bloqueo = ejecutar_cobros(proteger=True)
    print("Cada cajero completa la actualización antes de que entre el otro.")
    print(f"\nComparación final: sin Lock = ${sin_bloqueo}; con Lock = ${con_bloqueo}.")


if __name__ == "__main__":
    main()
