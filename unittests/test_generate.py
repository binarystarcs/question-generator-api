import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current))

print(sys.path)

from engine.generate import QuestionGenerator


@QuestionGenerator.register("ADDITION", 1, 2.0)
def generate_simple_sum_a():
    return {"statement": "2+1="}


@QuestionGenerator.register("ADDITION", 1, 1.0)
def generate_simple_sum_b():
    return {"statement": "1+2="}


@QuestionGenerator.register("ADDITION", 2)
def generate_simple_sum_c():
    return {"statement": "2+2="}


@QuestionGenerator.register("ADDITION", 3)
def generate_simple_sum_d():
    return {"statement": "2+3="}


@QuestionGenerator.register("ADDITION", 4)
def generate_simple_sum_e():
    return {"statement": "2+4="}


@QuestionGenerator.register("ADDITION", 5)
def generate_simple_sum_e():
    return {"statement": "2+5="}


if __name__ == "__main__":
    first_question = QuestionGenerator.get_question("ADDITION", 2, exact_level=True)
    assert first_question["statement"] == "2+2=", "Level 2 question"

    second_question = QuestionGenerator.get_question("ADDITION", 5, exact_level=True)
    assert second_question["statement"] == "2+5=", "Level 5 question"

    third_question = QuestionGenerator.get_question("ADDITION", 1, exact_level=True)
    assert third_question["statement"] in ["1+2=", "2+1="], "Level 1 question"
