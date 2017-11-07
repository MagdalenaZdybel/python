import easygui
color = easygui.choicebox("Jaki jest Twój ulubiony kolor?",
                          choices = ['white', 'black','pink'])
easygui.msgbox("Wybrałeś: " + color)
print("User choice: " + color)