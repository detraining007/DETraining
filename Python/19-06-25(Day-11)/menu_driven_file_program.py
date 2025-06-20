#To implement menu driven file operations

def file_operations(file_name,mode):
    while True:
        if mode=="w":
            with open(file_name,mode) as file:
                context=file.write("Im in python class")
                print("Successful written content to the file ",file_name)
                file.close()
        elif mode=="r":
            try:
                with open(file_name,"r") as file:
                    context=file.read()
                    print(context)
                    print("Successful read the content to the file ",file_name)
                    file.close()
            except:
                with open(file_name,"w") as file:
                    context=file.write("Im in python class of except class")
                    print(context)
                    print("Successful written content to the file ",file_name)
                    file.close()

        elif mode=="a":
            with open(file_name,"a") as file:
                context=file.write("\nIm the newly appended line")
                print("Successful appended the content to the file ",file_name)
                file.close()
        else:
            print("Entered wrong mode")
            choice=input("If you want to try again the yes or else no: ")
            if choice=="yes":
                continue
            else:
                print("Terminating the program")
                break
        break


if __name__=="__main__":
    variable="example8.txt"
    mode="r"
    file_operations(variable,mode) 