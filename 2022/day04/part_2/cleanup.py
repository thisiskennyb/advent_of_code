def camp_cleanup(text_file):
    import re
    with open(text_file, 'r') as infile:
        count = 0
        for line in infile:
            numbers = re.findall(r'\d+', line)
            range1 = range(int(numbers[0]), int(numbers[1])+1)
            range2 = range(int(numbers[2]), int(numbers[3])+1)
            for num in range1:
               
                if num in range2:
                    count += 1
                    break
        return count

            



print(camp_cleanup('data.txt'))