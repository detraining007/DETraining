ones = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ten = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def wordForNumber():
    num = input("Enter a number : ").strip()
    if not num.isdigit():
        print("Please enter a valid integer number.")
        return
    length = len(num)
    n = int(num)
    res = ""
    for l in range(length - 1,-1,-1):
        p = n // 10 ** l
        n -= p * 10 ** l
        if p == 0:
            continue
        if(l == 0):
            res += " " + ones[p]
        elif(l == 1):
            if(p > 1):
                res += " " + tens[p-2]
            elif(p == 1):
                res += ten[n]
                print(res)
                return
            else:
                continue
        elif(l == 2):
            res +=  " " + ones[p] + " hundered"
        elif(l == 3):
            res +=  " " + ones[p] + " thousand"
    print(res)

wordForNumber()