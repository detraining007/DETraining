def Triangle_Pattern(lines):
    for element in range(lines):
        for value in range(element,lines):
           print(" ",end="  ")
        for star in range(element):
            print("*",end="  ")
        for final in range(element+1):
               print("*",end="  ")
        print("\n")    
           
         

if __name__ == "__main__":
    lin = int(input("Enter the no of lines you want: "))
    print(Triangle_Pattern(lin))
    

 