# class Auto:
#     def __init__(self, kola):
#         self.kola = kola
#         print(f'ten samochód ma {kola} koła')
#
# class Hello:
#     def _func1(self, x):
#         return print(x)
#     def func2(self, x, y):
#         return print(x+y)
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# hello = Hello(5,8)
# print(hello.x)
# print(hello.y)
# print(hello.func2(7,9))
#
#
# #
# #
# #
# #
# # Volkswagen = Auto
# # Audi = Auto
# # Maluch = Auto
# # Matiz = Auto
# #
# #
# # Volkswagen(3)

class gener2():
    def __init__(self):
        self.x = set(list(__import__('random').randint(0,10) for i in range(100)))


class gener(gener2):
    def func(self, z):
        print(dict(zip(z, __import__('string').ascii_letters)))


obiekt = gener()
obiekt.func(obiekt.x)


'''
Napisz mi proszę kalkulator który jest obiektem :)

Ma też działać tak samo jak kalkulator funkcyjny

(zmienna1, zmienna2)
'''

def func(x,y):
    x = x
    y = y
    yield x+y
    
'''
Spróbuj napisać własną mikrobibliotekę w pythonie wykorzystując obiektówkę. DOWOLNY TEMAT mikroliba

- Kalkulator
- "Generator" list / 
- "Generator" słów / 
- "Generator" znaków / 
- Biblioteka określająca zwierzęta i np. meble i ich funkcjonalności
- Biblioteka szykowania zamówień -> jeszcze bez dziedziczenia :)
'''
