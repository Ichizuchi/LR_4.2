class Pair:
    MAX_SIZE = 100  

    def __init__(self, first, second, size=10):
        if not (isinstance(first, int) and isinstance(second, int)):
            raise ValueError("Оба поля должны быть целыми числами.")
        if first <= 0:
            raise ValueError("Поле first должно быть положительным числом.")
        if second <= 0:
            raise ValueError("Поле second должно быть положительным числом.")
        if not (1 <= size <= self.MAX_SIZE):
            raise ValueError(f"size должен быть в пределах от 1 до {self.MAX_SIZE}.")
        
        self.first = first
        self.second = second
        self.size = size
        self.count = 2 
        self.elements = [first, second] 

    def read(self):
        try:
            first = int(input("Введите целое положительное число first: "))
            second = int(input("Введите целое положительное число second: "))
            self.__init__(first, second, self.size)
        except ValueError as e:
            print(f"Ошибка: {e}")
            exit(1)

    def display(self):
        print(f"first = {self.first}, second = {self.second}")
        print(f"Элементы списка: {self.elements}")

    def ipart(self):
        if self.second == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю.")
        return self.first // self.second

 
    def get_size(self):
        return self.size

    def get_count(self):
        return self.count

    def __getitem__(self, index):
        if index >= self.count:
            raise IndexError("Индекс выходит за пределы количества элементов.")
        return self.elements[index]

    # Перегрузка операции индексирования для установки элемента
    def __setitem__(self, index, value):
        if index >= self.size:
            raise IndexError(f"Нельзя установить элемент: максимальный размер {self.size}.")
        if index >= self.count:
            self.count += 1  
        if index < len(self.elements):
            self.elements[index] = value
        else:
            self.elements.append(value)

    # Перегрузка оператора сложения +
    def __add__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first + other.first, self.second + other.second, self.size)
        elif isinstance(other, int):
            return Pair(self.first + other, self.second + other, self.size)
        else:
            raise TypeError("Операнд должен быть либо объектом Pair, либо целым числом.")

    # Перегрузка оператора вычитания -
    def __sub__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first - other.first, self.second - other.second, self.size)
        elif isinstance(other, int):
            return Pair(self.first - other, self.second - other, self.size)
        else:
            raise TypeError("Операнд должен быть либо объектом Pair, либо целым числом.")

    # Перегрузка оператора умножения *
    def __mul__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first * other.first, self.second * other.second, self.size)
        elif isinstance(other, int):
            return Pair(self.first * other, self.second * other, self.size)
        else:
            raise TypeError("Операнд должен быть либо объектом Pair, либо целым числом.")

    # Перегрузка оператора деления /
    def __truediv__(self, other):
        if isinstance(other, Pair):
            if other.first == 0 or other.second == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            return Pair(self.first // other.first, self.second // other.second, self.size)
        elif isinstance(other, int):
            if other == 0:
                raise ZeroDivisionError("Деление на ноль невозможно.")
            return Pair(self.first // other, self.second // other, self.size)
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


def make_pair(first, second, size=10):
    try:
        return Pair(first, second, size)
    except ValueError as e:
        print(f"Ошибка: {e}")
        exit(1)


if __name__ == '__main__':
    pair1 = make_pair(5, 2, size=5)
    pair1.display()
    print(f"Целая часть дроби: {pair1.ipart()}")

    print(f"Размер списка: {pair1.get_size()}")
    print(f"Количество элементов: {pair1.get_count()}")

    print(f"Элемент по индексу 0: {pair1[0]}")
    print(f"Элемент по индексу 1: {pair1[1]}")

    pair1[0] = 10
    pair1[2] = 7 
    pair1.display()
    
    print(f"Обновленное количество элементов: {pair1.get_count()}")
