# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#   Post-fix arithmetic evaluation

# An application of the Stack ADT
# and the Queue ADT

import Queue as Q
import Stack as S


def evaluate(expr):
    """
    Evaluate a postfix expression.
    Pre-conditions:
       expr: a string containing a postfix expression
    Post-Conditions:
        none
    Return:
        the value of the expression
    """

    # create the initial empty data structures
    expression = Q.Queue()
    evaluation = S.Stack()

    expr_list = expr.split()
    # put all the items in the Queue
    for c in expr_list:
        expression.enqueue(c)

    # evaluate the expression
    while not expression.is_empty():
        c = expression.dequeue()

        if c == '*':
            v1 = evaluation.pop()
            v2 = evaluation.pop()
            evaluation.push(v1*v2)
        elif c == '/':
            v1 = evaluation.pop()
            v2 = evaluation.pop()
            evaluation.push(v2/v1)
        elif c == '+':
            v1 = evaluation.pop()
            v2 = evaluation.pop()
            evaluation.push(v1+v2)
        elif c == '-':
            v1 = evaluation.pop()
            v2 = evaluation.pop()
            evaluation.push(v2-v1)
        else:
            evaluation.push(float(c))

    return evaluation.pop()


example = "3 4 + 5 *"
print('('+example+')', '=',evaluate(example))
