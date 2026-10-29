# Videogames Platform

Aplicación de ejemplo para consultar y añadir videojuegos. El backend usa FastAPI y almacena los datos en memoria; por tanto, los juegos añadidos se pierden al reiniciar el servidor.

## Requisitos

- Python 3.10 o posterior
- pip

## Instalación

Desde la carpeta `videogames-platform`, crea un entorno virtual e instala las dependencias:

```bash
python -m venv .venv
```

En Windows:

```powershell
.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

Después, instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Abre dos terminales desde la carpeta del proyecto.

Inicia la API:

```bash
uvicorn backend.main:app --reload
```

Inicia el servidor del frontend:

```bash
python -m http.server 5500 --directory frontend
```

Abre <http://localhost:5500> en el navegador. La documentación interactiva de la API está disponible en <http://127.0.0.1:8000/docs>.

## API

- `GET /api/games`: lista los videojuegos.
- `POST /api/games`: valida y añade un videojuego.

El cuerpo de `POST /api/games` tiene esta forma:

```json
{
  "title": "Hollow Knight",
  "genre": "Aventura",
  "platform": "PC",
  "release_year": 2017,
  "description": "Explora un vasto reino subterráneo."
}
```

Los géneros aceptados son `Acción`, `Aventura`, `Estrategia`, `Deportes`, `RPG` y `Otro`.
