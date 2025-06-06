# API de Tareas

## Descripción
Esta API permite administrar una lista de tareas. Puedes crear, obtener, actualizar y eliminar tareas.

## Instalación
1. Asegúrate de tener Python 3 instalado.
2. Instala Flask con el comando `pip install Flask`.
3. Guarda el archivo `app.py` en un directorio local.

## Puesta en marcha
1. Abre una terminal y navega hasta la carpeta donde guardaste el archivo.
2. Ejecuta `python app.py`.
3. La aplicación estará disponible en `http://127.0.0.1:5000/`.

## API Endpoints

### Get All Tasks
- **Endpoint:** `/tareas`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "tareas": [
      {
        "id": 1,
        "titulo": "Comprar leche",
        "descripcion": "Ir a la tienda y comprar leche",
        "hecho": false
      },
      {
        "id": 2,
        "titulo": "Estudiar Python",
        "descripcion": "Completar el tutorial de Python",
        "hecho": false
      }
    ]
  }
  ```

### Get a Specific Task
- **Endpoint:** `/tareas/<tarea_id>`
- **Method:** `GET`
- **Response (Success):**
  ```json
  {
    "tarea": {
      "id": 1,
      "titulo": "Comprar leche",
      "descripcion": "Ir a la tienda y comprar leche",
      "hecho": false
    }
  }
  ```
- **Response (Error - Task not found):**
  ```json
  {
    "error": "Tarea no encontrada"
  }
  ```

### Add a New Task
- **Endpoint:** `/tareas`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "titulo": "Nueva Tarea",
    "descripcion": "Descripción de la nueva tarea"
  }
  ```
- **Response:**
  ```json
  {
    "tarea": {
      "id": 3,
      "titulo": "Nueva Tarea",
      "descripcion": "Descripción de la nueva tarea",
      "hecho": false
    }
  }
  ```

### Update an Existing Task
- **Endpoint:** `/tareas/<tarea_id>`
- **Method:** `PUT`
- **Request Body (partial updates allowed):**
  ```json
  {
    "titulo": "Título Actualizado",
    "descripcion": "Descripción Actualizada",
    "hecho": true
  }
  ```
- **Response (Success):**
  ```json
  {
    "tarea": {
      "id": 1,
      "titulo": "Título Actualizado",
      "descripcion": "Descripción Actualizada",
      "hecho": true
    }
  }
  ```
- **Response (Error - Task not found):**
  ```json
  {
    "error": "Tarea no encontrada"
  }
  ```

### Delete a Task
- **Endpoint:** `/tareas/<tarea_id>`
- **Method:** `DELETE`
- **Response (Success):**
  ```json
  {
    "resultado": "Tarea eliminada"
  }
  ```
- **Response (Error - Task not found):**
  ```json
  {
    "error": "Tarea no encontrada"
  }
  ```
