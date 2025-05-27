# Todo API

## Description
This API allows you to manage a list of tasks. You can create, retrieve, update, and delete tasks.

## Getting Started
To run the application, you will need Python and Flask installed.
1. Save the code as `app.py`.
2. Open your terminal and navigate to the directory where you saved the file.
3. Run the command `python app.py`.
4. The application will be running on `http://127.0.0.1:5000/`.

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
