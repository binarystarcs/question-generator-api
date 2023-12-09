import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current))

import logging
import random
from uuid import uuid4
from engine import database
from constants.levels import get_exact_level


class TopicLevelQuestionGenerator:
    def __init__(self, topic, level):
        self.topic = topic
        self.level = level
        self.generators = []

    def select_generator(self):
        generators = [x["generator"] for x in self.generators]
        weights = [x["weight"] for x in self.generators]
        generator = random.choices(generators, weights)[0]
        return generator

    def get_question(self):
        generator = self.select_generator()
        question = generator()
        if question is None:
            logging.error(
                f"Failed to generate question topic {self.topic} level {self.level}."
            )
            return None
        question["level"] = self.level
        question["topic"] = self.topic
        return question


class TopicQuestionGenerator:
    def __init__(self, name):
        self.name = name
        self.generators = {}

    def register(self, fn, level, weight=1.0):
        if level not in self.generators:
            self.generators[level] = TopicLevelQuestionGenerator(self.name, level)
        self.generators[level].generators.append({"generator": fn, "weight": weight})

    def get_question(self, level, exact_level=False):
        if exact_level:
            question_level = level
            question = self.generators[level].get_question()
        else:
            question_level = get_exact_level(level)
            question = self.generators[question_level].get_question()
        if question is None:
            logging.error(
                f"No question generated for topic {self.name}, level {question_level}."
            )
            return None
        question["topic"] = self.name
        return question


class QuestionGenerator:
    generators = {}

    @classmethod
    def register(cls, topic, level, weight=1.0):
        def decorator(fn):
            if topic not in cls.generators:
                cls.generators[topic] = TopicQuestionGenerator(name=topic)
            cls.generators[topic].register(fn, level, weight=weight)
            return fn

        return decorator

    def get_question(topic, level, exact_level=False):
        topic_generator = QuestionGenerator.generators[topic]
        question = topic_generator.get_question(level, exact_level=exact_level)
        question["id"] = str(uuid4())
        print("Connecting to DB...")
        database.store_question(question)
        question = database.prepare_for_python(question)
        return question

    def verify_profile_topic(topic_entry):
        """Topic entry is {topic: str, level: int, need: float}
        Returns True if able to generate a question."""
        if (
            not "topic" in topic_entry
            or not "level" in topic_entry
            or not "need" in topic_entry
        ):
            return False
        print("hi")
        return topic_entry["topic"] in QuestionGenerator.generators

    def get_question_from_profile(profile):
        # profile is a dictionary with entry topics: [{topic:, level:, need:}]
        if "topics" not in profile:
            logging.error("Topics section absent from profile\n", profile)
            return None
        filtered_topics = list(
            filter(QuestionGenerator.verify_profile_topic, profile["topics"])
        )
        topics = list(
            map(lambda entry: (entry["topic"], entry["level"]), filtered_topics)
        )
        needs = list(map(lambda entry: entry["need"], filtered_topics))
        chosen_topic = random.choices(topics, weights=needs)[0]
        return QuestionGenerator.get_question(*chosen_topic)
