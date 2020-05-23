import random

adjectives = [
    "sleepy",
    "friendly",
    "grumpy",
    "wise",
    "hungry",
    "excited",
    "confused",
    "old"
]

things = [
    "hippo",
    "fox",
    "llama",
    "dinosaur",
    "dog",
    "boy",
    "duck",
    "elephant",
    "book",
    "sausage",
    "lemon",
    "table",
    "banana",
    "cheese"
]

actions = [
    "likes",
    "eats",
    "befriends",
    "fights",
    "helps"
]

def pick (list):
    return random.choice(list)

def optional (word):
    if (bool(random.getrandbits(1))):
        return word

    return ""

def remove_empty(parts):
    return [word for word in parts if word]

def form_sentence (*parts):
    return ' '.join(remove_empty(parts))

sentence = form_sentence(
    "The",
    optional(pick(adjectives)),
    pick(things),
    pick(actions),
    "the",
    optional(pick(adjectives)),
    pick(things)
)

print(sentence)

