import boto3
import logging

TABLE_NAME = "questions-data"

client = boto3.client("dynamodb")


def prepare_for_dynamo(item):
    for key, value in item.items():
        if isinstance(value, str):
            item[key] = {"S": value}
        elif isinstance(value, int):
            item[key] = {"N": str(value)}
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
    if not question:
        logging.error("Failed to retrieve question")
    return question
