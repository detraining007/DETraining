def num_to_words(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
            "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    units = [(10000000, "Crore"), (100000, "Lakh"), (1000, "Thousand"), (100, "Hundred")]

    def two_digit_words(n):
        if n < 20:
            return ones[n]
        else:
            return tens[n // 10] + (" " + ones[n % 10] if n % 10 != 0 else "")

    def convert(n):
        if n == 0:
            return "Zero"
        words = ""
        for value, name in units:
            count = n // value
            if count != 0:
                words += convert(count) + " " + name + " "
                n %= value
        if n > 0:
            if words and n < 100:
                words += "and "
            words += two_digit_words(n)
        return words.strip()

    return convert(n)


print(num_to_words(1234))         # Output: One Thousand Two Hundred and Thirty Four
print(num_to_words(204501))       # Output: Two Lakh Four Thousand Five Hundred and One
print(num_to_words(98765432))     # Output: Nine Crore Eighty Seven Lakh Sixty Five Thousand Four Hundred and Thirty Two