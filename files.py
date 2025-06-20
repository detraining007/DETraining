#with open('practice.py','r') as file:
 #   f=file.read()
#    print(f)

try:
    while True:
        inp=input('Enter a file name:')
        operation=input("Which operation you want to perform 'r','w','a':")
        with open(inp,operation) as file:
            if operation == 'r' :
                f=file.read()
                print(f)
                file.close()
            elif operation == 'w':
                text=input('Write anthing to file:')
                f=file.write(text)
                file.close()
            #elif operation == 'a':
              #  f=file.append(
except FileNotFoundError:
                print(inp,' is not available')
                with open(inp,'w') as file:
                    file=inp.read()
                    print(file)
            
