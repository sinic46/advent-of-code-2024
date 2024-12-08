def get_input():
    with open('data.txt', 'r') as file:
        lines = file.readlines()
        return lines
    
    

def check_safty(data):
    safty = 0
    
    for line in data:
        line = line.strip()
        line = line.split(' ')
                
        num_line = [int(x) for x in line]
        
        print(f'testing:{num_line}')
        
        safe_row, idx = check_list(num_line)
        
        if(safe_row):
            safty += 1
            print(f'Row: {num_line} is safe')
        else:
            print(f'Row: {num_line} is not safe at index: {idx}')
            copy_line1 = num_line.copy()
            copy_line2 = num_line.copy()
            del copy_line1[idx+1]
            del copy_line2[idx]
            safe_row, idx = check_list(copy_line1)
            if(safe_row):
                safty += 1
                print(f'Row: {num_line} is safe')
            else:
                safe_row, idx = check_list(copy_line2)
                if(safe_row):
                    safty += 1
                    print(f'Row: {num_line} is safe')
                else:
                    print(f'Row: {num_line} is not safe at index: {idx}')


    return safty

def check_list(num_line):
    
    values = len(num_line)
    
    if num_line[0] < num_line[values - 1]:
            
        for idx, val in enumerate(num_line):
            
            if idx == values - 1:
                    return True,0
            
            if not 0 < num_line[idx + 1]- val <= 3:
                return False, idx
                
    else:
        for idx, val in enumerate(num_line):
            
            if idx == values - 1:
                return True,0
            
            if not 0 > num_line[idx + 1]- val >= -3:
                return False, idx





if __name__ == '__main__':
    file_data = get_input()
    
    safty = check_safty(file_data)
    
    print(safty)