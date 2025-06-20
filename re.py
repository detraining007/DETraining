import re
txt='The tiser is national animal of india'
s=re.findall('is',txt,)
print(s)
if s:
    print('Found')
else:
    print('Not Found')
