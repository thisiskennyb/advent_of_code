def rps(text_file):
    score_dict = {
        "AX": 4,
        "AY": 8,
        "AZ": 3,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 7,
        "CY": 2,
        "CZ": 6
    }

    player_02_score = 0
    rubric_values = ''

    with open(text_file, 'r') as infile:
        for line in infile:
            rubric_values = line[0] + line[2]
            player_02_score += score_dict[rubric_values]
            rubric_values = ''
    return player_02_score

print(rps('rps.txt'))