# 2)Airplane
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
#
# объекта:
#
# ● make (марка)
#
# ● model
#
# ● year
#
# ● max_speed
#
# ● odometer
#
# ● is_flying
#
# ﻿
#
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
#
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
#
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
#
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
#
# все методы класса.

class Airplanes: #
    """Описание Сомолета и его возможности"""
  #  """каждый раз когда говорят 'создайте класс и передайте в нее характеристики полей... делаем следующее' """

    def __init__(self, mark, model, year, max_speed): # то есть создаем метод и инициализируем в него все поля те в которые мы передавать значение будем потом
        self.mark = mark # то что инициализировали передаем
        self.model = model #
        self.year = year #
        self.max_speed = max_speed #
        self.odometr = 0 #
        self.is_flying = False #


    def take_off(self): # создаем метод взлета где будем передовать только ""
        self.is_flying = True # Таким образом мы меняем значения "False" на "True"
        message_take = f"{self.mark} {self.model} was take off" # Новая переменная которая дает нам сообщение о взлете, марки и модели самолета
        return message_take # тут мы просто возврощаем новую переменную в которой есть message

    def fly(self, km): # создаем метод полета и передаем ему аргумент "" то есть то есть скорость в километрах
        self.odometr += km # на в свойства так же поля "" будем плюсовать километр
        message_fly = f"{self.mark} lew {self.odometr}km during the flying {self.max_speed} km/h" # тут с помошью формата
        return message_fly # будем вызывать сперва марку слово взлёт показатели одометра и максимальную скорость в километрах в час


    def land(self): # метод вычисления приземления
        self.is_flying = False # меняем обратно значения полета на ""
        message_land = f"{self.mark} landed, the odometr shows {self.odometr}km " # о марке самолета и скорость при полете в километрах
        return message_land # возвразаем это сообщение


flanker1 = Airplanes("Flanker1", "Su-35", "2008", 2500) # создаем первую модель "" который
print(flanker1.take_off()) # вызываем взлет ""
print(flanker1.fly(600)) # вызываем полет в котором указан скорость ""
print(flanker1.fly(600)) #
print(flanker1.land()) # и вызов метода приземления






