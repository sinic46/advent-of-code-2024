import re
def get_input():
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        return lines
    
def sort_lines(lines):
    rules = {}
    print_lines = []
    for line in lines:
        match = re.match(r'(\d{2})\|(\d{2})',line)
        
        if match:
            print(match.groups())
            
            if match.group(1) not in rules:
                rules[match.group(1)] = [match.group(2)]
            else:
                rules[match.group(1)].append(match.group(2))
            
        else:
            print_lines.append(line)
    
    
    
    
    return rules, print_lines
 
    
if __name__ == '__main__':
    rules, print_lines = sort_lines(get_input())
    
    print(rules['71'])