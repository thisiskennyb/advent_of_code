import re

def extract_prefix_suffix_letters(s):
    left = 0
    right = len(s)-1

    while s[right].isalpha() and right > 0:
        right -= 1

    while s[left].isalpha() and left < len(s)-1:
        left += 1

 
    return [s[:left], s[right+1:]]

def find_digits(s):
    first_int = ''
    last_int = ''
    
    pattern = r'\d'
    # Use findall to extract all digits from the string
    digits = re.findall(pattern, s)

    first_digit = digits[0] if digits else ''
    last_digit = digits[-1] if digits else ''
    
    return [first_digit, last_digit]
    
    

def find_numeric_string(s):
    pattern = r'(one|two|three|four|five|six|seven|eight|nine)'
    matches = re.findall(pattern, s)
    return matches
    
def convert_to_num(num_string):
   
    num_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    return num_dict[num_string]
    

def find_calibration_value(line):
    prefix_suffix_letters = extract_prefix_suffix_letters(line)

    digits = find_digits(line)
 
    
    prefix_letters = prefix_suffix_letters[0]
    suffix_letters = prefix_suffix_letters[1]
    
    is_first_digit = find_numeric_string(prefix_letters) if prefix_suffix_letters[0] else ''
    is_last_digit = find_numeric_string(suffix_letters) if prefix_suffix_letters[1] else ''
    
    if_first_digit = convert_to_num(is_first_digit[0]) if is_first_digit else ''
    if_last_digit = convert_to_num(is_last_digit[-1]) if is_last_digit else ''
    
    print(int("".join([if_first_digit if if_first_digit else digits[0], if_last_digit if if_last_digit else digits[-1]])))
    return int("".join([if_first_digit if if_first_digit else digits[0], if_last_digit if if_last_digit else digits[-1]]))
    


def sum_calibration_values(file):
    
    calibration_value_sum = 0
    
    with open(file, 'r') as infile:
        
        for line in infile:
            line = line.strip()
            calibration_value_sum += find_calibration_value(line)
            
    return calibration_value_sum


print(sum_calibration_values('input.txt'))