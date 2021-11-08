from flask import Flask, render_template, request, url_for
import sys
app2 = Flask(__name__)



    
@app2.route('/home')
def index():
    return render_template('index.html')


@app2.route('/popup')
def popup():
    return render_template('popup.html')


@app2.route('/result', methods=['POST', 'GET'])
def result_message():
    return render_template('index.html', result = result)

if __name__ == "__main__":
    app2.run(host = '0.0.0.0')
