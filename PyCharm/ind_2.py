#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В следующих заданиях требуется реализовать абстрактный базовый класс, определив в нем
абстрактные методы и свойства. Эти методы определяются в производных классах. В базовых
классах должны быть объявлены абстрактные методы ввода/вывода, которые реализуются в
производных классах.
Вызывающая программа должна продемонстрировать все варианты вызова переопределенных
абстрактных методов. Написать функцию вывода, получающую параметры базового класса по
ссылке и демонстрирующую виртуальный вызов.

Создать абстрактный базовый класс Pair с виртуальными арифметическими операциями.
Реализовать производные классы Complex (комплексное число) и Rational (рациональное
число).
"""

from abc import ABC, abstractmethod


class Pair(ABC):
    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def output(self):
        pass


class Complex(Pair):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.imaginary + other.imaginary)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.imaginary - other.imaginary)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Complex):
            real_part = self.real * other.real - self.imaginary * other.imaginary
            imaginary_part = self.real * other.imaginary + self.imaginary * other.real
            return Complex(real_part, imaginary_part)
        else:
            raise TypeError("Unsupported operand type for *")

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def input(self):
        real = float(input("Enter the real part: "))
        imaginary = float(input("Enter the imaginary part: "))
        self.real = real
        self.imaginary = imaginary

    def output(self):
        print(self)


class Rational(Pair):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(other, Rational):
            common_denominator = self.denominator * other.denominator
            numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            return Rational(numerator, common_denominator)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Rational):
            common_denominator = self.denominator * other.denominator
            numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            return Rational(numerator, common_denominator)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator)
        else:
            raise TypeError("Unsupported operand type for *")

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def input(self):
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        self.numerator = numerator
        self.denominator = denominator

    def output(self):
        print(self)


def demonstrate_virtual_call(pair):
    pair.output()


if __name__ == '__main__':
    # Создание объектов класса Complex и Rational
    complex1 = Complex(2, 3)
    complex2 = Complex(4, 5)
    rational1 = Rational(1, 2)
    rational2 = Rational(3, 4)

    # Продемонстрировать виртуальный вызов метода output
    demonstrate_virtual_call(complex1)
    demonstrate_virtual_call(rational1)

    # Примеры использования арифметических операций
    result_complex = complex1 + complex2
    print("Complex addition:", result_complex)

    result_rational = rational1 - rational2
    print("Rational subtraction:", result_rational)