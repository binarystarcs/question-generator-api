import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current))

import logging
import random
import database


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
        is_correct = AnswerVerifier.verifiers[verifier](
            correct_answer, submitted_answer
        )
        return {
            "is_correct": is_correct,
            "correct_answer": correct_answer,
            "submitted_answer": submitted_answer,
        }

    def verify_from_json(question_json, submitted_answer):
        return AnswerVerifier.verify(
            question_json["verifier"],
            question_json["answer"],
            submitted_answer,
        )

    def get_question_json(question_id):
        question = database.retrieve_question(question_id)
        logging.info(question)
        return question

    def verify_from_id(question_id, submitted_answer):
        question_json = AnswerVerifier.get_question_json(question_id)
        return AnswerVerifier.verify_from_json(question_json, submitted_answer)
