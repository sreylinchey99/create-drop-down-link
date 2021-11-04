# Marge
num_of_list = [9, 8, 7, 6, 5]
num_of_list.extend([4, 3, 2, 1])  # to marge one list into another list
num_of_list.append(0)  # to append one element into the list
print(num_of_list)

# Slice
num = [1, 2, 3, 4, 5, 6]
print("Last element of the list is:", num[-1])
print("First element of the list is:", num[0])
print("Two first elements of list are:", num[:2])
print("elements from index 2 until index 5 are:", num[2:5])
print("All element are:", num[:])
print("The element next to the last position is:", num[-2])

# Loop
array_of_num = [10, 20, 30, 40, 50, 60]
for i in array_of_num:
    print(i)  # it will be print all the element of the array one by one

