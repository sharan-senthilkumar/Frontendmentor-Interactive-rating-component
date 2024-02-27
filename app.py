from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

global_rating = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_rating', methods=['POST'])
def submit_rating():
    global global_rating
    if request.method == 'POST':
        rating = request.form['rating']
        global_rating = rating
        return 'Rating submitted successfully'


@app.route('/thank')
def thank_you():
    global global_rating
    return render_template('result.html', rating=global_rating)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
