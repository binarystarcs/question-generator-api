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
def generate_level_one_negative_addition():
    first_value = 1
    second_value = 1
    while first_value >= 0 and second_value >= 0:
        first_value = random.randint(-10, 10)
        second_value = random.randint(-10, 10)
    statement = f"Work out {first_value} + {second_value}"
    answer = first_value + second_value
    return {
        "statement": statement,
        "answer": str(answer),
        "display": DISPLAY_STANDARD_LATEX,
        "answer_format": ANSWER_FORMAT_INTEGER,
        "verifier": VERIFIER_EXACT,
    }


@QuestionGenerator.register(TOPIC_NEGATIVE_ARITHMETIC, 1)
def generate_level_one_negative_subtraction():
    first_value = 1
    second_value = 1
    while first_value >= 0 and second_value >= 0:
        first_value = random.randint(-10, 10)
        second_value = random.randint(-10, 10)
    statement = f"Work out {first_value} - {second_value}"
    answer = first_value - second_value
    return {
        "statement": statement,
        "answer": str(answer),
        "display": DISPLAY_STANDARD_LATEX,
        "answer_format": ANSWER_FORMAT_INTEGER,
        "verifier": VERIFIER_EXACT,
    }


@QuestionGenerator.register(TOPIC_NEGATIVE_ARITHMETIC, 1)
def generate_level_one_negative_multiplication():
    first_value = 1
    second_value = 1
    while first_value >= 0 and second_value >= 0:
        first_value = random.randint(-10, 10)
        second_value = random.randint(-10, 10)
    statement = f"Work out {first_value} \\times {second_value}"
    answer = first_value * second_value
    return {
        "statement": statement,
        "answer": str(answer),
        "display": DISPLAY_STANDARD_LATEX,
        "answer_format": ANSWER_FORMAT_INTEGER,
        "verifier": VERIFIER_EXACT,
    }


@QuestionGenerator.register(TOPIC_NEGATIVE_ARITHMETIC, 1)
def generate_level_one_negative_division():
    first_value = 1
    second_value = 1
    while (first_value >= 0 and second_value >= 0) or first_value * second_value == 0:
        first_value = random.randint(-6, 6)
        second_value = random.randint(-6, 6)
    product = first_value * second_value
    statement = f"Work out {product} \\div {second_value}"
    answer = first_value
    return {
        "statement": statement,
        "answer": str(answer),
        "display": DISPLAY_STANDARD_LATEX,
        "answer_format": ANSWER_FORMAT_INTEGER,
        "verifier": VERIFIER_EXACT,
    }
