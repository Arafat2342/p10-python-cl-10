# Taking user input
n = float(input('Enter a number: '))
p = n


# Converting to binary

bi = ''
decimal_bi = ''
whole_num = int(n)
decimal_fraction_num = n - whole_num

# Converting the whole number part to binary
while whole_num > 0:
    rem = whole_num % 2
    bi = str(rem) + bi
    whole_num = whole_num // 2

# converting the decimal fraction number to binary

if decimal_fraction_num > 0:
    max_decimal_numlen = 0
    decimal_bi = '.'

    while decimal_fraction_num > 0 and max_decimal_numlen < 10:
        decimal_fraction_num *= 2
        decimal_bi += str(int(decimal_fraction_num))
        decimal_fraction_num -= int(decimal_fraction_num)
        max_decimal_numlen += 1

result = float(bi + decimal_bi)

print(f"Converting ({p})₁₀ to binary: ({result})₂")