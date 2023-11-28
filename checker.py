import logging

from engine import verify

from verifiers import exact

from constants.topics import *

SAMPLE_EVENT = {"id": "1ed88fb7-5c23-443b-b9b9-517ef9dbb1d3", "answer": "3"}


def validate_event(event):
    if "id" not in event:
        logging.error("Missing id")
        return False
    if "answer" not in event:
        logging.error("Missing answer")
        return False
    return True


def handler(event):
    if not validate_event(event):
        logging.error("Invalid event")
        return None
    result = verify.AnswerVerifier.verify_from_id(event["id"], event["answer"])
    return result


if __name__ == "__main__":
    result = handler(SAMPLE_EVENT)
    print(result)
