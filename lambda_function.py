import json
import checker
import getter
import logging


def lambda_handler(event, context):
    if event["rawPath"] == "/question":
        logging.info("Handling question request:")
        try:
            body = json.loads(event["body"])
            question = getter.handler(body)
            return json.dumps(question)
        except:
            logging.error("Server error")
            return json.dumps({"error": "Server error"})
    elif event["rawPath"] == "/answer":
        logging.info("Handling answer check request:")
        logging.info(event)
        try:
            body = json.loads(event["body"])
            result = checker.handler(body)
            if result is None:
                return json.dumps({"error": "No question generated"})
            return json.dumps(result)
        except:
            logging.error("Server error")
            return json.dumps({"error": "Server error"})
