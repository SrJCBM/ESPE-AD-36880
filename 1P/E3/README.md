# E3 — Hilos y condiciones de carrera

## Ejemplo de la vida diaria

Dos cajeros de una cafetería registran una venta de $10 cada uno. Comparten una caja cuyo saldo inicial es $0. Al finalizar ambos cobros, el saldo correcto es $20.

El script `hilos_condicion_carrera.py` ejecuta dos escenarios, reiniciando la caja en cada uno:

1. **Sin `Lock`:** ambos cajeros leen $0 antes de escribir. Cada uno calcula `0 + 10` y escribe $10. La segunda escritura reemplaza el resultado de la primera: solo quedan $10 registrados.
2. **Con `Lock`:** un cajero termina la operación completa antes de que entre el otro. El primero actualiza el saldo a $10 y el segundo lee ese saldo y lo actualiza a $20.

## Cómo se demuestra la carrera

Se crean dos `threading.Thread`, que acceden al mismo diccionario `caja`. La actualización se divide en lectura, cálculo y escritura; esta operación compuesta necesita protección.

En el escenario sin protección, `threading.Barrier(2)` hace que ambos hilos terminen de leer antes de permitirles escribir. Esto fuerza de manera didáctica un intercalado que pierde una actualización. La barrera **no protege la transacción**. Sin ella, el problema podría aparecer o no en una ejecución, según la planificación de los hilos.

En el escenario corregido, `threading.Lock()` protege toda la operación de lectura, cálculo y escritura. No se utiliza la barrera dentro del bloqueo porque el primer hilo impediría que el segundo llegara a ella. `join()` espera la finalización de ambos hilos antes de consultar el saldo.

Hay un bloqueo adicional para imprimir líneas completas en consola; este solo ordena los mensajes y no protege el saldo. El GIL de CPython no convierte toda esta transacción en una operación atómica.

## Requisitos

Docker Desktop iniciado con contenedores Linux. Para la alternativa con Compose, también necesitas Docker Compose. La primera construcción necesita Internet para descargar `python:3.13-slim`. No necesitas instalar Python en el equipo.

## Ejecutar con Docker

Abre una terminal dentro de `1P/E3` y ejecuta:

```powershell
docker build -t distribuidas-e3:local .
docker run --rm distribuidas-e3:local
```

El programa muestra ambos escenarios y termina automáticamente. `--rm` elimina el contenedor al finalizar. Para repetirlo, vuelve a ejecutar `docker run`. Si modificas el script, reconstruye la imagen.

## Ejecutar con Docker Compose

Desde la misma carpeta:

```powershell
docker compose up --build --abort-on-container-exit --exit-code-from demo
```

Para repetir la ejecución sin reconstruir:

```powershell
docker compose up --abort-on-container-exit --exit-code-from demo
```

Para eliminar el contenedor y la red del ejercicio:

```powershell
docker compose down
```

## Resultado esperado

Entre los mensajes de los cajeros se muestran estos resultados:

```text
--- SIN LOCK: condición de carrera ---
Saldo esperado: $20 | Saldo registrado: $10
Actualizaciones perdidas: $10

--- CON LOCK: actualización protegida ---
Saldo esperado: $20 | Saldo registrado: $20
Actualizaciones perdidas: $0

Comparación final: sin Lock = $10; con Lock = $20.
```

El orden de los mensajes de los cajeros puede variar. Los saldos finales se mantienen porque el primer escenario fuerza el intercalado problemático y el segundo protege la actualización. La demostración tarda aproximadamente 3 segundos: una espera compartida de 1 segundo y dos esperas protegidas de 1 segundo cada una.

## Archivos

- `hilos_condicion_carrera.py`: programa en Python.
- `Dockerfile`: construcción de la imagen.
- `docker-compose.yaml`: ejecución de un contenedor.
- `.dockerignore`: limita el contexto de construcción al programa y al Dockerfile.

## Referencia

[Documentación de threading, Lock y Barrier](https://docs.python.org/3.13/library/threading.html).
