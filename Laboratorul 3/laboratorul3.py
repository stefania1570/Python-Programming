#ex1: Write a function that receives as parameters two lists a and b and returns a list of sets containing: 
# (a intersected with b, a reunited with b, a - b, b - a)

def set_operations(a, b):
    # Converteste listele in seturi ca sa putem face operatii cu ele
    set_a = set(a)
    set_b = set(b)

    intersection = set_a.intersection(set_b)  
    union = set_a.union(set_b) 
    a_minus_b = set_a.difference(set_b)  
    b_minus_a = set_b.difference(set_a)

    result = [intersection, union, a_minus_b, b_minus_a]
    return result

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
result = set_operations(a, b)
print("ex 1 - operatii cu seturi: ", result)

# ex2: Write a function that receives a string as a parameter and returns a dictionary in which the keys are
# the characters in the character string and the values are the number of occurrences of that character in the given text.

def count_characters(text):
    dictionary = {}
    
    for char in text:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    
    return dictionary

input_string = "ana are mere"
result = count_characters(input_string)
print("ex 2 - dictionary de frecventaa caracterelor: ", result)
# sau:
# return {i: text.count(i) for i in set(text)}

# ex3: Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must 
# be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

def compare_dicts(dict1, dict2):
    # comparam daca au acelasi set de chei
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]

        # Check if the values are dictionaries and compare them recursively
        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dicts(value1, value2):
                return False
        # pt liste
        elif isinstance(value1, list) and isinstance(value2, list):
            if not compare_lists(value1, value2):
                return False
        # pt seturi
        elif isinstance(value1, set) and isinstance(value2, set):
            #seturile sunt NEORDONATE deci le putem compara folosind operatori. in schimb, la liste putem avea elemente duplicat
            if value1 != value2:
                return False
        else:
            if value1 != value2:
                return False

    return True

def compare_lists(list1, list2):

    if len(list1) != len(list2):
        return False

    for item1, item2 in zip(list1, list2):
        if isinstance(item1, dict) and isinstance(item2, dict):
            if not compare_dicts(item1, item2):
                return False
        elif isinstance(item1, list) and isinstance(item2, list):
            if not compare_lists(item1, item2):
                return False
        elif isinstance(item1, set) and isinstance(item2, set):
            if item1 != item2:
                return False
        else:
            if item1 != item2:
                return False

    return True

dict1 = {'a': 1, 'b': {'c': [1, 2, 3]}, 'd': [4, 5]}
dict2 = {'a': 1, 'b': {'c': [1, 2, 3]}, 'd': [4, 5]}

result = compare_dicts(dict1, dict2)
print("ex 3 - comparare recursiva dictionare:", result) 

# ex 4: The build_xml_element function receives the following parameters: tag, content, and key-value elements given 
# as name-parameters. Build and return a string that reabcsents the corresponding XML element.
# Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") 
# returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

# **ceva = variable number of keyword arguments (key-value pairs)
def build_xml_element(tag, content, **parameters):
    return "<" + tag + " " + r" ".join([p[0]+" = \"" + p[1] + "\"" if type(p[1]) == str else p[0]+" = " + str(p[1])
                                        for p in parameters.items()])+">"+content+"</"+tag+">"

print("ex 4 - ", build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") )

# ex 5: The validate_dict function that receives as a parameter a set of tuples ( that reabcsents validation rules for
# a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: 
# (key, "abcfix", "middle", "suffix"). A value is considered valid if it starts with "abcfix", "middle" is inside the value 
# (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all 
# the rules, False otherwise.

def validate_dict(rules, dictionary):
    for key, abcfix, middle, suffix in rules:
        if key not in dictionary:
            return False
        value = dictionary[key]
        if not value.startswith(abcfix):
            return False
        # exclude primul si ultimul caracter
        if middle not in value[1:-1]:
            return False
        if not value.endswith(suffix):
            return False
    return True

rules = [
    ("1", "abc", "mid", "suf"),
    ("2", "abc", "xyz", "123")
]

my_dict = {
    "1": "abcfixmiddlesuf",
    "2": "abcdefgxyz123"
}

result = validate_dict(rules, my_dict)
print("ex 5 - ", result) 

#ex 6: Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of 
# unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve 
# this objective).

def form_tuple(list):
    return len(set(list)), len(list) - len(set(list))

list = [1, 2, 3, 3, 4, 4, 4, 5]
result = form_tuple(list)
print("ex 6 - tuplu :", result)  

# ex 7:

def set_operations(*sets):
    result = {}
    for i in range(0, len(sets) - 1):
        for j in range(i + 1, len(sets)):
            result.update({(str(sets[i]) + " | " + str(sets[j])): (sets[i] | sets[j]),
                           (str(sets[i]) + " & " + str(sets[j])): (sets[i] & sets[j]),
                           (str(sets[i]) + " - " + str(sets[j])): (sets[i] - sets[j]),
                           (str(sets[j]) + " - " + str(sets[i])): (sets[j] - sets[i])})
    return result

set1 = {1, 2}
set2 = {2, 3}
result = set_operations(set1, set2)
print("ex 7 - set operations:", result)

# ex 8 dar notat cu 10: Write a function that receives a single dict parameter named mapping. This dictionary always contains a string 
# key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the 
# following way: the value of the current key is the key for the next value, until you find a loop (a key that was visited 
# before). The function must return the list of objects obtained as previously described.

# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will return ['a', '6', 'z', '2']

def loop(mapping):
    to_return = []
    value = mapping['start']
    while value not in to_return:
        to_return.append(value)
        value = mapping[value]
    return to_return

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = loop(mapping)
print("ex 10 - ", result)  # ['a', '6', 'z', '2']

# ex 11: Write a function that receives a variable number of positional arguments and a variable number of keyword arguments and will return 
# the number of positional arguments whose values can be found among keyword arguments values. 
# Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return return 3

def my_function(*arguments, **keywords):
    return len([pos_argument for pos_argument in arguments if pos_argument in keywords.values()])

print("ex 11: ", my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5))