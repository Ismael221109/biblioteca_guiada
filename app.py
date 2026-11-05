import html
from flask import Flask, jsonify, request
from config import Config
from models import db, Busqueda
from openlibrary_service import buscar, consultar_isbn, OpenLibraryError

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.errorhandler(OpenLibraryError)
def error_externo(error):
    return jsonify({"error": str(error)}), 502

@app.get("/salud")
def salud():
    return jsonify({"estado": "activo"}), 200

def registrar(criterio, termino):
    db.session.add(Busqueda(criterio=criterio, termino=termino))
    db.session.commit()



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="127.0.0.1", port=5000, debug=False, use_reloader=False)
