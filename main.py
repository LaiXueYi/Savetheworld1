from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=["GET", 'POST'])
def index():
    suggestions = None
    if request.method == 'POST':
        suggestions = request.form['suggestions']
        with open('suggestion.txt', 'a') as file:
            file.write(suggestions + '\n')
        return redirect(url_for('thankyou'))
    return render_template('index.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

app.run(host='0.0.0.0', port=81)
