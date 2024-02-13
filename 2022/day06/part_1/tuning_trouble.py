def tuning_trouble (text_file):

    with open(text_file, "r") as file:
        document_string = file.read()
  
    counter = 4
    test_list = list(document_string[:4])

    if len(test_list) == len(set(test_list)):
            return counter
    
    for char in range(4,len(document_string)):
        counter += 1
        test_list.pop(0)
        test_list.append(document_string[char])  
   
        if len(test_list) == len(set(test_list)):
            return counter




print(tuning_trouble('data.txt'))