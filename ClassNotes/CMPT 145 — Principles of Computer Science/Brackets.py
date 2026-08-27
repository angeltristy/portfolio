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
#   Application: Bracket Matching Algorithm
#
# Check a string for matching brackets
# Uses the Queue and Stack ADTs

import Queue as Q
import Stack as S

example = '( ( ( ( ) ) )'

# create the initial empty containers
chars    = Q.Queue()
brackets = S.Stack()
unmatched_close = False


# put all the characters in the Queue
for c in example:
    chars.enqueue(c)


# brackets match if and only if every '(' has
# a corresponding ')'
while not chars.is_empty() and not unmatched_close:
    c = chars.dequeue()
    if c == '(':
        brackets.push(c)
    elif c == ')' and not brackets.is_empty():
        brackets.pop()
    elif c == ')' and brackets.is_empty():
        unmatched_close = True
    else:
        pass


# check how the analysis turned out
if unmatched_close:
    print("Found a ')' with no matching '('")
elif not brackets.is_empty():
    print("At least one '(' without a matching ')'")
else:
    print('Brackets matched')

