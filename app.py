from flask import Flask, jsonify, request, Response
import csv
from io import StringIO

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
    if not request.is_json or "titulo" not in request.json or "descripcion" not in request.json:
        return jsonify({"error": "Solicitud incorrecta"}), 400
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
    if not request.is_json:
        return jsonify({"error": "Solicitud incorrecta"}), 400
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

# Nuevo endpoint para exportar tareas en formato CSV
@app.route("/tareas/export", methods=["GET"])
def exportar_tareas_csv():
    """Devuelve todas las tareas en formato CSV."""
    buffer = StringIO()
    writer = csv.DictWriter(buffer, fieldnames=["id", "titulo", "descripcion", "hecho"])
    writer.writeheader()
    writer.writerows(tareas)
    csv_data = buffer.getvalue()
    buffer.close()
    response = Response(csv_data, mimetype="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=tareas.csv"
    return response

if __name__ == "__main__":
    app.run(debug=True)
