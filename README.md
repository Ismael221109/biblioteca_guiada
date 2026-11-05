# Biblioteca Guiada

API REST desarrollada con Flask para buscar libros y consultar información bibliográfica mediante Open Library. Las búsquedas realizadas se registran en una base de datos SQLite.

## Características

- Buscar libros por título.
- Buscar libros por autor.
- Consultar información de un libro por ISBN.
- Consultar el historial de las búsquedas realizadas.
- Comprobar el estado de la API.
- Manejo de errores cuando Open Library no está disponible.

## Tecnologías

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Requests
- python-dotenv
- POSTMAN

## Requisitos

- Python 3.10 o superior
- pip

## Instalación

1. Crear y activar un entorno virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

3. Crear un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=sqlite:///biblioteca.db
OPENLIBRARY_CONTACT=tu-correo@example.com
```

`DATABASE_URL` es opcional. Si no se define, se utiliza una base de datos SQLite llamada `biblioteca.db`.
`OPENLIBRARY_CONTACT` puede contener un correo de contacto para identificar las solicitudes a Open Library.

## Ejecución

```powershell
python app.py
```

La API estará disponible en `http://127.0.0.1:5000`. La base de datos y sus tablas se crean automáticamente al iniciar el servidor.

## Endpoints

### Estado de la API

```http
GET /salud
```

Ejemplo:

```powershell
curl http://127.0.0.1:5000/salud
```

Respuesta:

```json
{
  "estado": "activo"
}
```

### Buscar por título

```http
GET /libros/buscar?titulo=el%20nombre%20del%20viento
```

El título debe tener al menos 2 caracteres. El resultado incluye hasta 10 coincidencias.

### Buscar por autor

```http
GET /libros/autor?nombre=Gabriel%20Garcia%20Marquez
```

El nombre del autor debe tener al menos 2 caracteres. El resultado incluye hasta 10 coincidencias.

### Consultar por ISBN

```http
GET /libros/isbn/<isbn>
```

El ISBN debe tener 10 o 13 dígitos.

Ejemplo:

```powershell
curl http://127.0.0.1:5000/libros/isbn/9780140328721
```

### Consultar historial

```http
GET /historial
```

Devuelve hasta los últimos 50 registros de búsquedas.

Ejemplo:

```powershell
curl http://127.0.0.1:5000/historial
```

## Respuestas de error

- `400 Bad Request`: parámetro ausente o con formato incorrecto.
- `502 Bad Gateway`: Open Library no pudo procesar la solicitud.

Ejemplo:

```json
{
  "error": "titulo debe tener al menos 2 caracteres"
}
```
