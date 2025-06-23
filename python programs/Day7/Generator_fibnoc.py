class Generate_fib(object):
    def generate_fib(self,num):
        # self.num = num
        a=0
        b=1
        for i in range(num):
            yield a
            a,b = b , a+b
obj = Generate_fib()

# it prints list of elements
print(list(obj.generate_fib(10)))

# to print single element from generator
for i in obj.generate_fib(10):
    print(i)