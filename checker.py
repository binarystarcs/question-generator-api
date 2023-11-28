import logging

from engine import verify

from verifiers import exact

from constants.topics import *

SAMPLE_EVENT = {"id": "1", "answer": "-2"}


def validate_event(event):
    if "id" not in event:
        logging.error("Missing id")
        return False
    if "answer" not in event:
        logging.error("Missing answer")
        return False


def handler(event):
    if not validate_event(event):
        logging.error("Invalid event")
        return False
    result = verify.AnswerVerifier.verify_from_id(event["id"], event["answer"])


if __name__ == "__main__":
    result = handler(SAMPLE_EVENT)
    print(result)
