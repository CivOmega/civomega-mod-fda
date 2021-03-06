"""
contains `PATTERNS`, defining strings that this module may respond to
you can set anything you want here (which you can use in `parser.py`,
but you must set `PATTERNS`)
"""

# patterns for returning info about bills in congress
FOOD_RECALL_COUNT_PATTERNS = frozenset([
    
])

FOOD_RECALL_DETAIL_PATTERNS = frozenset([
    "what food recalls were because of {reason}",
])

# IMPORTANT:
#   * all questions must be unique (you can change the variable inside
#     the pattern if the wording is otherwise identical)
#   * the variable must be unique inside the question (you can't have
#     "what are {person} and {person} talking about" but you can have
#     "what are {person1} and {person2} talking about")

PATTERNS = FOOD_RECALL_COUNT_PATTERNS | FOOD_RECALL_DETAIL_PATTERNS