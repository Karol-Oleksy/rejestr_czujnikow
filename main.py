import flask
from flask import request, jsonify, redirect, render_template
from functions import dist_id, check_form, find_sensor

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_AS_ASCII'] = False

#list for keeping the sensors' data
sensors = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/choose_id')
def choose_id():
    return render_template('choose_id.html')

@app.route('/id', methods=['POST'])
def id_redirect():
    id = request.form['id']
    if request.form['button'] == 'Wyświetl':
        return redirect('/show/{}'.format(id))
    elif request.form['button'] == 'Usuń':
        return redirect('/delete/{}'.format(id))
    elif request.form['button'] == 'Edytuj':
        return redirect('/edit/{}'.format(id))

@app.route('/edit/<id>')
def edit(id):
    sensor = find_sensor(sensors,id)[0]
    if not sensor:
        return 'Brak czujnika o podanym id.'
    else:
        owner = sensor['owner']
        address = sensor['address']
        return render_template('edit.html', id=id, owner=owner, address=address)

@app.route('/delete/<id>')
def delete(id):
    id = int(id)
    sensor, i = find_sensor(sensors,id)
    if not sensor:
        return 'Brak czujnika o podanym id.' 
    else:
        sensors.pop(i)
        return 'Usunięto czujnik o id {}.'.format(id)
       

@app.route('/show/all')
def show_all():
    return jsonify(sensors)

@app.route('/show/<id>')
def show_id(id):
    id = int(id)
    sensor = find_sensor(sensors,id)[0]
    if not sensor:
        return 'Brak czujnika o podanym id.'
    else:
        return jsonify(sensor)

@app.route('/add_result', methods=['POST'])
def add_result():
    if check_form(request.form) == 1:
        return 'Któreś z pól jest puste. Wypełnij wszystkie pola.'
    else:        
        name = request.form['name']
        surname = request.form['surname']
        street = request.form['street']
        number = request.form['number']
        code = request.form['code']
        town = request.form['town']
        country = request.form['country']    
        result = {'id': dist_id(sensors),
                'address' : '{} {}, {} {}, {}'.format(street,number,code,town,country),
                'owner' : '{} {}'.format(name, surname)}
        sensors.append(result)
        return 'Dodano czujnik o id {}.'.format(result['id'])
  
@app.route('/edit_result', methods=['POST'])
def edit_result():
    if check_form(request.form) == 1:
        return 'Któreś z pól jest puste. Wypełnij wszystkie pola.'
    else: 
        i = find_sensor(sensors, request.form['id'])[1]
        owner = request.form['owner']
        address = request.form['address']
        sensors[i]['owner'] = owner
        sensors[i]['address'] = address
        return 'Edytowano czujnik o id {}.'.format(request.form['id'])



   
app.run()