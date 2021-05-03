import random

def dist_id(sensors):
    #creates distinct random id for a sensor

    ids = []
    for sensor in sensors:
        ids.append(sensor['id'])
    rand = random.randint(10000,20000)
    while rand in ids:  
        rand = random.randint(10000,20000)
    return rand

def check_form(form):
    #checks if all the fields in the form are filled

    empty = 0
    form = form.to_dict()
    for field in form:
        if not form[field]:
            empty = 1
            break
    return empty

def find_sensor(sensors, id):
    #finds sensor with a given id; if it doesn't exist, r_sen is empty
    id = int(id)
    r_sen = {}
    r_ind = 0
    for sensor in sensors:
        if id == sensor['id']:
            r_sen = sensor
            r_ind = sensors.index(sensor)
            break
    return r_sen, r_ind