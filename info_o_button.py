import easygui
color = easygui.buttonbox("Jaki jest Twój ulubiony kolor?",
                          choices = ['white', 'black','pink'])
easygui.msgbox("Wybrałeś: " + color)
print("User choice: " + color)