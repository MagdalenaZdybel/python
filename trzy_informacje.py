name = "Magdalena Zdybel"
birth = "1 January 1978"
myColor = "red"
yes = "yes"
abouts = "yes"
name2 = {}

print("Hi! Have nice day! Do you want to know some about me?")


Iwant = (input("If yes write yes, if don't write no: "))

if Iwant == yes:
    print("My name is: ", name)
    print("I was born: ", birth)
    print("My favorite color is: ", myColor)
else:
    print("Goodbye!")

answers = (input('And now I want to know something about you. Can you answer with three question? If yes write yes: '))
if answers == yes:
    print("great!")
else:
    print("Goodbye!")
    input("What' your name? ")
if name2 == {}:
    print("Hello ", name2)




