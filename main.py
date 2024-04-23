from flask import Flask, render_template, request, redirect

app = Flask(__name__)

stored_text = "Hello world!"

@app.route('/', methods=['GET', 'POST'])
def index():
    global stored_text
    if request.method == 'POST':
        # Get the text submitted by the user
        text = request.form['text']
        # Store the text in the variable
        stored_text = text
        # Redirect to the same route to display the stored text
        return redirect('/')
    return render_template('index.html', stored_text=stored_text)

@app.route('/api/latest')
def latest():
    return stored_text