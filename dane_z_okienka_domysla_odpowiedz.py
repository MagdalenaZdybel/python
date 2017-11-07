import easygui
color = easygui.enterbox("Jaki jest Twój ulubiony kolor?", default = 'pinkowy')
easygui.msgbox("Wybrałeś: " + color)
print("User choice: " + color)