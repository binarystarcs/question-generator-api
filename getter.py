import logging

from engine import generate

from questions import negative_arithmetic

from constants.topics import *

SAMPLE_PROFILE = {
    "name": "Sample Profile",
    "topics": [{"topic": TOPIC_NEGATIVE_ARITHMETIC, "level": 1, "need": 1}],
}


def handler():
    question = generate.QuestionGenerator.get_question_from_profile(SAMPLE_PROFILE)
    return question


if __name__ == "__main__":
    question = handler()
    print(question)
