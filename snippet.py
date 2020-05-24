import random
import re
import yaml

settings = {}

with open("settings.yml", 'r') as stream:
    try:
        settings = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

def load_word_list (filename):
    with open(filename, 'r') as f:
        return [word.strip() for word in f.readlines()]

def pick (list):
    return random.choice(list)

def optional (word, optional):
    if (not optional or bool(random.getrandbits(1))):
        return word

    return None

def remove_empty(parts):
    return [word for word in parts if word]

def form_sentence (*parts):
    return ' '.join(remove_empty(parts))

def process_word (part):
    match = re.match('^(\?)?\{(\w+)\}$', part)

    if not match:
        return part

    is_optional = bool(match.group(1)) # ?
    list = match.group(2)

    return optional(pick(word_lists.get(list)), is_optional)

def not_none (l):
    return [x for x in l if x is not None]

structure = settings.get('structure').split(' ')
# load possible word lists
word_lists = settings.get('words')
for list in word_lists:
    word_lists[list] = load_word_list(word_lists.get(list))

sentence = ' '.join(not_none([process_word(part) for part in structure]))

print(sentence)

