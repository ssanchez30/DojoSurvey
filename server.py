from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "secret"


@app.route('/', methods=['GET'])
def principal():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def registration():
    name = request.form['fName']
    location = request.form['location']
    language = request.form['fLanguage']
    comment = request.form['comments']
    genero = request.form['genero']
    hobbies = request.form.getlist('hobbies')
    cant = len(hobbies)

    context = {
        "name": name,
        "location": location,
        "language": language,
        "comment": comment,
        "genero": genero,
        "hobbies": hobbies,
        "cant": cant
    }

    session['datos'] = context

    return redirect('/detalle')


@app.route('/detalle', methods=['GET'])
def detalle():
    return render_template('detalle.html')


if __name__ == "__main__":
    app.run(debug=True)
