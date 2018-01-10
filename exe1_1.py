#Napisz funkcję, która zamieni wszystkie cyfry na "#" w tekście (stringu)
#>>> cenzura_cyfr("password12345")
#"password#####"
#>>> cenzura_cyfr("a1a ma k0ta")
#"a#a ma k#ta"


# def cenzura_cyfr(c):
#     print(c)
#
# c = 'password12345'
#
# cenzura_cyfr(c)


#def dodawnie(a, b):
#    print (a+b)

#parA = 1
#parB = 2

#dodawnie(parA, parB)

def cenzura_cyfr(a):
    print(a)

a = str("password12345")

if a <= str('12345'):
    print('#####')
