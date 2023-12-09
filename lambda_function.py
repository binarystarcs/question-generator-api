import json
import checker
import getter
import logging


def form_response(data):
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept",
            "Access-Control-Allow-Methods": "OPTIONS, POST",
        },
        "body": json.dumps(data),
    }
    return response


def lambda_handler(event, context):
    if event["rawPath"] == "/question":
        logging.info("Handling question request:")
        try:
            body = json.loads(event["body"])
            question = getter.handler(body)
            return form_response(question)
        except:
            logging.error("Server error")
            return form_response({"error": "Server error"})
    elif event["rawPath"] == "/answer":
        logging.info("Handling answer check request:")
        logging.info(event)
        try:
            body = json.loads(event["body"])
            result = checker.handler(body)
            if result is None:
                return form_response({"error": "No question generated"})
            return form_response(result)
        except:
            logging.error("Server error")
            return form_response({"error": "Server error"})
