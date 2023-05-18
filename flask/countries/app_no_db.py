from flask import Flask, request, jsonify
import db
    
app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.route("/countries/<int:id>", methods=['GET'])
def id_countries(id):
    for countrie in countries: 
        if countrie.get('id') == id:
            return jsonify(countrie)
        
@app.route("/countries/<int:id>", methods=['PUT'])
def edit_countries_id(id):
    novo_countrie = request.get_json()
    for indice,countrie in enumerate(countries):
        if countrie.get('id') == id:
            countries[indice].update(novo_countrie)
            return jsonify(countries[indice])
        
@app.route("/countries/<int:id>", methods=['DELETE'])
def delete_countries_id(id):
    for i,countrie in enumerate(countries):
        if countrie.get('id') == id:
            del countries[i]
            return jsonify(countries)

@app.route("/countries", methods=['GET'])
def get_countries():
    return jsonify(countries)

@app.route("/countries",methods=['POST'])
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=8090)