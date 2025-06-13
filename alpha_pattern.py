def generate_pattern():
    letters=['A','B','C','D','E','F']
    total_lines=6
    max_index=len(letters)-1
    for i in range(total_lines):
        left_part=''
        for j in range(max_index-i+1):
            left_part +=letters[j] + ' '
        middle_space='  '*(2*i-1+1) if i!=0 else ''
        right_part=''
        for j in range(max_index-i,-1,-1):
            right_part+=letters[j] + ' '
        print(left_part+middle_space+right_part.strip())
if __name__=="__main__":
    generate_pattern()
