
def psychological_agent(observation, configuration):
    if observation.step == 0:
        return 0  # Начинаем с камня
    elif observation.step == 1:
        return 1  # Затем бумага
    else:
        return (observation.step - 2) % configuration.signs  # Чередуем
