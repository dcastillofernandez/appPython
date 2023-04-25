from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo
tareas = [
    {
        "id": 1,
        "titulo": "Comprar leche",
        "descripcion": "Ir a la tienda y comprar leche",
        "hecho": False,
    },
    {
        "id": 2,
        "titulo": "Estudiar Python",
        "descripcion": "Completar el tutorial de Python",
        "hecho": False,
    },
]

@app.route("/tareas", methods=["GET"])
def obtener_tareas():
    return jsonify({"tareas": tareas})

@app.route("/tareas/<int:tarea_id>", methods=["GET"])
def obtener_tarea(tarea_id):
    tarea = [t for t in tareas if t["id"] == tarea_id]
    if len(tarea) == 0:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify({"tarea": tarea[0]})

@app.route("/tareas", methods=["POST"])
def agregar_tarea():
    tarea = {
        "id": tareas[-1]["id"] + 1 if len(tareas) > 0 else 1,
        "titulo": request.json["titulo"],
        "descripcion": request.json["descripcion"],
        "hecho": False,
    }
    tareas.append(tarea)
    return jsonify({"tarea": tarea}), 201

@app.route("/tareas/<int:tarea_id>", methods=["PUT"])
def actualizar_tarea(tarea_id):
    tarea = [t for t in tareas if t["id"] == tarea_id]
    if len(tarea) == 0:
        return jsonify({"error": "Tarea no encontrada"}), 404
    tarea[0]["titulo"] = request.json.get("titulo", tarea[0]["titulo"])
    tarea[0]["descripcion"] = request.json.get("descripcion", tarea[0]["descripcion"])
    tarea[0]["hecho"] = request.json.get("hecho", tarea[0]["hecho"])
    return jsonify({"tarea": tarea[0]})

@app.route("/tareas/<int:tarea_id>", methods=["DELETE"])
def eliminar_tarea(tarea_id):
    tarea = [t for t in tareas if t["id"] == tarea_id]
    if len(tarea) == 0:
        return jsonify({"error": "Tarea no encontrada"}), 404
    tareas.remove(tarea[0])
    return jsonify({"resultado": "Tarea eliminada"})

if __name__ == "__main__":
    app.run(debug=True)
