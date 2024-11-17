
import numpy as np

opponentHistory = []

def psychological_agent(observation, configuration):
    global opponentHistory
    if observation.step > 0:
        opponentHistory.append(observation.lastOpponentAction)
        while len(opponentHistory) > 10:
            opponentHistory.pop(0)
    if len(opponentHistory) < 10:
        return np.random.randint(0, configuration.signs)
    
    last_moves = np.array(opponentHistory)
    move_counts = np.bincount(last_moves, minlength=configuration.signs)
    most_frequent_move = np.argmax(move_counts)
    if not isinstance(most_frequent_move, int):
        most_frequent_move = 0
    return (most_frequent_move + 1) % 3
