# Нужно создать класс который принимет модель
# ноутбука(Acer, Asus, ...) и возвращает полную комплектацию ноутбука со всеми характеристиками.
class Acer:
    RAM = None
    Videocard = None
    HardDrive = None
    MotherBoard = None
    ScreenSize = None

    def __init__(self, the_ram= None, the_Videocard= None,
                       the_HardDrive= None,the_MotherBoard= None,
                       the_ScreenSize= None):
        print('Call initiation __init__')
        self.the_ram= the_ram
        self.the_Videocard= the_Videocard
        self.the_HardDrive= the_HardDrive
        self.the_MotherBoard= the_MotherBoard
        self.the_ScreenSize= the_ScreenSize

# В характеристики должны входить:
# CPU
#
# 2 RAM
#
# 3 Video card
#
# 4 Hard Drive
#
# 5 Motherboard
#
# 6 Screen Size
#
# Для каждой характеристики создайте внутри класса
# функцию которая добавляет по одной характеристики к Dictionary.

#
# В итоге Ваш класс должен вернуть Dictionary в котором перечислены:
#
# Модель Ноутбука и его Характеристики.