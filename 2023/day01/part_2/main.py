# Initialize dictionary with number words as keys and their corresponding values
# Initialize two arrays prefix and suffix
# Initialize two variables for left digit and right digit
# append all of the letters in the string that do not include numbers
# check both strings against the dictionary and set value if found
# else find the first digits



def prefix_suffix_letters(s):
    """
    Given an input string this function returns two strings:
     first string - prefix substring if all letters else empty
     second string - suffix substring if all letters else empty 
    """
    left = 0
    right = len(s)-1

    while s[right].isalpha():
        right -= 1

    while s[left].isalpha():
        left += 1

    return [s[:left], s[right+1:]]


print(prefix_suffix_letters("6iuhu6dfsd"))

#start a substring with size length of three. Lengthen the substring by one
#until it is length of five. Increase the left pointer by one and reset the 
#substring to lenght of three
def find_num_string(arr):
    """
    The input for this function is an array containing two strings
    the strings can be empty
    The function returns an array with values
     of the number string if found else an empty string
    """
    
    pass


# def open_read (input_file):

#     with open(input_file, 'r') as infile:

#         num_dict = {
#             "one": "1",
#             "two": "2",
#             "three": "3",
#             "four": "4",
#             "five": "5",
#             "six": "6",
#             "seven": "7",
#             "eight": "8",
#             "nine": "9"
#         }

    #     num_array = []
        
    #     for line in infile:

    #         line = line.strip()
    #         left = 0
    #         right = len(line)-1

    #         while line[right].isalpha():
    #             right -= 1

    #         while line[left].isalpha():
    #             left += 1

    #         num_array.append(int(line[left] + line[right]))

    # return sum(num_array)


# print(open_read('input.txt'))