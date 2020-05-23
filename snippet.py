import random

adjectives = [
    "fast",
    "friendly",
    "grumpy",
    "wise",
    "hungry",
    "excited"
]

characters = [
    "hippo",
    "fox",
    "dog",
    "boy"
]

actions = [
    "likes",
    "eats",
    "reads",
    "deserves"
]

items = [
    "books",
    "maths papers",
    "chocolate",
    "cheese",
    "sausages"
]

def pick (list):
    return random.choice(list)

def form_sentence (*parts):
    return ' '.join(parts)

sentence = form_sentence(
    "The",
    pick(adjectives),
    pick(characters),
    pick(actions),
    pick(items)
)

print(sentence)

