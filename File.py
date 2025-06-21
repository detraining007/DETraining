class Menu(object) :
    def __init__(self,filename,name):
       self.filename= filename  
       self.name=name
    
    def mode(self):
        self.name=input("Enter a to append file,\n Enter r to read file\n Enter w to write file ")
        return self.name
    
    def file_read(self):
        with open(self.filename,"r") as file:
           content=file.read()
           print(content)
        
   
    def file_write(self):
               try:
                  print("what u want to write")
                  content = input()
                  with open(self.filename,"w") as file:
                   file.write(content)
                   print(content)
               except Exception as err:
                    print("file is not found")
              
    
    def file_append(self):
            try:
               print("what u want to append?: ")
               content = input()
               with open(self.filename,"a") as file:
                file.write(content)
                print(content)
            except Exception as err:
                print("file is not found")


if __name__ == "__main__":
    filename = input("Enter the filename ")
    obj1 =Menu(filename,"name")
    choice=obj1.mode()
    if choice == "r":
        obj1.file_read()
    elif(choice == "w"):
        obj1.file_write()
    elif(choice == "a"):
        obj1.file_append()


