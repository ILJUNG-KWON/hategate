from flask import Flask, render_template, request, url_for
import sys
app2 = Flask(__name__)



    
@app2.route('/home')
def index():
    return render_template('popup.html')



@app2.route('/result', methods=['POST', 'GET'])
def result_message():
    text = request.form['user_mes']
    return render_template('popup.html', result1 = result1, result2=result2, cnt=cnt)

if __name__ == "__main__":
    app2.run(host = '0.0.0.0')
