import re
def is_pangram(sentence):
    my_set_alphabets=set()
    pattern='[a-zA-Z]'
    for i in range(len(sentence)):
        if re.match(pattern, sentence[i]):
            my_set_alphabets.add(sentence[i].lower())
    if len(my_set_alphabets)!=26:
        return False
    return True
