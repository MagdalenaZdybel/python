from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello():
    return "Dupa Jasiu pierdzi Stasiu"
app.run(debug=True)

#program Testowy - do sprawdzenia co wprowadził użytkownik
