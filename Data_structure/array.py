# #method number one
# import array as arr
# num = arr.array("i",[1,2,3,4,5])
# num.append(6)
# print(num)

# #Method number two
# import array
# container = array.array("i",[1,2,3,4,5]) 
# container.pop(-1)
# container[-1] = 12
# print(container)  

# # Method number three
# from array import*
# arr_of_num = array("i",[1,3,5,7,9])
# new_array = len(arr_of_num)
# print("Index of array is:", new_array)

# import array as arr
# numbers_list = [10,20,30,40,50,60] 
# numbers_array = arr.array('i', numbers_list) 
# print(numbers_array[2:5]) 		
# print(numbers_array[:-5]) 		
# print(numbers_array[5:]) 		
# print(numbers_array[:]) 	


# import array as arr 
# numbers_list = [2, 5, 62, 5, 42, 52, 48, 5] 
# numbers_array = arr.array('i', numbers_list) 
# print(numbers_array[2:5])     # 3rd to 5th 
# print(numbers_array[:-5])     # beginning to 4th 
# print(numbers_array[5:])     # 6th to end 
# print(numbers_array[:])     # beginning to end

# number = arr.array('i', [1, 2, 3, 3, 4]) 
# print("index of the array is:",len(number))
# for i in number:
#     print(i)


# First method to create a 1 D array
from array import array


N = 5
arr = [0]*N
print(arr)
# Second method to create a 1 D array
N = 5
arr = [0 for i in range(N)]
print(arr)

#Method 1
# 2D array
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr)

 #Method2
# 2D array
rows, cols = (5, 5)
arr = [[0 for i in range(cols)] for j in range(rows)]
print(arr)