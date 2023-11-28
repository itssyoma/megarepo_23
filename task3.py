#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":

    word = input("Введите слово: ")

    if len(word) < 3:
        print("Слово содержит менее трех букв", file=sys.stderr)
        exit(1)
    
    k = int(input("Какую букву, помимо 3-ей, нужно удалить? "))

    if k == 3 or k > len(word) or k == 0:
        print("Неверное значение k", file=sys.stderr)
        exit(1)
    
    word_result = ""
    if k < 3:
        if k == 1:
            word_result += word[1]
        elif k == 2:
            word_result += word[0]
        if len(word) > 3:
            word_result += word[3:]
    else:
        word_result += word[:2]
        if k >= 5:
            word_result += word[3:k-1]
        if k != len(word):
            word_result += word[k:]
    
    print(f"Обновленное слово: {word_result}")
