import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current))

from constants.verifiers import *
from engine.verify import AnswerVerifier


@AnswerVerifier.register(VERIFIER_EXACT)
def verify_exact(user_answer, correct_answer, answer_data=None):
    user_answer = str(user_answer).strip()
    correct_answer = str(correct_answer).strip()
    return user_answer == correct_answer
