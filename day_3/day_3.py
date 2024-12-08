import re


def get_input():
    with open('data.txt', 'r') as file:
        lines = file.read()
        return lines
    

def search(data):
    matching_values = []
        
    matching_values += re.findall(r"mul\(\d{1,},\d{1,}\)|do\(\)|don't\(\)", data)
    
    return matching_values

def multiply(matching_values):
    
    state = True
    
    total = 0
    for value in matching_values:
        if 'don\'t' in value:
            state = False
        elif 'do' in value:
            state = True
        else:
            if state:
                values = value.split(',')
                total += int(values[0][4:]) * int(values[1][:-1])
    
    return total


if __name__ == '__main__':
    data = get_input()
    matching_values = search(data)
    
    print(matching_values)
    
    print(multiply(matching_values))
    
    