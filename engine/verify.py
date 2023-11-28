import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current))

import logging
from engine import database


class AnswerVerifier:
    verifiers = {}

    @classmethod
    def register(cls, name):
        def decorator(fn):
            if name not in cls.verifiers:
                cls.verifiers[name] = fn
            return fn

        return decorator

    def verify(verifier, submitted_answer, correct_answer, answer_data=None):
        is_correct = AnswerVerifier.verifiers[verifier](
            submitted_answer, correct_answer, answer_data=answer_data
        )
        return {
            "is_correct": is_correct,
            "correct_answer": correct_answer,
            "submitted_answer": submitted_answer,
        }

    def verify_from_json(question_json, submitted_answer):
        answer_data = None
        if "answer_data" in question_json:
            answer_data = question_json["answer_data"]
        return AnswerVerifier.verify(
            question_json["verifier"],
            submitted_answer,
            question_json["answer"],
            answer_data=answer_data,
        )

    def get_question_json(question_id):
        question = database.retrieve_question(question_id)
        logging.info("Retrieved from database: ", question)
        return question

    def verify_from_id(question_id, submitted_answer):
        question_json = AnswerVerifier.get_question_json(question_id)
        return AnswerVerifier.verify_from_json(question_json, submitted_answer)
