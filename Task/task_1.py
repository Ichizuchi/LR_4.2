class Pair:
    def __init__(self, first, second):
        if not (isinstance(first, int) and isinstance(second, int)):
            raise ValueError("Оба поля должны быть целыми числами.")
        if first <= 0:
            raise ValueError("Поле first должно быть положительным числом.")
        if second <= 0:
            raise ValueError("Поле second должно быть положительным числом.")
        
        self.first = first
        self.second = second

    def read(self):
        try:
            first = int(input("Введите целое положительное число first: "))
            second = int(input("Введите целое положительное число second: "))
            self.__init__(first, second)
        except ValueError as e:
            print(f"Ошибка: {e}")
            exit(1)

    def display(self):
        print(f"first = {self.first}, second = {self.second}")

    def ipart(self):
        if self.second == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю.")
        return self.first // self.second

    # Перегрузка оператора сложения +
    def __add__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first + other.first, self.second + other.second)
        elif isinstance(other, int):
            return Pair(self.first + other, self.second + other)
        else:
            raise TypeError("Операнд должен быть либо объектом Pair, либо целым числом.")

    # Перегрузка оператора вычитания -
    def __sub__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first - other.first, self.second - other.second)
        elif isinstance(other, int):
            return Pair(self.first - other, self.second - other)
        else:
            raise TypeError("Операнд должен быть либо объектом Pair, либо целым числом.")

    # Перегрузка оператора умножения *
    def __mul__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first * other.first, self.second * other.second)
        elif isinstance(other, int):
            return Pair(self.first * other, self.second * other)
        else:
            raise TypeError("Операнд должен быть либо объектом Pair, либо целым числом.")

    # Перегрузка оператора деления /
    def __truediv__(self, other):
        if isinstance(other, Pair):
            if other.first == 0 or other.second == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            return Pair(self.first // other.first, self.second // other.second)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            return Pair(self.first // other, self.second // other)
        else:
            raise TypeError("Операнд должен быть либо объектом Pair, либо целым числом.")

    # Перегрузка оператора равенства ==
    def __eq__(self, other):
        if isinstance(other, Pair):
            return self.first == other.first and self.second == other.second
        return False

    # Перегрузка оператора неравенства !=
    def __ne__(self, other):
        return not self.__eq__(other)


def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(f"Ошибка: {e}")
        exit(1)


if __name__ == '__main__':
    pair1 = make_pair(5, 2)
    pair2 = make_pair(3, 1)
 
    pair1.display()
    print(f"Целая часть дроби: {pair1.ipart()}")

    pair2.display()
    print(f"Целая часть дроби: {pair2.ipart()}")

    print("\nОперации с перегруженными операторами:")
    print(f"pair1 + pair2: {pair1 + pair2}")
    print(f"pair1 - pair2: {pair1 - pair2}")
    print(f"pair1 * pair2: {pair1 * pair2}")
    print(f"pair1 / pair2: {pair1 / pair2}")
    print(f"pair1 == pair2: {pair1 == pair2}")
    print(f"pair1 != pair2: {pair1 != pair2}")

    pair1.read()
    pair1.display()
    print(f"Целая часть дроби: {pair1.ipart()}")
