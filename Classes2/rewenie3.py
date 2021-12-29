# Создайте класс Factory и внутри создайте 2 метода:
#
# Метод engine который возвращает строку "Двигатель создан"
#
# Метод bridge который возвращает строку "Ходовая часть создана"
#
# Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. В классе Toyota создайте методы wheels и windows.
#
# Метод wheels возвращает строку "Колёса готовы"
#
# Метод windows возвращает строку "Стёкла готовы"
#
# Из класса Toyota вызовите все методы, методы вернут вам строки(объекты)
#
# Результат каждого метода вставьте в лист

class Factory:
    def engine(self):
        print('Result "Engine"')
        return 'Engine creatreed'


    def bridge(self):
        print('Result "Bridge"')
        return 'Bridge created'



class Toyota(Factory):

    def wheels(self):
        print('Result "wheels"')
        return 'Wheels created'


    def windows(self):
        print('Result "Windows"')
        return 'Windows created'



fac = Factory()
fac.engine()
fac.bridge()
Toy = Toyota()
Toy.wheels()
Toy.windows()
x = [fac.engine(), fac.bridge(), Toy.windows(), Toy.wheels()]
print(x)




