import boto3
import logging
import time

TABLE_NAME = "questions-data"
PERSISTENCE_SECONDS = 3600

client = boto3.client("dynamodb")
logging.basicConfig(level=logging.INFO)


def prepare_for_dynamo(item):
    for key, value in item.items():
        if isinstance(value, str):
            item[key] = {"S": value}
        elif isinstance(value, int):
            item[key] = {"N": str(value)}
    item["ttl"] = {"N": str(int(time.time() + PERSISTENCE_SECONDS))}
    return item


def prepare_for_python(item):
    for key, value in item.items():
        if isinstance(value, dict) and "S" in value:
            item[key] = value["S"]
        elif isinstance(value, dict) and "N" in value:
            item[key] = int(value["N"])
    return item


def store_question(question):
    try:
        logging.info(f"Storing question {question}")
        question_to_store = prepare_for_dynamo(question)
        logging.info(f"Storing question {question_to_store}")
        client.put_item(TableName=TABLE_NAME, Item=question_to_store)
    except:
        logging.error("Failed to store question")


def retrieve_question(id):
    question = client.get_item(TableName=TABLE_NAME, Key={"id": {"S": id}})
    if not question or not "Item" in question:
        logging.error("Failed to retrieve question")
    question = prepare_for_python(question["Item"])
    logging.info(f"Retrieved question {question}")
    return question
