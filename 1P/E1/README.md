# E1 — Ejecución secuencial

Repositorio público: [ESPE-AD-36880 — E1](https://github.com/SrJCBM/ESPE-AD-36880/tree/main/1P/E1).

## Ejemplo de la vida diaria

Una cafetería prepara un desayuno: primero café (3 segundos), después pan tostado (2 segundos) y finalmente jugo (1 segundo). Cada actividad termina antes de iniciar la siguiente.

El script `ejecucion_secuencial.py` utiliza un ciclo `for` y `time.sleep()` para simular las esperas. Imprime inicio, avances, fin y tiempo transcurrido. No utiliza hilos ni tareas asíncronas.

## Requisitos

Docker Desktop iniciado con contenedores Linux y Docker Compose. La primera construcción necesita Internet para descargar `python:3.13-slim`. No necesitas Python instalado en el equipo.

## Ejecutar con Docker Compose

Abre una terminal dentro de `1P/E1` y ejecuta:

```powershell
docker compose up --build --abort-on-container-exit --exit-code-from demo
```

`--build` construye la imagen con el script actual. La ejecución aparece en la terminal y el programa termina automáticamente. El comando devuelve el código de salida del programa.

Para repetir la ejecución:

```powershell
docker compose up --abort-on-container-exit --exit-code-from demo
```

Para eliminar el contenedor y la red del ejercicio:

```powershell
docker compose down
```

## Ejecutar con Docker directamente

Desde la misma carpeta:

```powershell
docker build -t distribuidas-e1:local .
docker run --rm distribuidas-e1:local
```

## Resultado esperado

La salida incluye líneas de avance entre estos eventos principales:

```text
[ 0.00 s] INICIO: Preparar café
[ 3.00 s] FIN: Preparar café
[ 3.00 s] INICIO: Tostar pan
[ 5.00 s] FIN: Tostar pan
[ 5.00 s] INICIO: Servir jugo
[ 6.00 s] FIN: Servir jugo
Desayuno listo. Tiempo total: 6.00 segundos.
```

Los tiempos son aproximados. La duración total se acerca a la suma `3 + 2 + 1 = 6 segundos` porque ninguna espera se superpone con otra.

## Archivos

- `ejecucion_secuencial.py`: programa en Python.
- `Dockerfile`: construcción de la imagen.
- `docker-compose.yaml`: ejecución de un contenedor.
- `.dockerignore`: limita el contexto de construcción al programa y al Dockerfile.

## Referencia

[Documentación de time.sleep](https://docs.python.org/3.13/library/time.html#time.sleep).
