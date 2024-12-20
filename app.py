from flask import Flask, request, make_response
from datetime import datetime
import os
app = Flask(__name__)

@app.route('/display/img/<string:filename>', methods=['GET'])
def display_img(filename):
    request_begin_time = datetime.today()
    print("request_begin_time", request_begin_time)
    if request.method == 'GET':
        image_data = open("app/static/"+filename, "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
    else:
        pass

@app.route('/happynewyear/<string:filename>', methods=['GET'])
def display_new_year(filename):
    request_begin_time = datetime.today()
    print("request_begin_time", request_begin_time)
    if request.method == 'GET':
        image_data = open("app/static/"+filename+".jpg", "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
    else:
        pass

@app.route('/test')
def hello():
    pattern = ""

    pattern = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"*20
    return pattern


@app.route('/', methods=['GET'])
def base_url():
    request_begin_time = datetime.today()
    print("request_begin_time", request_begin_time)
    if request.method == 'GET':
        image_data = open("app/static/happybirthday_v2.jpg", "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
    else:
        pass

@app.route('/iamhappy', methods=['GET'])
def show_note():
    request_begin_time = datetime.today()
    print("request_begin_time", request_begin_time)
    if request.method == 'GET':
        image_data = open("app/static/note.jpg", "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
    else:
        pass

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=1225)
