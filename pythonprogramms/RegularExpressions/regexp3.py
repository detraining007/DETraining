import re
patterns=["fox","dog","horse"]
text="The quick brown fox jumps over the lazy dog."
for pattern in patterns:
    print('Searching for "%s" in "%s" -> ' %(pattern,text))
    if re.search(pattern,text):
        print("Matched")
    else:
        print("Not Matched")

