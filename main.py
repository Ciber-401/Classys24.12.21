from pprint import pprint as pp # Создаем красивый принт
class Car: #  Создание класса всегда с "" и с закглавной буквы

    # дальше идут атрибуты класса то есть поля еше называются а так же переменные
    front = None  # это кузов
    window = None #  тут
    door = 'Закрыты' # тут двери
    motor = None # тут мотор
    the_kolosa = None # тут колёса

    def __init__(self, the_kolodka=None, oil=None): # создаем метод в котором указываем значения ""
        pp('Инициализация вызов __init__') # принтуем 'Инициализация вызов __init__' чтобы понять что у нас происходит
        self.the_kolodka = the_kolodka # "" передаем динамические атрибуты и потом будем их менять
        self.oil = oil # тут тоже самое

    def __str__(self):  # создаем метод с дандермедом __str__ чтобы высветить данные в типе данных стринг
        pp('Строчное отображение данных __str__')  # принтуем теперь что мы видем
        return f"Это объект {self.the_kolodka}"  # и возврощаем атрибут "the_kolodka " чтобы её значения увидеть

    #
    # дальше создаем метод "open_door" and "close_door" или так сказать возможности нашей двери то на что она способна

    def open_door(self, a):  # тут метод который открывает двери
        self.door = 'Открыты'  # передаем massage о открытии дверей
        return f'Двери {self.door} {a} раз'  # в {а} колчичество раз которую
                                             # мы укажем в конце и передадим в {а} какое то значение

    def close_door(self, a):  # тут метод который открывает двери
        self.door = 'Закрыты'  # передаем massage о открытии дверей
        return f'Двери {self.door} {a} раз'  # # в {а} колчичество раз которую
                                             # мы укажем в конце и передадим в {а} какое то значение



lexus = Car('Brembo')  #
# lexus.front="Седан"  #
# lexus.window=6  #
# lexus.motor='2jz'  #
# lexus.door=5  #
# lexus.the_kolosa=4  #
pp(lexus.open_door(5)) # передаем значение в переменную  {} чтобы высветить количество раз сколько она открывается
pp(lexus.close_door(3))  # передаем значение в переменную  {} чтобы высветить количество сколько раз она закрывалась
# pp(lexus.__dict__)  #

