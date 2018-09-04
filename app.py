from flask import Flask,render_template,send_from_directory
import os
app = Flask(__name__)

BASE_URL = os.path.abspath(os.path.dirname(__file__))


APP_FOLDER = os.path.join(BASE_URL, "static")

@app.route('/')
def index():

    return render_template('index.html')



@app.route('/get_title')
def get_title():
    print "in function"
    return 'Telsa Azad'


@app.route('/client-app/<path:filename>')
def client_app_folder(filename):
    return send_from_directory(APP_FOLDER, filename)


app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

