from urllib.request import urlopen
html = urlopen("http://projekty.motta.com.pl/pythonTest/tekst_do_pythona.txt")
wiadomosc = html.read()
print(wiadomosc)