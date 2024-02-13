def open_read (input_file):

    with open(input_file, 'r') as infile:

        num_array = []
        
        for line in infile:

            line = line.strip()
            left = 0
            right = len(line)-1

            while line[right].isalpha():
                right -= 1

            while line[left].isalpha():
                left += 1

            num_array.append(int(line[left] + line[right]))

    return sum(num_array)


print(open_read('input.txt'))


