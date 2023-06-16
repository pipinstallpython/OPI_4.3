#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Составить программу с использованием иерархии классов. Номер варианта необходимо
получить у преподавателя. В раздел программы, начинающийся после инструкции if __name__
= '__main__': добавить код, демонстрирующий возможности разработанных классов.

Создать класс Pair (пара чисел); определить методы изменения полей и вычисления
произведения чисел. Определить производный класс RightAngled с полями-катетами.
Определить методы вычисления гипотенузы и площади треугольника.
"""

import math


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Возможность изменить значения полей a и b объекта.
    def set_values(self, a, b):
        self.a = a
        self.b = b

    # Произведение
    def multiply(self):
        return self.a * self.b

    # Сложение
    def calculate_numbers(self):
        return self.a + self.b


class RightAngled(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def set_values(self, a, b):
        super().set_values(a, b)

    def calculate_hypotenuse(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def calculate_area(self):
        return 0.5 * self.a * self.b


if __name__ == '__main__':
    pair = Pair(3, 4)
    right_angled = RightAngled(3, 4)

    pair.set_values(5, 6)
    print("Произведение чисел (Pair):", pair.multiply())

    pair.set_values(7, 8)
    print("Сумма чисел (Pair):", pair.calculate_numbers())

    right_angled.set_values(5, 12)
    print("Гипотенуза (RightAngled):", right_angled.calculate_hypotenuse())
    print("Площадь треугольника (RightAngled):", right_angled.calculate_area())
