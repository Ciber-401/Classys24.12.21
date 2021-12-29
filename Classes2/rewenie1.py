# Создайте класс Factory и внутри создайте 2 метода:

# Метод engine который возвращает строку "Двигатель создан"
#
# Метод bridge который возвращает строку "Ходовая часть создана"
class Factory:
    engine = 0

    def __new__(cls, *args, **kwargs):
        print('__new__ Factory')
        cls.engine = 0
        return super().__new__(cls)


    def __init__(self, bridge):
        print('__init__ Factory')
        self.bridge = bridge

object1 = Factory('engine created')
object1.bridge = 'bridge created'
object1.engine = 'engine created'

print(object1.__dict__)






