import logging
import random

level_choice = {
    1: {"levels": [1, 2], "weights": [8, 2]},
    2: {"levels": [1, 2, 3], "weights": [3, 5, 2]},
    3: {"levels": [1, 2, 3, 4], "weights": [1, 2, 5, 2]},
    4: {"levels": [1, 2, 3, 4, 5], "weights": [0, 1, 2, 5, 2]},
    5: {"levels": [1, 2, 3, 4, 5], "weights": [0, 1, 1, 2, 5]},
}


def get_exact_level(level):
    if level not in level_choice:
        logging.error("Invalid level")
    levels = level_choice[level]["levels"]
    weights = level_choice[level]["weights"]
    return random.choices(levels, weights)[0]
