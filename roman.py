roman={'I':1,'V':5,'X':10,'L':50}
result=0
s='LVIII'

for i in range(len(s)):
        if s[i] == 'I':
            result+=roman['I']
            
        elif s[i]=='V':
            result+=roman['V']
            
        elif s[i] == 'L':
            result+=roman['L']
            

print(result)