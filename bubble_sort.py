list = [2,3,6,6,5]
up_value = int(input)
for i in list:
    max_value = max(list) 
    if i == max_value:
        list.pop(i)
    else:
        print(up_value)  
