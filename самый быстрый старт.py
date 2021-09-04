import numpy as np


def score_game(game_score):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = round(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core(number):
    count = 1
    minimum = 1
    maximum = 101

    predict = (maximum + minimum) // 2

    while number != predict:
        count += 1
        if number > predict:
            minimum = predict
        else:
            maximum = predict

        predict = (maximum + minimum) // 2

    return (count)


score_game(game_core)

