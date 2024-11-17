import random

def reaction_to_wins_agent(observation, configuration):

    def is_opponent_winner(observation):
        rewards = observation[0]['reward']
        return rewards[0] < rewards[1]

    if observation.step == 0:
        return random.randrange(0, configuration.signs)  # Случайный выбор на первом ходе
    elif is_opponent_winner(observation):
        return 0
        return random.randrange(0, configuration.signs)  # Случайный выбор
    return 0
    # else:
    #     return (observation.lastOpponentAction + 1) % configuration.signs  # Бьет последний ход противника
