# file = open("E:\IHUB Full Stack Java\_ram.txt","r")
# # file = open("E:\IHUB Full Stack Java\java Notes\java5.txt","r")
#
# lines = file.readline()
# file.write("hey ramu miriyala")
# print(lines)

# file reading and writing by using "r+"
# with open("E:\IHUB Full Stack Java\_ram.txt", "r+") as file:
#     lines = file.readline()
#     file.write("\nhey ramu miriyala")  # Writing on a new line
#     print(lines)

with open("E:\IHUB Full Stack Java\_ram.txt","r")as file:
    lines = file.readlines()
    for line in lines:
        print(line)
file.close()

with open("E:\IHUB Full Stack Java\_ram.txt","a") as file:
    file.write("\nhow r u")
file.close()
