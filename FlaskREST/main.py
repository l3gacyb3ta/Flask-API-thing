from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
from flask_cors import CORS, cross_origin

app = Flask(__name__)
db = TinyDB('database.json')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'


@app.route('/names', methods=['GET','POST']) 
@cross_origin()
def hello_world():
  if request.method == 'POST':
    data = "BROKEN"
    print(request.form)
    for i in request.form.keys():
      data = i
    db.insert({'name':data})
    return "Success"
  else:
    return jsonify(db.all())


if __name__ == '__main__':
    app.run(host='localhost',port=5000,debug=True)