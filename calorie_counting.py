def calorie_counting(text_file):
    most_calories = 0
    calorie_counter = 0
    cals_per_elf = []
    with open(text_file, 'r') as infile:
        for line in infile:
            if len(line.strip()) > 0:
                calorie_counter += int(line.strip())       
            elif len(line.strip()) == 0:
                cals_per_elf.append(calorie_counter)
                calorie_counter = 0
    return sum(sorted(cals_per_elf)[-3:])
                

               
    return most_calories


print(calorie_counting('calories.txt'))