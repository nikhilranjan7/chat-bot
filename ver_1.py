# Simple Greeting input and Randomized Greeting output

import random

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def check_for_greeting(sentence):

    for word in sentence:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)

print(check_for_greeting(input('Greet me:\n').split(' ')))
