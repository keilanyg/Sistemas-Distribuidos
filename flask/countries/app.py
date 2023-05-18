from flask import Flask, request, jsonify
import db
    
app = Flask(__name__)

@app.route("/countries/<int:id>", methods=['GET'])
def id_countries(id):
    countries = db.query_db(f'select * from countries where id = {id}')
    return jsonify(countries),200
        
@app.route("/countries/<int:id>", methods=['PUT'])
def edit_countries_id(id):
    dado = request.get_json()
    countries = db.query_db('UPDATE countries SET country_name="{}", capital="{}" WHERE id = "{}"'.format(dado["country_name"], dado["capital"], id))
    return jsonify(countries)
        
@app.route("/countries/<int:id>", methods=['DELETE'])
def delete_countries_id(id):
    countries = db.query_db(f'DELETE from countries where id = {id}')
    return jsonify(countries),200


@app.route("/countries",methods=['GET'])
def get_countries():
    countries = db.query_db('select * from countries')
    return jsonify(countries),200

@app.route("/countries",methods=['POST'])
def add_country():
    if request.is_json:
        country = request.get_json()
        id = db.insert((country['country_name'],country['capital']))
        return {"id":id}, 201
    return {"error": "Request must be JSON"}, 415


if __name__ == '__main__':
    init_db = False
    
    db.init_app(app)
    
    if init_db:
        with app.app_context():
            db.init_db()
    
    app.run(debug=True,host="0.0.0.0", port=8090)