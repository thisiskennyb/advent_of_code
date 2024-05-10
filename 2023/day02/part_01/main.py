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
    
def determine_valid_game(game):
    '''
    Return Game ID value if game is valid
    Else Return 0
    '''
    valid_game_params = {
        "red": 12,
        "green": 13,
        "blue": 14,       
    }
    
    game_id = extract_game_id(game)
    
    random_cubes = extract_random_cubes(game)
    
    for cube in random_cubes:
        if valid_game_params[cube[0]] < int(cube[1]):
            return 0
    
    return game_id


def find_game_id_sum(file):
    valid_game_id_sum = 0
    
    with open(file, "r") as infile:
        for line in infile:
            line.strip()
            valid_game_id_sum += determine_valid_game(line)
            
    return valid_game_id_sum
            
print(find_game_id_sum("puzzle.txt"))