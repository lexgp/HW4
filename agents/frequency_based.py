import numpy as np

opponentHistory = []

def frequency_based_agent(observation, configuration):
    global opponentHistory
    if len(opponentHistory) == 0:
        # Случайный выбор на первом ходе
        return np.random.randint(0, configuration.signs)
    else:
        opponentHistory.append(observation.lastOpponentAction)
        move_count = np.zeros(configuration.signs, dtype=int)
        for i in range(observation.step):
            move_count[opponentHistory[i]] += 1  # Подсчет ходов противника
        most_frequent_move = np.argmax(move_count)  # Находим наиболее частый ход
        return (most_frequent_move + 1) % configuration.signs  # Бьет наиболее частый ход
