import random

def biased_random(observation, configuration):
    rand_val = random.random()
    if rand_val < 0.5:
        return 0  # 50% камень
    elif rand_val < 0.8:
        return 1  # 30% бумага
    else:
        return 2  # 20% ножницы
