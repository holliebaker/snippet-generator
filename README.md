# Snippet Generator

The aim is to generate (hopefully) funny snippets of text to help us train our speech models.

## How to use

```bash
# install required packages
$ pip install -r requirements.txt
# define configuration
$ vi settings.yml
# generate words!
$ python snippet.py
```

## Word list and structure specification

Word list and sentence structure configuration is done in `settings.yml`
- `structure`: specify thesentence structure.
  - Words in curly brackets indicate a choice from a word list
  - question mark before the curly brackets indicates that this word is optional
  - Extra whitespace is ignored - all words are separated by a single space
  - Words can be statically inserted into a sentecnce by typing them without the curly brackets
- `words`: specify word list locations.
  - Word lists are text files containing one word per line
  - The key for each word list represents one of the template words (in curly brackets) from the sentence structure.
  - For example, if structure is `Hello, {name}`, then `words` must have a key called `name` pointing to a text file
    (presumably of names)

### Example configuration
```yaml
---

structure: "The ?{adjective} {noun} {verb}"
words:
  verb: words/verbs.txt 
  noun: words/nouns.txt 
  adjective: words/adjective.txt

```

## Sample words and config

Please see https://github.com/holliebaker/snippet-generator-config.

