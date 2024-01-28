import pandas as pd
import random
import sys

from bb2 import *

# SCIENTIFIC TOPICS:
#   CHEMISTRY
#   BIOLOGY
#   PHYSICS
#   ELECTRICITY
#   SCIENTIFIC METHOD



questions = pd.read_csv("questions.csv")

def update_terminal(msg, questions=[]):
    global current_terminal_msg, current_questions
    current_terminal_msg = msg; current_questions = questions

def activate_inputs(mode="ABCD"):
    global inputs_on_off
    if mode == "ABCD":
        inputs_on_off = [1, 1, 1, 1]
    else:
        inputs_on_off = [1, 0, 1, 0]

def deactivate_inputs():
    global inputs_on_off
    inputs_on_off = [0, 0, 0, 0]


def ask_question(question_row):
    '''
    Asks the user a question based off its corresponding database row, then
    returns the correctness of the user's answer

    Parameters
    ----------
    question_row : int
        row number based on based on pandas row

    Returns
    -------
    bool
        True/False based on if answer correct
    '''
    global question_asked
    current_question = questions.iloc[question_row]['Question']
    answers = [questions.iloc[question_row][ f"Answer {i + 1}"] for i in range(4)]
    print(answers)
    answer_order = list(range(4)) ; random.shuffle(answer_order)
    print(answer_order)
    update_terminal(current_question, [answers[i] for i in answer_order])
    activate_inputs()
    answer_chosen = int(input())
    deactivate_inputs()
    if answer_order[answer_chosen] == 0:
        correct = True
        update_terminal('Correct!!')
        print('YAYYY')
    else:
        update_terminal('That is incorrect.')
        print('NOOOO')
        subract_time(20)
    question_asked_gets_false()
    print('whpps')
