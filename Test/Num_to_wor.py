def num_to_wor(num):
    Units = {1:"one",
               2:"two",
               3:"three",
               4:"four",
               5:"five",
               6:"six",
               7:"seven",
               8:"eight",
               9:"nine",
               }
    Tens = {10:"Ten",
            20:"Twenty",
            30:"Thirty",
            40:"Fourty",
            50:"Fifty",
            60:"sixty",
            70:"seventy",
            80:"eighty",
            90:"ninety"}
    hundreds = {100:"One Hundred",200:"Two Hundred",300:"Three Hundred",400:"Four Hundred",500:"Five Hundred",600:"Six Hundred",700:"Seven Hundred",800:"Eight Hundred",900:"Nine Hundred"}
    thousands = {1000:"One Thousand",2000:"Two Thousand",3000:"Three Thousand",4000:"Four Thousand",5000:"Five Thousand",6000:"Six Thousand",7000:"Seven Thousand",8000:"Eight Thousand",9000:"Nine Thousand"}
    teens = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:'sixteen',17:"seventeen",18:"eighteen",19:"nineteeen"}
    lengths = []
    oig = num
    word = ""
    while(num !=0):
        og = num
        num = num//10
        rem = og%10
        lengths.append(rem)
    lengths.sort()
    val = 0
    if len(lengths) == 2:
            word = Tens[lengths[val]*10] +" "+ Units[lengths[val+1]]
            print(word)
    elif len(lengths) == 3:
         word = hundreds[lengths[val]*100] + " and " + " " + Tens[lengths[val+1]*10] +" "+ Units[lengths[val+2]]
         print(word)
    elif len(lengths) == 4:
         word = thousands[lengths[val]*1000]+hundreds[lengths[val+1]*100] + " and " + " " + Tens[lengths[val+2]*10] +" "+ Units[lengths[val+3]]
         print(word)


        








if __name__ == "__main__":
    num = int(input("Enter the number: "))
    print(num_to_wor(num))