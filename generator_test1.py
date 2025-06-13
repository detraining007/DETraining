#Program to implement generator and yeild - This is also called lazy evaluation
#This is used to generate one element at a time. if we use return for the generator function... it keeps creating memory stack and removing it. 
#We dont want to generate everything at once. so we are generating one by one without returning but yeilding. yeild keeps the function live
#where it keeps waiting.

#This is basic generator program taught in class

def generator_item(n):
    for i in range(n):
        yield i

if __name__=="__main__":
    n=int(input("Enter the number of items to be generated: "))
    for i in generator_item(n):
        print("Generated item:",i)

#This is the improvised code for different use
def generator_item(n):
    lst=['mango','banana','coconut','dragon fruit']
    lst1=['meena','meera','dimple','vandu']
    for i in range(len(lst)):
        yield lst1[i]+" likes "+lst[i]

if __name__=="__main__":
    n=int(input("Enter the number of items to be generated: "))
    for i in generator_item(n):
        print(i)