with open("C:\\Users\\BODDULA MANEESH\\OneDrive\\Desktop\\Data engineering\\DETraining\\abc.txt","r") as file:
    reading = file.read()
    print(reading)
    file.close()

with open("C:\\Users\\BODDULA MANEESH\\OneDrive\\Desktop\\Data engineering\\DETraining\\abc.txt","a+") as file:
    file.write("\nmy name is maneesh")
    reading = file.read()
    print(reading)
    file.close()

with open("C:\\Users\\BODDULA MANEESH\\OneDrive\\Desktop\\Data engineering\\DETraining\\abc.txt","w+") as file:
    file.write("\n data engineering")
    reading = file.read()
    print(reading)
    file.close()


with open("C:\\Users\\BODDULA MANEESH\\OneDrive\\Desktop\\f1.txt","r") as file:
    ride = file.read()
    print(ride)

    
