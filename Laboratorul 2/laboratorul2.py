# ex1: Write a function to return a list of the first n numbers in the Fibonacci string.
def generate_fibonacci(n):
    fibonacci_string = []
    a, b = 0, 1

    for i in range(n):
        fibonacci_string.append(a)
        a, b = b, a + b # !! single line swapping in python

    # Remove the first element (0) if the list is not empty
    if len(fibonacci_string) > 0:
        fibonacci_string.pop(0)

    return fibonacci_string

n = 7
fibonacci_string = generate_fibonacci(n)
print("ex 1: Fibonacci string:", fibonacci_string, "\n")

# ex2: Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    for i in range(2,number//2 + 1):
        if(number % i == 0):
            return False
    return True

def find_primes_in_list(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example usage:
numbers = [2, 3, 24, 4, 5, 6, 7, 8, 9]
prime_list = find_primes_in_list(numbers)
print("ex 2: Prime numbers in list:", prime_list, "\n")

# !!! ex 3: Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
def list_operations(a, b):
    # Intersection of 'a' and 'b'
    intersection = list(set(a) & set(b))

    # Union (reunion) of 'a' and 'b'
    union = list(set(a) | set(b))

    # Elements in 'a' but not in 'b'
    difference_a = list(set(a) - set(b))

    # Elements in 'b' but not in 'a'
    difference_b = list(set(b) - set(a))

    return intersection, union, difference_a, difference_b

#VARIANTA A 2-A EX 3!!!:
# def list_operations(a, b):
#     # Intersection of 'a' and 'b' while preserving the order
#     intersection = [x for x in a if x in b]

#     # Union (reunion) of 'a' and 'b' while preserving the order
#     union = a + [x for x in b if x not in a]

#     # Elements in 'a' but not in 'b' while preserving the order
#     difference_a = [x for x in a if x not in b]

#     # Elements in 'b' but not in 'a' while preserving the order
#     difference_b = [x for x in b if x not in a]

#     return intersection, union, difference_a, difference_b

# Example usage:
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
result = list_operations(a, b)
print("Intersection:", result[0])
print("Union:", result[1])
print("A - B:", result[2])
print("B - A:", result[3])

#ex 4: Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start 
# position (integer). The function will return the song composed by going though the musical notes beginning with the start position 
# and following the moves given as parameter.
#	Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"] 
def compose(notes, moves, start_position):
    # verificam daca poz de inceput este valida
    start_position = start_position % len(notes)

    composed_song = []
    composed_song.append(notes[start_position])

    for move in moves:
        start_position = (start_position + move) % len(notes)
        composed_song.append(notes[start_position])

    return composed_song

musical_notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2

result = compose(musical_notes, moves, start_position)
print("\nex 4: ", result)

# ex 4: Write a function that receives as parameter a matrix and will return the matrix obtained by 
# replacing all the elements under the main diagonal with 0 (zero).

def replace_in_matrix(matrix):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(num_rows):
        for j in range(num_cols):
            if i > j:
                matrix[i][j] = 0

    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = replace_in_matrix(matrix)
print("ex 5 - matrice rezultata:")
for row in result:
    print(row)

# ex 6: Write a function that receives as a parameter a variable number of lists and a whole number x. 
# Return a list containing the items that appear exactly x times in the incoming lists. 

def create_count(input_list):
    count = {}
    for item in input_list:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count

def find_items_appearing_x_times(x, *lists):
    all_items = []
    for list in lists:
        all_items = all_items + list

    count = create_count(all_items)
    result = [item for item, nr in count.items() if nr == x]
    return result

list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
x = 2

result = find_items_appearing_x_times(x, list1, list2, list3, list4)
print("ex 6 elemente ce apar de x ori in toate listele date:\n", result)

#ex 7: Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. 
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be 
# the greatest palindrome number.

def is_palindrome(number):
    # Convert the number to a string 
    number_str = str(number)
    return number_str == number_str[::-1] #collection[start:stop:step] => o sa dea reverse la string.
    #!!!! stop-ul e interval deschis deci va lua pana la indexul stop-1, inclusiv

def find_palindromes(numbers):
    palindrome_count = 0
    greatest_palindrome = None

    for number in numbers:
        if is_palindrome(number):
            palindrome_count += 1
            if greatest_palindrome is None or number > greatest_palindrome:
                greatest_palindrome = number

    return (palindrome_count, greatest_palindrome)

numbers = [121, 1331, 456, 787, 1001]
result = find_palindromes(numbers)
print("ex 7.1: Number of palindromes:", result[0])
print("ex 7.2: Greatest palindrome:", result[1])

# ex 8: Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
#  For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True, 
# otherwise it should contain characters that have the ASCII code not divisible by x.
# Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must return list of lists.

def process_strings(x=1, strings=[], flag=True):
    result = []
    
    for string in strings:
        filtered_chars = []
        for char in string:
            if flag:
             if (ord(char) % x == 0): # ord(char) - afla codul ascii al caracterului
                filtered_chars.append(char)
            else:
                if (ord(char) % x != 0):
                 filtered_chars.append(char)   
        result.append(filtered_chars)
    
    return result

x = 2
strings = ["test", "hello", "lab002"]
flag = False
output = process_strings(x, strings, flag)
print("ex8: ", output)

#ex 9: Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return 
# a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see the game 
# if there is at least one taller spectator standing in front of him. All the seats are occupied. All the seats are at the same level. 
# Row and column indexing starts from 0, beginning with the closest row from the field.

#	Example:
# FIELD
#[[1, 2, 3, 2, 1, 1],
#[2, 4, 4, 3, 7, 2],
#[5, 5, 2, 5, 6, 4],
#[6, 6, 7, 6, 7, 5]] 
#Will return : [(2, 2), (3, 4), (2, 4)] 

def find_obstructed_seats(matrix):
    obstructed_seats = []

    rows = len(matrix)
    cols = len(matrix[0])

    #citim matricea pe coloane
    for col in range(cols):
            for row in range(rows):
                for k in range(row):
                    if matrix[row][col] <= matrix[k][col]: 
                        obstructed_seats.append((row, col))
                        break
    return obstructed_seats

matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

result = find_obstructed_seats(matrix)
print("ex 9:", result)

# Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains the first items 
# in the lists, the second element contains the items on the position 2 in the lists, etc. 
# Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 

#Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to generate 
# max ([len(x) for x in input_lists]) tuples.

def merge_lists(*input_lists):
    max_len = max(len(x) for x in input_lists)
    result = []
    for i in range(max_len):
        tuple_items = tuple(x[i] if i < len(x) else None for x in input_lists) #pt fiecare lista, luam elementul cu acelasi index. daca nu avem, punem None
        result.append(tuple_items)
    return result

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

merged = merge_lists(list1, list2, list3)
print("ex 10:", merged)

# ex 11: Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. 
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def order_tuples(list):
    sorted_list = sorted(list, key=lambda x: x[1][2]) 
    return sorted_list

input_list = [('abc', 'bcd'), ('abc', 'zza')]
result = order_tuples(input_list)
print("ex 11: ", result)

# ex 12: Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme. 
# Two words rhyme if both of them end with the same 2 letters.
# Example: group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']] 

def group_by_rhyme(word_list):
    # dictionar -> pereche key-value unde cheile sunt rimele (ultimele 2 cuv)
    rhyme_groups = {}

    for word in word_list:
        rhyme = word[-2:]

        # daca rima gasita nu exista deja, o creem
        if rhyme not in rhyme_groups:
            rhyme_groups[rhyme] = []

        # adaugam cuvantul la grupul potrivit
        rhyme_groups[rhyme].append(word)

    # conversie dictionar->lista
    result = list(rhyme_groups.values())

    return result

words = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(words)
print("ex 12:", result)
