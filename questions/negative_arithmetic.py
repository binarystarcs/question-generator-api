import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current))

import logging
import random
from constants.topics import *
from constants.displays import *
from constants.answers import *
from constants.verifiers import *
from engine.generate import QuestionGenerator


@QuestionGenerator.register(TOPIC_NEGATIVE_ARITHMETIC, 1)
def generate_level_one_negative_plus_positive():
    negative_value = random.randint(-10, -1)
    positive_value = random.randint(1, 10)
    statement = f"Work out {negative_value} + {positive_value}"
    answer = negative_value + positive_value
    return {
        "statement": statement,
        "answer": str(answer),
        "display": DISPLAY_STANDARD_LATEX,
        "answer_format": ANSWER_FORMAT_INTEGER,
        "verifier": VERIFIER_EXACT,
    }
