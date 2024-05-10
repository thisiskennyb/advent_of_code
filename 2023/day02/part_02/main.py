import re

def extract_game_id(game):
    game_id_pattern = r'Game (\d+)'
    match = re.search(game_id_pattern, game)
    game_number = int(match.group(1))
    return game_number   

def extract_random_cubes(game):
    cube_pattern = r'(\d+) (\w+)'
    matches = re.findall(cube_pattern, game)
    color_number_tuples = [(match[1], int(match[0])) for match in matches]
    return color_number_tuples

def find_product_of_set_values(set):
    product = 1
    for value in set.values():
        product *= int(value)  
    return product
    
def find_power_of_set(game):
    '''
    Return Game ID value if game is valid
    Else Return 0
    '''
    cube_counts = {
        "red": None,
        "green": None,
        "blue": None
    }
    
    random_cubes = extract_random_cubes(game)
    
    for cube in random_cubes:
        color, number = cube
        if not cube_counts[color]:
            cube_counts[color] = int(number)
        elif cube_counts[color] < int(number):
            cube_counts[color] = int(number)
            
    set_power = find_product_of_set_values(cube_counts)
    
    return set_power


def find_sum_of_powers(file):
    valid_game_id_sum = 0
    
    with open(file, "r") as infile:
        for line in infile:
            line.strip()
            valid_game_id_sum += find_power_of_set(line)
            
    return valid_game_id_sum
            
print(find_sum_of_powers("puzzle.txt"))