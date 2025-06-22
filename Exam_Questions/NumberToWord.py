def number_to_words(num):
    dict_01={"One": 1,"Two": 2,"Three":3,"Four": 4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9}
    dict_02={"Ten": 10,"Eleven": 11,"Twelve":12,"Thirteen": 13,"Fourteen":14,"Fifteen":15,"Sixteen":16,"Seventeen":17,"Eighteen":18,"Nineteen":19}
    dict_03={"Twenty": 20,"Thirty": 30,"Forty":40,"Fifty": 50,"Sixty":60,"Seventy":70,"Eighty":80,"Ninety":90}

    if num == 0:
        return "Zero"
    elif num < 10:
        for word, val in dict_01.items():
            if val == num:
                return word
    elif 10 <= num < 20:
        for word, val in dict_02.items():
            if val == num:
                return word
    elif num >= 20 and num < 100:
        tens = num // 10 * 10
        ones = num % 10
        tens_word = ""
        ones_word = ""
        for word, val in dict_03.items():
            if val == tens:
                tens_word = word
        if ones > 0:
            for word, val in dict_01.items():
                if val == ones:
                    ones_word = word
            return tens_word + " " + ones_word
        else:
            return tens_word
            
    else:
        return "Number out of range"
        
num=int(input("Enter the Number: "))
print(number_to_words(num))