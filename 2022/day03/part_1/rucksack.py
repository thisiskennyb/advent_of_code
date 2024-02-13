def rucksack(input_file):
    with open(input_file, 'r') as infile:
        item_list = []
        for line in infile:
            rucksack_1 = line[:int((len(line)/2))]
            rucksack_2 = line[int((len(line)/2)):]
            
            common_item = None
            for item in rucksack_1:
                if item in rucksack_2:
                    common_item = item
                    item_list.append(common_item)
                    common_item = None
                    break
       
        item_score = 0
        for thing in item_list:
            if thing.islower():
                item_score += ord(thing) - 96
                
            elif thing.isupper():
                item_score += ord(thing) - 38
        return item_score     



print(rucksack('data.txt'))