#Домашнее задание по уроку "Пространство имен"

def test_function():
    k = 1
    def inner_function():
       print("Я в области видимости функции test_function")
    inner_function()
    return k
test_function()
#   Вызов inner_function вне функции test_function приводит к ошибке.
#   Имя inner_function локальное для функции test_function,
#   в глобальном пространстве его нет. NameError: name 'inner_function' is not defined.
inner_function()