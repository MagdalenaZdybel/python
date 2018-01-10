from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello/<imie>")

def show_imie(imie):
        return render_template(
            'hello.html',
            naglowek = 'Twoje imie',
            twojeImie = imie,
            link = True
        )

app.run(debug=True)