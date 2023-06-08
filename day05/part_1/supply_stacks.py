def supply_stacks(text_file):
    with open(text_file, 'r') as infile:
        stack_row_list = []
        stack_dict = {}
        index_dict = {}
        for line in infile:
            if line.startswith('move'):
                pass

# builds a list with the first lines in the data.txt that contain the column numbers with stack of boxes
# if iterating backwards through list it starts from bottom row of column numbers and goes through box rows
# did not strip() line so all indexs correspond with correct column numbers
            elif line.strip() != '':
                stack_row_list.append(line)
        
# creates two dictionaries, stack_dict key=column# value=[]
# index_dict key=index of column number value=column number corresponding to index
        column_numbers = stack_row_list.pop()
        for i in range(len(column_numbers)):
            if column_numbers[i].isdigit():
                index_dict[i] = column_numbers[i]
                stack_dict[column_numbers[i]] = []


# fills the stack dictionary with the default box stack configiration 
        for row in stack_row_list[::-1]:
            for j in range(len(row)):
                if row[j].isalpha():
                    stack_dict[index_dict[j]].append(row[j])
                    

        return stack_dict

official_stack_dictionary = supply_stacks('data.txt')

def restack(stack, text_file):
    import re
    with open(text_file, 'r') as infile:
        for line in infile:
# grabs the values needed to know how many boxes to take from a stack and put on another stack
            if line.startswith('move'):
                matches = re.findall(r"\d+", line)
                box_quantity_to_move = matches[0]
                from_column = matches[1]
                to_column = matches[2]

#This takes the values from above and applies them to the proper dictionary values             
                for box in range(int(box_quantity_to_move)):
                    grab_and_move = stack[from_column].pop()
                    stack[to_column].append(grab_and_move)

#return the values of the top box from every stack
        top_boxes = ''
        for key in range(1, len(stack) + 1):
            top_boxes += str(stack[str(key)].pop())
        return top_boxes


print(restack(official_stack_dictionary, 'data.txt'))





