import re

patterns = {'fox', 'dog', 'cat', 'rabbit'}
text = 'the quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('searching for "%s" -> %s' % (pattern, text))
    if re.search(pattern, text):
        print("matched")
    else:
        print("not matched")