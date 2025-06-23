class File_Acess(object):
    def write_file(self,stmt):
        self.stmt = stmt
        with open("created_file.txt","a") as file:
            file.write(f"\n{self.stmt}")
        file.close()
    def read_file(self):
        with open("created_file.txt","r") as file:
            lines = file.readlines()
            print(lines)
        file.close()
obj = File_Acess()
choice = int(input("Enter ur choice 1=write or 2=read"))
if choice == 1:
    stmt = input("Enter what you want write in file")
    obj.write_file(stmt)
elif choice ==2:
    obj.read_file()
else:
    print("you didn't choose correct choice, so we are closing")

