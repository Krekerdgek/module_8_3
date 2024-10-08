# Задача "Некорректность":
# Класс исключений IncorrectVinNumber
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)

# Классы исключений IncorrectCarNumbers
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)

# Класс Car
class Car:
    def __init__(self, model, vin, numbers):

        self.model = model
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):

            self.__vin = vin
            self.__numbers = numbers
            print(f'{self.model} успешно создан')

        else:
            pass

    # Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
    def __is_valid_vin(self, vin_number):
        try:
            if isinstance(vin_number, float):
                raise IncorrectVinNumber('Некорректный тип vin номерa')
            if not 1000000 <= vin_number <= 9999999:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        except IncorrectVinNumber:
            pass
        else:
            return True


# Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
    def __is_valid_numbers(self, numbers):
        try:
            if not isinstance(numbers, str):
                raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            if len(numbers) != 6:
                raise IncorrectCarNumbers('Неверная длина номера')
        except IncorrectCarNumbers:
            pass
        else:
            return True

# Ввод проверяемых параметров

car1 = Car('Mod1', 5565657, 'r222op')
car2 = Car('Mod2', 3333, 'r222op')
car3 = Car('Mod3', 5555555.7, 'r222op')
car4 = Car('Mod4', 1234567, 'r222op5')
car5 = Car('Mod5', 77777777, 'e58lm37')
car6 = Car('Mod6', 85.25, 'q999iu')