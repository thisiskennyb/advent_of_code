def camp_cleanup(text_file):
    import re
    with open(text_file, 'r') as infile:
        count = 0
        for line in infile:
            numbers = re.findall(r'\d+', line)
            range1 = range(int(numbers[0]), int(numbers[1]))
            range2 = range(int(numbers[2]), int(numbers[3]))
            if range1.start <= range2.start and range1.stop >= range2.stop:
                count += 1
            elif range2.start <= range1.start and range2.stop >= range1.stop:
                count += 1

        return count

            



print(camp_cleanup('data.txt'))
