forever = True

end_list = []
while forever:
    input_numbers = input('Please enter a number you want to sort: ')
    if 'done' in input_numbers.lower():
        forever = False
    elif int(input_numbers) > 100:
        print('Number not added since, it is above 100')
    else:
        end_list.append(int(input_numbers))

group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0
group_5 = 0
group_6 = 0
group_7 = 0
group_8 = 0
group_9 = 0
group_10 = 0
group_11 = 0
group_12 = 0
group_13 = 0
group_14 = 0
group_15 = 0
group_16 = 0
group_17 = 0
group_18 = 0
group_19 = 0
group_20 = 0
group_21 = 0

for x in end_list:
    if x < 5:
        group_1 += 1
    elif x < 5:
        group_2 += 1
    elif x < 10:
        group_3 += 1
    elif x < 15:
        group_4 += 1
    elif x < 20:
        group_5 += 1
    elif x < 25:
        group_6 += 1        
    elif x < 30:
        group_7 += 1       
    elif x < 35:
        group_8 += 1      
    elif x < 40:
        group_9 += 1     
    elif x < 45:
        group_10 += 1
    elif x < 50:
        group_11 += 1 
    elif x < 55:
        group_12 += 1      
    elif x < 60:
        group_13 += 1
    elif x < 65:
        group_14 += 1        
    elif x < 70:
        group_15 += 1       
    elif x < 75:
        group_16 += 1      
    elif x < 80:
        group_17 += 1      
    elif x < 85:
        group_18 += 1    
    elif x < 90:
        group_19 += 1 
    elif x < 95:
        group_20 += 1
    elif x < 100:
        group_21 += 1

print(f'There are {group_1} numbers in group 1')
print(f'There are {group_2} numbers in group 1')
print(f'There are {group_3} numbers in group 1')
print(f'There are {group_4} numbers in group 1')
print(f'There are {group_5} numbers in group 1')
print(f'There are {group_6} numbers in group 1')
print(f'There are {group_7} numbers in group 1')
print(f'There are {group_8} numbers in group 1')
print(f'There are {group_9} numbers in group 1')
print(f'There are {group_10} numbers in group 1')
print(f'There are {group_11} numbers in group 1')
print(f'There are {group_12} numbers in group 1')
print(f'There are {group_13} numbers in group 1')
print(f'There are {group_14} numbers in group 1')
print(f'There are {group_15} numbers in group 1')
print(f'There are {group_16} numbers in group 1')
print(f'There are {group_17} numbers in group 1')
print(f'There are {group_18} numbers in group 1')
print(f'There are {group_19} numbers in group 1')
print(f'There are {group_20} numbers in group 1')
print(f'There are {group_21} numbers in group 1')
