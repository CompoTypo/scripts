# INPUT MUST BE AN INT
import sys

# Original roman numeral notation used strike overs instead of switching cases
RomanNumerals = {
    'M': 1000000,
    'D': 500000,
    'C': 100000,
    'L': 50000,
    'X': 10000,
    'V': 5000,
    'm': 1000,
    'd': 500,
    'c': 100,
    'l': 50,
    'x': 10,
    'v': 5,
    'I': 1
}

def RomanNumerizer(num):
    roman_numeral = ''
    for numeral, value in RomanNumerals.items():
        while num >= value:
            num -= value
            roman_numeral += numeral
        if num == 9:
            roman_numeral += 'Ix'
            break
        elif num == 4:
            roman_numeral += 'Iv'
            break

    print(roman_numeral)

if len(sys.argv) != 2:
    RomanNumerizer(int(input('Enter an integer: ')))
else:
    RomanNumerizer(int(sys.argv[1]))