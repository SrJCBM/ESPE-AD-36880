# Aplicaciones Distribuidas — Primer parcial

Tres ejemplos en Python sobre ejecución de tareas en una cafetería. Cada ejercicio es independiente y utiliza un solo contenedor Docker.

| Carpeta | Tema | Ejemplo | Duración aproximada |
| --- | --- | --- | --- |
| [E1](1P/E1/README.md) | Ejecución secuencial | Preparar café, tostar pan y servir jugo, en orden | 6 segundos |
| [E2](1P/E2/README.md) | Concurrencia con `asyncio` | Las mismas tareas avanzan durante las esperas de las otras | 3 segundos |
| [E3](1P/E3/README.md) | Hilos y condición de carrera | Dos cajeros registran ventas en una caja compartida | 3 segundos |

## Requisitos

- Docker Desktop iniciado, con contenedores Linux y Docker Compose disponible.
- Conexión a Internet la primera vez para descargar la imagen base `python:3.13-slim`.

No hace falta instalar Python en el equipo. Los programas usan únicamente la biblioteca estándar, muestran su ejecución en la terminal y terminan automáticamente.

## Ejecutar

Desde la raíz del repositorio:

```powershell
docker compose -f 1P/E1/docker-compose.yaml up --build --abort-on-container-exit --exit-code-from demo
docker compose -f 1P/E2/docker-compose.yaml up --build --abort-on-container-exit --exit-code-from demo
docker compose -f 1P/E3/docker-compose.yaml up --build --abort-on-container-exit --exit-code-from demo
```

Ejecuta cada comando por separado para comparar las salidas. También puedes entrar en cada carpeta y usar las instrucciones de su README, que incluyen Docker Compose y los comandos de Docker directo.

## Qué comparar

- **E1:** cada tarea termina antes del inicio de la siguiente; las esperas se suman: `3 + 2 + 1 = 6 s`.
- **E2:** las tres tareas empiezan antes de que termine la primera; las esperas se superponen y el total se aproxima a `max(3, 2, 1) = 3 s`.
- **E3:** sin proteger la actualización se registran `$10` de `$20` esperados; con `Lock` se registran los `$20`.

Los tiempos pueden variar ligeramente según el equipo. Las pausas representan esperas de actividades cotidianas; no son una medición de rendimiento de CPU.
