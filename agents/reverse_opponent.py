
import random
from choices import GameChoice

reversed_choices = {
    GameChoice.ROCK: GameChoice.PAPER,
    GameChoice.PAPER: GameChoice.SCISSORS,
    GameChoice.SCISSORS: GameChoice.ROCK,
}

def reverse_opponent(observation, configuration):
    if observation.step > 0:
        return reversed_choices[observation.lastOpponentAction]
    else:
        return random.randrange(0, configuration.signs)
