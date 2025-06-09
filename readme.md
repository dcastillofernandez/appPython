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

## Endpoints de la API

### Obtener todas las tareas
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

### Obtener una tarea específica
- **Endpoint:** `/tareas/<tarea_id>`
- **Method:** `GET`
- **Respuesta (éxito):**
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
- **Respuesta (error - tarea no encontrada):**
  ```json
  {
    "error": "Tarea no encontrada"
  }
  ```

### Agregar una nueva tarea
- **Endpoint:** `/tareas`
- **Method:** `POST`
- **Cuerpo de la solicitud:**
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

### Actualizar una tarea existente
- **Endpoint:** `/tareas/<tarea_id>`
- **Method:** `PUT`
- **Cuerpo de la solicitud (se permiten actualizaciones parciales):**
  ```json
  {
    "titulo": "Título Actualizado",
    "descripcion": "Descripción Actualizada",
    "hecho": true
  }
  ```
- **Respuesta (éxito):**
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
- **Respuesta (error - tarea no encontrada):**
  ```json
  {
    "error": "Tarea no encontrada"
  }
  ```

### Eliminar una tarea
- **Endpoint:** `/tareas/<tarea_id>`
- **Method:** `DELETE`
- **Respuesta (éxito):**
  ```json
  {
    "resultado": "Tarea eliminada"
  }
  ```
- **Respuesta (error - tarea no encontrada):**
  ```json
  {
    "error": "Tarea no encontrada"
  }
  ```

### Exportar tareas a CSV
- **Endpoint:** `/tareas/export`
- **Method:** `GET`
- **Response:** Returns a CSV file (`text/csv`) containing all tasks. Example content:
  ```csv
  id,titulo,descripcion,hecho
  1,Comprar leche,Ir a la tienda y comprar leche,False
  2,Estudiar Python,Completar el tutorial de Python,False
  ```
