# coding=utf-8
#Napisz aplikację, która po wejściu na adres "/konto" wyświetli stan konta użytkownika i listę ostatnich przelewów.
#Początkowy stan konta ustaw np. na 1000 zł.
#Na stronie powinien znajdować się formularz, umożliwiający wykonanie przelewu - powinien zawierać dwa pola tekstowe:
#* nr konta docelowego,
#* kwotę przelewu.
#Po przesłaniu formularza kwota na koncie powinna zostać zmniejszona o podaną wartość, ponadto nowy przelew powinien pojawić się na liście ostatnich przelewów.
#Upewnij się, że odświeżenie strony po wykonaniu przelewu nie spowoduje wykonania tego przelewu jeszcze raz.

from flask import Flask, request, render_template, redirect

app = Flask(__name__)
przelewy = []

@app.route("/konto", methods=['GET','POST'])

def konto():
    stan_kasiory = 1000
    if request.method =='POST':
        przelewy.append({'konto':request.form['konto_dcelowe'],'kwota':request.form['kwota_przelewu']})
        stan_kasiory = stan_kasiory -int(request.form['kwotaPrzelewu']):
        return redirect('/konto')

    return render_template('zadanie1a.html', stan_kasiory = stan_kasiory, przelewy = przelewy)

 app.run(debug=True)