from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    title = "FLASK - Single Web Application"
    name = "Christian"
    return render_template('test.html', name=name, title=title)

@app.route('/data')
def data():
    my_data = {
        'name' : "Christian",
        'title' : "FLAKS - Single Web Application",
        'names' : ["one", 'two', 'three']
    }

    return jsonify(my_data)

 