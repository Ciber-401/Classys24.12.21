# 3)Car
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
#
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
#
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
#
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
#
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
#
# то пусть этот метод добавляет эти километры к значению одометра, но не
#
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
#
# пусть метод drive также отнимет потраченное количество бензина с помощью
#
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
#
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
#
# more!”
