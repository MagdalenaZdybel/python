#Napisz program, który po wejściu na adres /current-status metodą POST ustawi aktualny status na podstawie
# przekazanego w zapytaniu JSON-a (np. {"status": "starting"}),
# a po wejściu na ten sam adres metodą GET zwróci aktualny status.

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


