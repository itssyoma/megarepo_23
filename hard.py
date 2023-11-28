#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":

    sentence = input("Введите предложение: ")

    max_spaces = 0
    current_spaces = 0

    for char in sentence:
        if char == " ":
            current_spaces += 1
        else:
            max_spaces = max(max_spaces, current_spaces)
            current_spaces = 0
    
    print(f"Наибольшее количество идущих подряд пробелов: {max_spaces}")