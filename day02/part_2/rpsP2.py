# x - need to lose
# y - draw
# z - win

# x - rock
# y - paper
# z - scissors

def rps(text_file):
    score_dict = {
        "AX": 3,
        "AY": 4,
        "AZ": 8,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 2,
        "CY": 6,
        "CZ": 7
    }

    player_02_score = 0
    rubric_values = ''

    with open(text_file, 'r') as infile:
        for line in infile:
            rubric_values = line[0] + line[2]
            player_02_score += score_dict[rubric_values]
            rubric_values = ''
    return player_02_score

print(rps('data.txt'))