import pandas as pd


def get_input():
    with open('list.txt', 'r') as file:
        dataframe = pd.read_csv(file, header=0,delimiter='   ',engine='python')
        return dataframe

def order_data(data: pd.DataFrame):
    data0 = data['col1'].sort_values().tolist()
    data1 = data['col2'].sort_values().tolist()
    
    
    return data0, data1

def find_difference(df1:list, df2:list):
    
    diff = 0
    
    for idx, val in enumerate(df1):
        if val != df2[idx]:
            current_diff = df2[idx] - df1[idx]
            if current_diff < 0:
                current_diff = current_diff * -1
                
            diff += current_diff
    
    
    return diff

def find_occurrences(list1, list2):
    orrurrences = 0
    
    for idx, val in enumerate(list1):
        val_count = list2.count(val)
        
        orrurrences += val_count * val
        
    return orrurrences




if __name__ == '__main__':
    file_data = get_input()
    
    list1, list2 = order_data(file_data)
    
    diff = find_difference(list1, list2)
    
    occurrences = find_occurrences(list1, list2)
    
    print(occurrences)
