# 4. Ввести з клавіатури число, що означає кількість доларів і центів. Вивести цю кількість прописом.
# Наприклад:
# How much money do you have?
# 123,34
# You have: one hundred twenty three dollars thirty four cents
WORDS = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
         17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
         60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 1000_000: 'million',
         1000_000_000: 'milliard'}


def digit_to_string(str_num, add_str=''):
    global WORDS
    if not str_num:
        return ""
    str_len = len(str_num)
    str_num = int(str_num)
    ones = str_num % 10
    tens = (str_num % 100) - ones
    hundreds = str_num - tens - ones
    if 10 <= str_num < 20 or str_len == 1:
        return WORDS[str_num] + ' ' + add_str
    elif str_num < 100:
        return WORDS[tens] + ' ' + WORDS[ones] + ' ' + add_str
    elif str_num < 1000:
        if tens // 10 == 1:
            return WORDS[hundreds // 100] + ' ' + WORDS[100] + ' ' + WORDS[tens + ones] + ' ' + add_str
        else:
            return WORDS[hundreds // 100] + ' ' + WORDS[100] + ' ' + WORDS[tens] + ' ' + WORDS[ones] + ' ' + add_str
    else:
        return ""


def number_converter(str_num):
    steps = [0, 1000, 1000_000, 1000_000_000]
    coins = str_num[len(str_num) - 2:]
    result = ' dollars ' + digit_to_string(coins, "cents") if coins != '00' else ''
    other_num = str_num[:len(str_num) - 3]
    num_list = []
    while len(other_num) >= 3:
        user_num = other_num[len(other_num) - 3:]
        num_list.append(user_num)
        other_num = other_num[:len(other_num) - 3]

    if len(other_num) > 0:
        num_list.append(other_num)
    print(num_list)
    for idx, i in enumerate(num_list):
        if i == '000':
            continue
        result = ' ' + digit_to_string(i, WORDS[steps[idx]]) + result
    return result.replace("  ", " ")


print(number_converter("113211,30"))
print(number_converter("222,22"))
print(number_converter("210,15"))
print(number_converter("543210,10"))
print(number_converter("15919123456,20"))
print(number_converter("1000000,00"))


# 5. Напишіть програму, яка переводить ціле число з римського запису до десяткового. Наприклад: XXII -> 22
roman_digits = {1000: 'M', 900: 'CM',  500: 'D', 400: 'CD',
                100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}


def int_to_roman(num):
    global roman_digits
    result = ""
    for kay, value in roman_digits.items():
        x = num // kay
        result += value * (x)
        num -= x * kay
    return result


print(int_to_roman(3))# "III"
print(int_to_roman(4))# "IV"
print(int_to_roman(9))# "IX"
print(int_to_roman(58))# "LVIII"
print(int_to_roman(1994))# "MCMXCIV"