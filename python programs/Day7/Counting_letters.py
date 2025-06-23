class Counting(object):
    def counting_letters(self,list):
        count =1
        for i in range(len(list)-1):
            if list[i]==list[i+1]:
                count +=1
            else:
                print(list[i],"=",count,end="")
                count=1
obj = Counting()
name = input("Enter a name or string").lower()
list =[i for i in name]
list.sort()
print(list)
print(obj.counting_letters(list))