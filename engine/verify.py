import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current))

import logging
import random


class AnswerVerifier:
    verifiers = {}

    @classmethod
    def register(cls, name):
        def decorator(fn):
            if name not in cls.verifiers:
                cls.verifiers[name] = fn
            return fn

        return decorator

    def verify(verifier, correct_answer, submitted_answer):
        return AnswerVerifier.verifiers[verifier](correct_answer, submitted_answer)

    def verify_from_json(question_json, submitted_answer):
        return AnswerVerifier.verify(
            question_json["verifier"],
            question_json["answer"],
            submitted_answer,
        )

    def get_question_json(question_id):
        # TODO: Retrieve question from the database
        pass

    def verify_from_id(question_id, submitted_answer):
        question_json = AnswerVerifier.get_question_json(question_id)
        return AnswerVerifier.verify_from_json(question_json, submitted_answer)
