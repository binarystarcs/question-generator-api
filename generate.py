import logging
import random

class TopicLevelQuestionGenerator:
    generators = {}


class TopicQuestionGenerator:
    generators = {}


class QuestionGenerator:
    generators = {}

    @classmethod
    def register(cls, topic, level, weight=1.0):
        def decorator(fn):
            if topic not in cls.generators:
                cls.generators[topic] = TopicQuestionGenerator()
            cls.generators[topic].register(fn, level, weight=weight)
            return fn
        return decorator
    
    def get_question(topic, level, exact_level=False):
        topic_generator = QuestionGenerator.generators[topic]
        question = topic_generator.get_question(level, exact_level=exact_level)
        #TODO: Question to be stored in database!
        return question

    def verify_profile_topic(topic_entry):
        '''Topic entry is {topic: str, level: int, need: float}
           Returns True if able to generate a question.'''
        if (not 'topic' in topic_entry or
            not 'level' in topic_entry or
            not 'need' in topic_entry):
            return False
        return topic_entry['topic'] in QuestionGenerator.generators

    def get_question_from_profile(profile):
        # profile is a dictionary with entry topics: [{topic:, level:, need:}]
        if 'topics' not in profile:
            logging.error('Topics section absent from profile\n', profile)
            return None
        filtered_topics = filter(profile['topics'],
                                 QuestionGenerator.verify_profile_topics)
        topics = filtered_topics.map(lambda entry: (entry['topic'], entry['level']))
        needs = filtered_topics.map(lambda entry: entry['need'])
        chosen_topic = random.choices(topics, weights=needs)[0]
        return QuestionGenerator.get_question(*chosen_topic)


@QuestionGenerator.register("ADDITION", 1)
def generate_simple_sum():
    print("2+2=")
