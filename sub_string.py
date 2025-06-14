def is_sub_string(sub,main):
        check=[]
        for i in range(len(sub)):
          for j in range(len(main)):
             if sub[i] == main[j]:
                 check.append(sub[i])
                 main=main.replace(main[j],'')
                 break
        str=''.join(check)
        if str == sub:
            return True
        return False
sub='alex'
main='aaleex'

print(is_sub_string(sub,main))
