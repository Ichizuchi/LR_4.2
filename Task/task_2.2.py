class Hex:
    MAX_SIZE = 100 

    def __init__(self, hex_string='0'):
        # Инициализируем список из MAX_SIZE элементов, каждый из которых равен 0
        self.hex_digits = [0] * self.MAX_SIZE
        hex_string = hex_string.lstrip('0x').upper()  
        real_size = min(len(hex_string), self.MAX_SIZE)

        for i in range(real_size):
            digit = hex_string[-(i + 1)]  
            self.hex_digits[i] = int(digit, 16) 

        self.size = real_size 

    def display(self):
        # Выводим число в виде строки (начиная с самого старшего разряда)
        hex_str = ''.join(hex(digit)[2:].upper() for digit in reversed(self.hex_digits[:self.size]))
        print(f"0x{hex_str}")

    # Перегрузка оператора сложения +
    def __add__(self, other):
        if not isinstance(other, Hex):
            raise TypeError("Операнд должен быть объектом класса Hex.")
        
        result = Hex()  # Создаем новый объект для результата
        carry = 0

        # Складываем побитно числа
        for i in range(self.MAX_SIZE):
            total = self.hex_digits[i] + other.hex_digits[i] + carry
            result.hex_digits[i] = total % 16  # Остаток от деления на 16
            carry = total // 16  # Перенос в старший разряд

        result.size = max(self.size, other.size) + (1 if carry else 0)
        return result

    def __sub__(self, other):
        if not isinstance(other, Hex):
            raise TypeError("Операнд должен быть объектом класса Hex.")
        
        result = Hex()
        borrow = 0

        for i in range(self.MAX_SIZE):
            total = self.hex_digits[i] - other.hex_digits[i] - borrow
            if total < 0:
                total += 16
                borrow = 1
            else:
                borrow = 0
            result.hex_digits[i] = total

        result.size = max(self.size, other.size)
        return result

    # Перегрузка оператора умножения *
    def __mul__(self, other):
        if not isinstance(other, Hex):
            raise TypeError("Операнд должен быть объектом класса Hex.")
        
        result = Hex()

        for i in range(self.size):
            carry = 0
            for j in range(other.size):
                total = result.hex_digits[i + j] + self.hex_digits[i] * other.hex_digits[j] + carry
                result.hex_digits[i + j] = total % 16
                carry = total // 16

        result.size = self.size + other.size
        return result

    # Перегрузка оператора деления /
    def __truediv__(self, other):
        if not isinstance(other, Hex):
            raise TypeError("Операнд должен быть объектом класса Hex.")
        
        result = Hex()
        dividend = int(self.__str__(), 16)
        divisor = int(other.__str__(), 16)

        quotient = dividend // divisor
        result = Hex(hex(quotient))

        return result

    def __eq__(self, other):
        if not isinstance(other, Hex):
            return False
        return self.hex_digits == other.hex_digits

    def __lt__(self, other):
        for i in reversed(range(self.MAX_SIZE)):
            if self.hex_digits[i] < other.hex_digits[i]:
                return True
            elif self.hex_digits[i] > other.hex_digits[i]:
                return False
        return False

    def __gt__(self, other):
        return other < self

    def __str__(self):
        hex_str = ''.join(hex(digit)[2:].upper() for digit in reversed(self.hex_digits[:self.size]))
        return f"0x{hex_str}"


if __name__ == '__main__':
    hex1 = Hex("1A3")
    hex2 = Hex("B2")

    print("Hex1:")
    hex1.display()

    print("Hex2:")
    hex2.display()

    print("Сумма Hex1 и Hex2:")
    sum_hex = hex1 + hex2
    sum_hex.display()

    print("Разность Hex1 и Hex2:")
    diff_hex = hex1 - hex2
    diff_hex.display()

    print("Произведение Hex1 и Hex2:")
    prod_hex = hex1 * hex2
    prod_hex.display()

    print("Деление Hex1 на Hex2:")
    div_hex = hex1 / hex2
    div_hex.display()
