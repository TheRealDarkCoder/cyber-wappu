from flask import Flask, render_template, request, redirect, jsonify

app = Flask(__name__)

stored_text = "Hello world!"
author_name = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global stored_text
    global author_name
    if request.method == 'POST':
        # Get the text submitted by the user
        text = request.form['text']
        name = request.form['name']
        # Store the text in the variable
        stored_text = text
        author_name = name
        # Redirect to the same route to display the stored text
        return redirect('/')
    return render_template('index.html', stored_text=stored_text, author_name=author_name)

@app.route('/api/latest')
def latest():
    data = {'text': stored_text, 'author': author_name}
    return jsonify(data)