# Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory.
# В классе Toyota создайте методы wheels и windows.
#
# Метод wheels возвращает строку "Колёса готовы"
#
# Метод windows возвращает строку "Стёкла готовы"
#
# Из класса Toyota вызовите все методы, методы вернут вам строки(объекты)
#
# Результат каждого метода вставьте в лист

from rewenie1 import Factory

class Toyota(Factory):

    def wheels(self):
        print('Wheels')
        return 'Wheels created'

    def windows(self):
        print('Window')
        return 'Windows created'


object2 = Toyota("bridge")
print(object2.windows())
print(object2.wheels())
x = [object2.wheels(), object2.windows()]
print(x)












