from flask import Flask, render_template, redirect, request, url_for
inputTest = Flask(__name__)
 
@inputTest.route('/')
@inputTest.route('/<int:num>')
def inputTest(num=None):
    return render_template('main.html', num=num)
    
@inputTest.route('/calculate',methods=['POST'])
def calculate(num=None):
    if request.method == 'POST':
        temp = request.form['num']
    else:
        temp = None
    return redirect(url_for('inputTest',num=temp))
 
if __name__ == '__main__':
    inputTest.run(host = '0.0.0.0')


