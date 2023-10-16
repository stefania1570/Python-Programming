#ex1: Find The greatest common divisor of multiple numbers read from the console.
import math
howMany = input("ex 1: How many numbers will you be entering?")

for index in range(0,int(howMany)): #TypeError: 'str' object cannot be interpreted as an integer - DE AIA int()
    if index == 0:
        gcd_Result = int(input())
    else: gcd_Result = math.gcd(gcd_Result,int(input()))

if howMany != 0:
    print("GCD:", gcd_Result)
else:
    print("You didn't enter any number.")

#ex2: Write a script that calculates how many vowels are in a string.
def count_vowels(inputStr):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    for char in inputStr:
        if char in vowels:
            vowel_count += 1
    return vowel_count

inputS = input("ex 2: Enter the string:")
vowel_count = count_vowels(inputS)
print("Number of vowels in the string:", vowel_count)

#ex3: Write a script that receives two strings and prints the number of occurrences of the first string in the second.
input1 = input("ex 3: Enter first string:")
input2 = input("Enter the second string:")
count = 0

if input1 not in input2:
    print("input1 can not be found in input2")
elif len(input1)>len(input2):
    print("First string is bigger than the second")
else:
    for i in range(0,len(input2)):
        #Luam pozitie cu pozitie si facem match la string-uri
        if input1 in input2[i:i+len(input1)]:
            count = count + 1
        #Daca i-ul urmator + lungimea sirului de cautat e mai mare decat sirul in care cautam => break
        if i+1+len(input1)>len(input2):
            break
print(f"Sirul 1 apare de {count} ori in sirul 2")
#sau, alta modalitate de print pt string formatting cu "%"
print("Sirul 1 apare de %d ori in sirul 2" % count)

#ex4: Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
import re #regular expressions

def convert_to_snake_case(input_string):
    # Use regular expressions to find A-Z and insert _ before them
    snake_case_string = re.sub(r'([A-Z])', r'_\1', input_string)
    # Remove leading underscore and convert to lowercase
    snake_case_string = snake_case_string[1:].lower() #sau cu .lstrip('_') - removes the _ din fata cuvantului
    return snake_case_string

# Example usage
input_string = "UpperCamelCaseString"
snake_case_result = convert_to_snake_case(input_string)
print("ex 4:", snake_case_result)

#ex5: Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example)
def spiral_order(matrix):
    if not matrix:
        return ""

    result = [] #empty list

    left, right = 0, len(matrix[0]) #nr de coloane (lungimea listei de pe poz 0)
    top, bottom = 0, len(matrix) #nr de randuri
    while left < right and top < bottom:
        #prima linie
        for i in range(left,right):
            result.append(matrix[top][i])
        top += 1
        #going down pe ultima coloana (cea mai din dreapta)
        for i in range(top,bottom):
            result.append(matrix[i][right - 1])
        
        right -= 1 #am terminat cu ultima coloana, restrangem dreptunghiul

        if not (left < right and top < bottom):
            break

        #ultima linie (de jos)
        for i in range(right-1,left -1, -1): #left-1 pt ca la range e INTERVAL DESCHIS LA CAPATUL DIN DREAPTA!!!
            result.append(matrix[bottom-1][i])
        bottom -= 1

        #prima coloana
        for i in range(bottom-1, top-1, -1):
            result.append(matrix[i][left])
        left += 1 

    return "".join(result)

# Example matrix - lista de liste!!
matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

result = spiral_order(matrix)
print("ex 5", result)

#ex6: Write a function that validates if a number is a palindrome 

string=input(("ex 6: Enter a number:"))
if(string==string[::-1]):  
      print("The number is a palindrome")  
else:  
      print("The number is not a palindrome")  

# ex7:  Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", 
#       this function will return 123, or if the text is "abc123abc" the function will extract 123). 
#       The function will extract only the first number that is found.

def extract_first_number(text):
    number = ""
    found_number = False

    for char in text:
        if char.isdigit():
            number += char
            found_number = True
        elif found_number:
            # iese din for cand intalnim un caracter care nu e cifra si am gasit un nr
            break

    if number:
        return int(number)
    else:
        return "No number"


text1 = "An apple is USD"
number1 = extract_first_number(text1)
print("ex7, primul exemplu:", number1)  

text2 = "abc123abc"
number2 = extract_first_number(text2)
print("ex7, al doilea exemplu:"number2)  

#ex8: Write a function that counts how many bits with value 1 a number has. 
# For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"

def count_set_bits(number):
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count

result = count_set_bits(24)
print("ex8 v1: Number of set bits in 24:", result)  # Output will be 2

#Alta varianta:
def count_set_bits(n):
    # Convert the integer to its binary representation
    binary_str = bin(n)
    
    # Count the number of '1's in the binary string
    count = binary_str.count('1')
    
    return count

# Example usage:
number = 24
bit_count = count_set_bits(number)
print(f'ex 8 v2: Number {number} has {bit_count} bits with value "1"')

#ex9:   Write a functions that determine the most common letter in a string. 
#       For example if the string is "an apple is not a tomato", 
#       then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. 
#       Casing should not be considered "A" and "a" represent the same character.

input_str = "an apple is not a tomato"

input_str_lower = input_str.lower()

letter_counts = {} #dictionary in python (key, value) pairs 
for char in input_str_lower:
    if char.isalpha():      
        # incrementam nr pt fiecare litera gasita
        letter_counts[char] = letter_counts.get(char, 0) + 1  

most_common = max(letter_counts, key=letter_counts.get)
count = letter_counts[most_common]

print("ex 9: The most common letter is '{}' - it appears {} times.".format(most_common, count))

#ex 10:  Write a function that counts how many words exist in a text.
#        A text is considered to be form out of words that are separated by only ONE space.
#        For example: "I have Python exam" has 4 words.

text = "I have Python exam"

words = text.split(" ")
words = list(filter(bool, words)) # functia bool elimina elementele nule ( 'bool("")' este 'False') pt ca daca avem 
                                  # mai mult de un spatiu, split va pune spatiul in plus drept cuvant
word_count = len(words)

print("ex 10: The number of words in the text is: {}".format(word_count))