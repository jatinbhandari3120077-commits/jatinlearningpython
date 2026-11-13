
# 1.Develop a Python program to perform the following operations:
# A.Create an empty list.
# B.Use a loop to append 10 user-input integers to the list.
# C.Remove all numbers from the list that are divisible by 3.
# D.Clear the entire list afterward.


# l=[]
# for i in range(10):
#     m=int(input("please enter something "))
#     l.append(m)   
# print(l)

# for i in l:
#     if i%3==0:
#         l.remove(i)
# print(l)

# l.clear()
# print(l)



# a= [2, 3, 5, 7, 11, 13, 2, 3, 5,2]
# print(a.count(2))
# b=a.copy()
# a.clear()
# print(b)


# 2.Write a Python program to perform the following operations:
# A.Create a list with the elements [2, 3, 5, 7, 11, 13, 2, 3, 5].
# B.Use the count() method to find how many times the number 2 appears in the list.
# C.Make a copy of the list using the copy() method and display the copied list.
# D.Clear the original list and display both the original and copied lists.

# a = [2, 3, 5, 7, 11, 13, 2, 3, 5]
# print("Original List:", a)


# count_2 = a.count(2)
# print("Count of number 2:", count_2)


# b = a.copy()
# print("Copied List:", b)
# a.clear()
# print("Original List after clear():", a)
# print("Copied List (remains safe):", b)




# 3.Write a Python program to perform the following operations:
# A.Create two lists: list1 = ['apple', 'banana', 'cherry'] and list2 = ['orange', 'grape'].
# B.Use the extend() method to add all elements of list2 to list1.
# C.Find the index of 'grape' in the extended list and print it.

# l1 = ['apple', 'banana', 'cherry']
# l2 = ['orange', 'grape']
# l1.extend(l2)
# print(l1)
# b=l1.index('grape')
# print(b)


# 4.Develop a Python program to perform the following operations:
# A.Create a list with elements [10, 20, 30, 40, 50].
# B.Use the insert() method to add the number 25 at the third position.
# C.Use the pop() method to remove the last element from the list and print the removed element.
# Display the final state of the list


# l=[10, 20, 30, 40, 50]
# l.insert(3,25)
# print(l)

# print(l.pop())
# print(l)


# 5.Write a Python program to perform the following operations:
# A.Create a list of random numbers [12, 7, 19, 4, 15, 2].
# B.Use the sort() method to sort the list in ascending order and display it.
# C.Use the reverse() method to reverse the order of the sorted list and display the reversed list.

# l=[12, 7, 19, 4, 15, 2]
# l.sort()
# print(l)
# l.reverse()
# print(l)

# 6.Develop a Python program to perform the following operations:
# A.Create an empty list and use a loop to append 5 random numbers between 1 and 50.
# B.Use count() to display the frequency of each unique number in the list.
# C.Use index() to find the position of the largest number in the list.
# D.Use remove() to delete the smallest number from the list.
# E.Make a copy of the modified list and display both lists.

# import random


# a = []

# for i in range(5):
#     a.append(random.randint(1, 50))

# print("Original List:", a)


# for i in a:
#     print(i, "comes", a.count(i), "times")


# maximum = max(a)
# print("Maximum number:", maximum)
# print("Position:", a.index(maximum))


# smallest = min(a)
# a.remove(smallest)

# print("After removing smallest:", a)


# b = a.copy()

# print("Original List:", a)
# print("Copied List:", b)




# import random


# a = []

# for i in range(5):
#     a.append(random.randint(1, 50))

# print("Original List:", a)

# for i in a:
#     print(i, "comes", a.count(i), "times")

# largest=a[0]
# index=0
# for i in range(len(a)):
#     if a[i]>largest:
#          largest=a[i]
#          index=i
# print(f"the largest number is {largest} with index {index} ")   
    

# smallest=a[0]
# index=0
# for i in range(len(a)):
#     if a[i]<smallest:
#          smallest=a[i]
#          index=i
# print(f"the smallest number is {smallest} with index {index} ")  


# a.remove(smallest)

# print("After removing smallest:", a)


# b = a.copy()

# print("Original List:", a)
# print("Copied List:", b)




# 7.Write a Python program to perform the following operations:
# A.Create a list of strings names = ["John", "Antony", "Bob", "Antony", "David"].
# B.Use the count() method to find out how many times "Alice" appears in the list.
# C.Use the remove() method to delete the first occurrence of "Antony".
# D.Use the insert() method to add "Antony" back at the index position where it was removed.
# E.Print the final state of the list.


# l= ["John", "Antony", "Bob", "Antony", "David"]
# print(l.count("Antony"))
# l.remove("Antony")
# print(l)

# l.insert(1,"Antony")
# print(l)





# 9.Develop a Python program to perform the following operations:
# A.Create a list with elements [9, 1, 8, 2, 7, 3, 6, 4, 5].
# B.Use sort() to sort the list in ascending order.
# C.Use reverse() to reverse the sorted list.
# D.Use pop() to remove the element at index 4 and display it.
# E.Use insert() to insert the popped element at the start of the list and display the final list.



# l= [9, 1, 8, 2, 7, 3, 6, 4, 5]
# l.sort()
# print(l)
# l.reverse()
# print(l)
# a=l.pop(4)
# print(a)
# l.insert(0,a)
# print(l)


# l=[]
# for i in range(5):
#     a=input("please enter 5 names ")
#     l.append(a)

# print(l)

# l.sort()
# print(l)
# l.append("aaditya")
# l.append("aaanat")
# print(l)
# l.pop(1)
# print(l)



# 11. Consider a list, list1 = ['abc', 123, 'ab12', '456', 'xyz', '78xy']. Write a Python program to remove all alphanumeric strings 
# (strings containing both letters and numbers) from the list.




# l = ['abc', 123, 'ab12', '456', 'xyz', '78xy']
# result = []  

# for i in l:
#     # 
#     if type(i) == str:
#         has_letter = False
#         has_digit = False
        
#         # String ke ek-ek character ko check karo
#         for char in i:
#             if char.isalpha():      # Agar character letter hai
#                 has_letter = True
#             if char.isdigit():      # Agar character number hai
#                 has_digit = True
        
#         # Agar letter aur number DONO hain, toh isko skip kar do
#         if has_letter and has_digit:
#             continue
            
#     # Baaki sabhi items ko nayi list mein add kar lo
#     result.append(i)

# print(result)



# 12.Given a list, list2 = ['10', 'apple', '20', 'banana', '30', 'grape'], write a Python program to remove all numeric strings 
# (strings that consist only of digits) from the list and display the resulting list.


# list2 = ['10', 'apple', '20', 'banana', '30', 'grape']
# result = []  # Ek khali list jismein non-numeric strings rakhenge

# for item in list2:
#     item.isdigit() check karta hai ki kya string sirf numbers se bani hai
#     'not item.isdigit()' ka matlab hai ki agar woh sirf numbers nahi hain, toh rakh lo
#     if not item.isdigit():
#         result.append(item)

# print(result)





# 13.Write a Python program to keep only the integer values from the list list3 = [10, 'text', 25.5, 30, 'hello', 45] and remove all other types.
# l= [10, 'text', 25.5, 30, 'hello', 45] 
# result=[]
# for i in l:
#     if  not type(i)==str:
#         result.append(i)
# print(result)
# 14.Given a list, list4 = [1, 2, 3, 4, 2, 5, 3, 6, 7, 1], write a Python program to remove all duplicate elements, 
# keeping only the first occurrence of each number.
# l= [1, 2, 3, 4, 2, 5, 3, 6, 7, 1]
# for i in l:
#     if l.count(i)>1:
#         l.remove(i)

# print(l)



# 15.Consider a list, list5 = ['apple', 'dog', 'elephant', 'cat', 'giraffe']. Write a Python program to remove 
# all elements whose length is less than or equal to 3.

# l= ['apple', 'dog', 'elephant', 'cat', 'giraffe']
# result=[]
# for i in l:
#     if len(i)>3:
#         result.append(i)

# print(result)


# 16.Given a list, list6 = ['Python', 100, 'JavaScript', 3.14, 'Java', 42], write a Python program to remove all non-string elements from the list.

# l = ['Python', 100, 'JavaScript', 3.14, 'Java', 42]
# result=[]
# for i in l:

#     if type(i)==str:
#         result.append(i)

# print(result)


# 17.Write a Python program to remove all negative numbers from a list, list7 = [10, -5, 23, -42, 17, -8, 7], and display the updated list.

# l = [10, -5, 23, -42, 17, -8, 7]

# result=[]
# for i in l:
#     if i>0:
#         result.append(i)

# print(result)

# 18.Consider a list, list8 = ['Monday', 'Tuesday', 'Holiday', 'Wednesday', 'Holiday']. Write a Python program to replace all 
# occurrences of the word 'Holiday' with 'Thursday'.


# l = ['Monday', 'Tuesday', 'Holiday', 'Wednesday', 'Holiday']
# result = []

# for i in l:
#     if i == "Holiday":
#         continue
#     result.append(i)

# print(result)



# 19.Given a list, list9 = ['basketball', 'baseball', 'cricket', 'ball', 'football'], write a Python program to remove all 
# elements containing the substring 'ball'.

# l = ['basketball', 'baseball', 'cricket', 'ball', 'football']
# result=[]
# for i in l:
#     if "ball" not in i:
#         result.append(i)


# print(result)

# 20.Given two lists, list11 = [1, 2, 3] and list12 = [4, 5, 6], write a Python program to create a new list that contains 
# all elements from both lists without duplicates.

# list11 = [1, 2, 3]
# list12 = [4, 5, 6]

# # Combine both lists, convert to a set to remove duplicates, and convert back to a list
# combined_list = list(set(list11 + list12))

# print(combined_list)



# 21.Write a Python program that takes a list, list13 = [10, 20, 30, 40, 50, 60], and removes elements at every even index (0, 2, 4, etc.).

# l = [10, 20, 30, 40, 50, 60]
# result=[]
# for i in range(len(l)):
#     if not i%2==0:
#         result.append(l[i])

# print(result)



l = ['apple', 'banana', 'cherry', 'apple', 'cherry', 'apple']
print(l.count('apple'))
result=[]
for i in l:
    if i =='apple':
        continue

    result.append(i)

print(result)