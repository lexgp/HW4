import random

def pattern_recognizer(observation, configuration):
    if observation.step < 2:
        return random.randrange(0, configuration.signs)  # Случайный выбор на первых двух ходах
    else:
        # Определяем последний ход противника
        last_move = observation.lastOpponentAction
        # Если противник использует какой-то ход, выбираем его слабость
        return (last_move + 1) % configuration.signs  # Бьет последний ход противника
