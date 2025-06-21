# with open("E:\\vscodes\\DETraining\\sample_text.txt","r") as file:
#     r=file.read()
#     print(r)
#     file.close()

# with open("E:\\vscodes\\DETraining\\sample_text.txt","a+") as file:
#     file.write("\n opening in write + append open")#appends at the end
#     file.seek(0)#repositions cusor to beggining
#     r=file.read()
#     print(r)
#     file.close()

with open("E:\\vscodes\\DETraining\\sample_text.txt","w+") as file:
    file.seek(200)
    file.write("writing something using write + mode")
    file.seek(0)
    r=file.read()
    print(r)
    file.close()