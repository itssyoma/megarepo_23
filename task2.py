#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":

    sentence = input("Введите предложение: ")

    if sentence.isdigit():
        print("Введенное предложение состоит из цифр", file=sys.stderr)
        exit(1)
    
    if "а" in sentence:
        print(f"Буква а найдена в предложении на позиции {sentence.find('а')+1}")
    else:
        print("Буква а в предложении не найдена")
