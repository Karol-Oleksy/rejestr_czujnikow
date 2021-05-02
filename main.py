import flask, json, random
from flask import request, jsonify, redirect

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False

# Create some test data for our catalog in the form of a list of dictionaries.
sensors = [
    {'id': 0,
     'address': 'Mogilska 43, 31-545 Kraków, Polska',
     'owner': 'Jan Kowalski'},
    {'id': 1,
     'address': 'Dywizjonu 303 16a/6, 44-196 Knurów, Polska',
     'owner': 'Karol Oleksy'},
    {'id': 2,
     'address': 'Lesna 11, 44-100 Gliwice, Polska',
     'owner': 'Błażej Bęben'}
]

def dist_id(sensors):
    ids = []
    for sensor in sensors:
        ids.append(sensor['id'])
    rand = random.randint(10000,20000)
    while rand in ids:  
        rand = random.randint(10000,20000)
    return rand


@app.route('/', methods=['GET'])
def home():
    return '''
    <body>
		<p>
	 	<a href="/sensors/add">Dodaj czujnik</a>
		<br><a href="
	</body>
    '''


@app.route('/sensors/all', methods=['GET'])
def api_all():
    return jsonify(sensors)


@app.route('/sensors', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Błąd: nie podano id czujnika. Spróbuj jeszcze raz."

    # Create an empty list for our results
    

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for sensor in sensors:
        if sensor['id'] == id:
            result = sensor

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(result)

@app.route('/sensors/add',methods = ['POST', 'GET'])
def add_sensor():
   if request.method == 'POST':
      name = request.form['name']
      surname = request.form['surname']
      street = request.form['street']
      number = request.form['number']
      code = request.form['code']
      town = request.form['town']
      country = request.form['country']      
      sensors.append({'id': dist_id(sensors),
                      'address' : '{} {}, {} {}, {}'.format(street,number,code,town,country),
                      'owner' : '{} {}'.format(name, surname)})
      return redirect('/')
   
app.run()