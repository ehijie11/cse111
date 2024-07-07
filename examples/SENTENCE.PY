#EHIJIE OMIJIE

import random

def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]
    # Randomly choose and return a noun.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            words = ["drinks", "eats", "grows", "laughs", "thinks",
                     "runs", "sleeps", "talks", "walks", "writes"]
        else:
            words = ["drink", "eat", "grow", "laugh", "think",
                     "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh",
                 "will think", "will run", "will sleep", "will talk",
                 "will walk", "will write"]
    # Randomly choose and return a verb.
    word = random.choice(words)
    return word

def make_sentence(quantity, tense):
    """Build and return a sentence with three words:
    a determiner, a noun, and a verb. The grammatical
    quantity of the determiner and noun will match the
    number in the quantity parameter. The grammatical
    quantity and tense of the verb will match the number
    and tense in the quantity and tense parameters.
    """
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    sentence = f"{determiner.capitalize()} {noun} {verb}."
    return sentence

def main():
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

if __name__ == "__main__":
    main()
