def find_badge(text_file):
    with open(text_file, 'r') as infile:
        search_array = []
        priority_score_list = []
        for line in infile:
            search_array.append(line.strip())
            if len(search_array) % 3 == 0:
                common_character = str(set(search_array[0]).intersection(set(search_array[1]), set(search_array[2])))[2]
                priority_score_list.append(common_character)
                search_array = []
            
        
        item_score = 0
        for badge in priority_score_list:
            if badge.islower():
                item_score += ord(badge) - 96
                
            elif badge.isupper():
                item_score += ord(badge) - 38
        return item_score     
  




print(find_badge('data.txt'))

