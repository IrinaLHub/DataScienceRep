
"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Функция угадывания числа методом деления отрезка пополам
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    # Используем метод деления отрезка пополам
    count = 0
    min_range = 1     # нижняя граница поиска числа
    max_range = 100   # верхняя граница поиска числа
    predict = 50      # предсказанное число

    while number != predict:
        count += 1        
        if number > predict:
            min_range = predict  
        elif number < predict:
            max_range = predict
        predict = min_range + ((max_range-min_range+1) // 2)

    # Ваш код заканчивается здесь    
    return count


def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []    
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10))  # загадали список чисел    

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))      
    return score

print(score_game(game_core_v3))