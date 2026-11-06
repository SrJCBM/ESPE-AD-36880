# E2 — Ejecución con concurrencia

## Ejemplo de la vida diaria

Una cafetería prepara café (3 segundos), tuesta pan (2 segundos) y sirve jugo (1 segundo). Mientras una actividad espera, las otras pueden avanzar; por ejemplo, la cafetera trabaja mientras se prepara el resto del desayuno.

El script `ejecucion_concurrente.py` utiliza `asyncio.gather()` para programar las actividades y esperar a que todas terminen. Cada `await asyncio.sleep(1)` cede el control al bucle de eventos, permitiendo avanzar a las otras tareas.

El programa usa un solo hilo. Es una demostración de concurrencia mediante esperas superpuestas; no de ejecución paralela de cálculos en varios núcleos.

## Requisitos

Docker Desktop iniciado con contenedores Linux. Para la alternativa con Compose, también necesitas Docker Compose. La primera construcción necesita Internet para descargar `python:3.13-slim`. No necesitas instalar Python en el equipo.

## Ejecutar con Docker

Abre una terminal dentro de `1P/E2` y ejecuta:

```powershell
docker build -t distribuidas-e2:local .
docker run --rm distribuidas-e2:local
```

El primer comando construye la imagen. El segundo muestra la ejecución y elimina el contenedor cuando termina. Para repetir el ejemplo, vuelve a ejecutar `docker run`. Si modificas el script, reconstruye la imagen.

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

La salida incluye líneas de avance entre estos eventos principales:

```text
[ 0.00 s] INICIO: Preparar café
[ 0.00 s] INICIO: Tostar pan
[ 0.00 s] INICIO: Servir jugo
[ 1.00 s] FIN: Servir jugo
[ 2.00 s] FIN: Tostar pan
[ 3.00 s] FIN: Preparar café
Desayuno listo. Tiempo total: 3.00 segundos.
```

Los tiempos son aproximados. Las tres actividades empiezan antes de que termine la primera. El total se acerca a `max(3, 2, 1) = 3 segundos`, frente a los 6 segundos de E1, porque sus esperas se superponen.

Las pausas simulan tiempos de actividades, no una prueba de velocidad de procesamiento.

## Archivos

- `ejecucion_concurrente.py`: programa en Python.
- `Dockerfile`: construcción de la imagen.
- `docker-compose.yaml`: ejecución de un contenedor.
- `.dockerignore`: limita el contexto de construcción al programa y al Dockerfile.

## Referencia

[Documentación de tareas y corrutinas de asyncio](https://docs.python.org/3.13/library/asyncio-task.html).
