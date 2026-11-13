# print("new journey begins")
# #my name is jatin this is a single line comment
# """""this is a multiline comment also known as dockstring enclosed in 3 column """
# variable=21 #this is a variable which can store different values ,variables has some conditions like 
# #it cannot start with a number ,we cannot use space inbetween or in the beginning
# # it cannot have special character except _

# jat_in7=69
# """""NAMING CONVENTIONS OF VARIABLE ARE OF 3 TYPE"""
# JatinBhandari=69 #pascal case
# jatinBhandari=69 #camel case
# jatin_bhandri=69 #snake case
# a = 3 #it is an integer like"-2,-1,0,1,2 and so on
# print(type(a))
# b=12/3 #it is of flot datatype though it will give integer value as any number written in form of p/q is
# c=8.2#it is also float
# print(type(c))
# d=7j #it is a complex same as iota(i) in maths but here we use 'j'
 #print(type(d))
# st="a[ijpk;'jv]"#anything on the keyobard eclosed in ''or"" can be called string
# B=True 
# BL=False #these two are boolean datatype
# print(type(B))
# al="A"
# print(ord(al))#ord function is used to print  the ascy value
# al=65
# print(chr(al))
# """""INDEXING
# POSITIVE INDEXING:- JATIN 
#                     01234
# NEGATIVE INDEXING:- J A T I N
#                    -5-4-3-2-1"""
# a="JATIN"
# print(a[1])
# print(a[-4])
# """"SLICING IN PYTHON
# EG JATIN BHANDARI WE WANT ONLY JATIN THEN WE USE SLICIE USING [START:STOP:STEPS]"""
#n="JATIN BHANDARI"
# print(n[0:5:1])#note for end point we have to use n+1 index as it will print till n-1 index
# #note blank space aslo has an index 
# """""if we dont add a number in the start or stop part then it will auto consider it from 0
#  or till end respectively"""""
#  print(n[ : : 1])
#print(n[0:5:2])#ye steps 2 krne wala paart aadi ne sikhaya tha
# """""TYPE CONVERSIONCONVERION OF ONE DATATYPE TO ANOTHER"""
# a=3
# a=str(a)
# print(type(a))
# #note 
# b="jatin"
# b=int(b)
# print(b)"""here there will be no output as it is a common sense that a word can't be converted into a string
# but anything on the keyboard can be converted into string"""
# c="12"
# c=int(c)
# print(type(c))
# d="jatin"
# d=bool(d)
# print(type(d))
# m="jatin"
# print(bool(m))#it will print true 
#n=0
#print(bool(n))#it will print false
#there are 7 values which will give output false other all will give true
#those values are 0 0.0 "" () [] {}
#f=12
#print(f/3)#it will give answer 4.0(float)altohugh f is integer because it is iplicit type conversion
#"FORMATTED STRING"
#eg 
#n = "Jatin bhandari"
#ag = "19"
#print("my name is",n,"my age is",ag)#it is very boring to apply"" all the time so we use formatted string
#name="jatin" 
#age=19
#print(f"my name is {name} and my age is {age}")#in this we have to use "" only once
#ab user se input lena seekhte hai
#age=input("hello what is your age ")
#print(age)#note here age is used as string 
#age=int (input("hello what is your age"))
#print(age)#now here th.
# e input can only be int
#arithmetic operators
#a=3
#b=2
#print(a+b)
#print(a-b)
#print(a/b)
#print(a//b)#IT IS FLOOR DIVISION ANSWER IS 1
#rint(a**b)#output is 3^2
#print(a%b)#it gives remainder
#python folow bodmas
#compoound assignment operators
#+=,/=,*=,//=,**=,%=,-=
# a=20
# a+=40
#a+=60
#print(a) #answer is 120 
#a+=20  == a=a+20
#comparison operators
#>,<,=,!=,>=,<= #these all give boolean output
# print(ord("A")) #65
# print(ord("B"))#66
# print("A">"B")#false
# print("ABC">"DEF")"""""IT WILL FIRST COMPARE ASCY VALUE OF A AND D hence the value of d is greater it 
# gave value false"""""
# print("ABC">"AFD")"HERE IT WILL FIRST COMPARE A AND A HENCE THEY ARE SAME THEN IT WILL "
# "COMPARE B AND F HNCE ASKY VALUE OF F IS GREATER IT GIVES OUTPUT FALSE"
# you cann't compare an integer with a string
# "logical operators"
#and operation# #all the statements should be true 
#print(48>31 and 55==55 and 68<99)#true 
#print(48<31 and 55==55 and 68<99)#false
#or operator#any one statement should be true
#print(12!=12 or 25==67 or 10>5)#true
#not operator#it turn true into false and false into true
#
# +print(not 12==12)
# "Answer True and False"
# print(126 > 130)#false 
# print((456 == 456) != (235 == 236))#true
# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)#true
# print(True and bool(0))#false
#"if else elif"
# a=int(input("a number"))
# if a<10:
#     print("hello")
     
# elif a>=10 & a<=20 :
#     print("tum chutiya ho")

# else:
#     print("not hello")
# Q1 Accept two numbers and print the greatest bw them
# a=int(input("enter a number"))
# b=int(input("enter another number"))
# if a>b:
#     print("a is greatest")

# elif b>a:
#     print("b is gretest")

# else :
#     print("haha lol")
#Q2 ACCEPT THE GENDER FROM THE USER AS CHAR AND PRINT THE RESPECTIVE MESSAGE
#GOOD MORNING SIR (MALE), GOOD MORNING MAM ( FEMALE)
# char=input("enter a gender")
# if char== "male" :
#     print("good  morning sir")
# elif char== "female":
#     print("good morning madam")
# else:
#     print("rather not say")
#write a programe to chec whether the number is an even number or not
# num =int(input("please enter a number"))
# if num%2==0:
#     print("number is even")
# else :
#     print("number is odd")
#Q accept a year
#  to check whether a number is a leap year or not 
# year = int(input("tell your year :- "))

# if year % 100 == 0 and year % 400 == 0:
#     print("Its a leap year")
# elif year % 100 != 0 and year % 4 == 0:
#     print("Its a leap year")
# else:
#     print("its a normal year")
# t = int(input("please tell the temprature :- "))

# if t < 0:
#     print("Freezing cold")
# elif t >= 0 and t < 10:
#     print("very cold")
# elif t >= 10 and t < 20:
#     print("cold")
# elif t >= 20 and t < 30:
#     print("plesant")
#LOOPS:- FOR LOOP AND WHILE LOOP
#FOR LOOP
# range(start,stop,step) for stop, numbers will print from start to n-1
#default( 0   ,    , 1  ) stop don't have a default ,you must have to decide a value
#eg
# a=range(0,20,1)
# for i in a:
#     print(i)
#the above program can also be written as
# for i in range(0,20,1):
#     print(i)
#the above you can usw for positive increment for eg 1  to 100 or 16 to 500
#but now we have to do negative decrement for eg 60 to 1 for that we set steps with negative sign
#eg 
# for i in range(16,1,-1):
#     print(i)
#Q PRINT TABLE OF 5
# for i in range(5,51,5):
#     print(i)
#q write a general programm to print any table
# n=int(input("type a number"))
# for i in range(n,(n*10)+1,n):
#     print(i)
#for loop in string
# a= "JATIN BHANDARI"
# for i in range(0,14,1):
#     print(a[i])
#how to find lenght of string
# a="my name is jatin bhandari"
# print(len(a))
#note lenght start from 1 not from 0
# a="my name is jatin bhandari i study at graphic era deemd to be university "
# for i in range(0,len(a),1):
#     print(a[i])
#DIRECT ITERATIONS
# a="i am very cool"
# for i in a:
#     print(i)
#BREAK CONTINUE ELSE STATEMENT
# for i in range(0,20,1):
#     if i==15:
#         break
#     else:
# print(i)#it will print till 14 onlyprint(i)#it will print till 14 only
# for i in range(0,20,1):
#     if i==15:
#         break
#     print(i) #this will also give the same output else statemt is not necessary
# for i in range(1,20,1):
#     if i==15:
#         continue
#     print(i)# all number will print except 15
# for i in range(0,21,1):
#     if i==15:
#         print("break statement is executed")
#         break
# else:
#     print("break statement is not executed")
#output is break statement is executed
# for i in range(0,21,1):
#     if i==25:
#         print("break statement is executed")
#         break
# else:
#     print("break statement is not executed")
    #OUTPUT IS BREAK STATEMENT IS NOT EXECUTED
    #simple concept agr break run kia o else nhi krega ,agr else run kia to break mhi krega
    #QUESTION PRACTICE FOR FOR LOOP
#Q1 ACCEPT AN INTEGER AND PRINT HELLO WORLD N TIMES
# a=int(input("enter a number"))
# for i in range(0,a,1):
#     print("hello world")
#Q write a program to inpu a number and print a proper table
# a=int(input("enter a number"))
# for i in range(1,11,1):
#     print(f"{a}*{i}={a*i}")
# NOTE HER ABOVE WE HAVE USED FORMATTED STRING WHICH ALLOW US TO USE VARIABLE INSIDE A NORMAL STRING
#q write a programme to print the sum of n terms
# n=int(input("enter a number"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+i   
# print(f"your sum is {sum}")
#write a program to calculate factorial of a number
# n=int(input("enter a number"))
# fact=1
# for i in range(n,1,-1):
#       fact=fact*i  
# print(f"your sum is {fact}")
# write a program to print the sum of even number and odd number seperatly in a range
# n=int(input("enter a mumber "))
# sume=0 
# sumo=0
# for i in range (n):
#     if i%2==0:
#         sume=sume+i

#     else:
#         sumo=sumo+i  

# print(f"sum of even number is {sume},{sumo}")
#q write a program to print all the factor of a number
# n=int(input("enter a number"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
#Q WRITE A PROgram to check whether the number is a perfect number of not
# n=int(input("enter a number"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum=sum+i
# if sum==n:
#     print("yes the number is a perfect number")
# else:
#     print("no not a perfect number")
#Q check whether the number is prime of not
# a=int(input("a number"))
# sum=0
# for i in range(1,a+1):
#     if a%i==0:
#         count=count+1
# if count==2:
#     print("yes it is prime") 
# else:
#     print("no not prime")          
# check whether the string is palindrome or not
# a=input("enter a string")
# b=""
# for i in range(len(a)-1,-1,-1):
#     b=b+a[i]
# if b==a:
#     print("yes the string is palindrome")
# else:
#     print("not a palindrome")

# a = input("enter a string")
# b = ""

# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]
# if b == a:
#     print("yes the string is palindrome")
# else:
#     print("not a palindrome")
#write a program to calculate the number of string intgeger and special characters
# a=input("please enter a random string")
# char=0
# digi=0
# spchar=0
# for i in a:
#     if i.isalpha():
#         char+=1
#     elif i.isdigit():
#         digi+=1
#     else:
#         spchar+=1    
# print(f"your digits are{digi}\n your alphabets are{char}\n your special character are {spchar}")
# print(dir(str))
# """WHILE LOOP"""
# a=int(input("please enter your integer"))
# while a>0 :
#     print(a%10)
#     a=a//10
#write a program to print reverse of a number
# a=int(input("please enter your integer"))
# rev=0
# while a>0 :
#      rev=rev*10+a%10
#      a=a//10
# print(rev)
#write a program to check whether it is a palindrome or not
# a=int(input("please enter your integer"))
# rev=0
# copy =a #copy variable
# while a>0 :
#       rev=rev*10+a%10
#       a=a//10

# if copy==rev:
#       print("yes it is palindrome")
# else:
#       print("not a palindrome")
# #build a random guessing game import random 
# num=random.randint(1,10)
# print(num)
# tries=0
# while true:
# guess=int(input("please enter a number"))
# if guess==num:
#      tries+=1
#      print("you won")
# else:
#      print("you loose")
"""FUNCTIONS"""
# def sum(a,b):
#     print(f"the sum of 2 number is{a+b} ")

# sum(45,54)
# def hello(name,age):
#     print(f'your name is {name} your age is {age}')
# hello(age=18,name="jatin")
# def sum(a,b=69):
#     print(f"the sum of a+b is {a+b}")
# sum(78)
# def palindrome(st):
#     rev=""
#     for i in range(len(st)-1,-1,-1):
#         rev=rev+st[i]
#     if rev==st:
#         print("yes palindrome")    
#     else:
#         print( "not a palindrome")

# palindrome("aaditya" )
"""data structures"""
"""list"""
# a=[1,"jatin",print()]#kuch bhi store kr lo
# print(a[2])
#loop in list
#method 1 : using index values
# a=["A",1,2,4,]
# for i in range(len(a)):
#     print(a[i])
#method 2 directly on values
# a=["A",1,2,4,]
# for i in a :
#     print(i)
#append :-it is to add a new entry in the list to the end
# l=[1,2,"a"]
# l.append("jatin")
# print(l)
#insert :- it is used to ADD a new entry in the list in between at any index
# .insert(index no,new entry)
# l=[0,1,2,4,5,6]
# l.insert(3,3)
# print(l)
#remove:-it is used to remove a entry in a list but the first occurance will only be remved
# l=[1,2,3,4,5,2,6,2,2]
# l.remove(2)
# print(l)
#you can also change any element at any index
# l=[1,2,3,4,5,2,6,2,2]
# l[0]=10
# print(l)
# l=[1,2,3,4,5,2,6,2]
# # pop print(l.pop())#it ia used to remove and store the element at an index (by default the last index if not given)
#l=[1,2,3,4,5,2,6,2,]
# # count print(l.count(2))#count the occurance of an element 
# l=[1,2,3,4,5,6,22,11,37,19,36,17]
##sort l.sort()
# print(l)
# l=[1,2,3,4,5,6,22,11,37,19,36,17]
# # reverse l.reverse()#reverse the  order of string
# print(l)
# l=[1,2,3,4,5,6,22,11,37,19,36,17]
# # clearl.clear()#it is used to clear all the element in a list
# print(l)
#Q write a program to print all the positive and negative elemeent of a list
# l=[1,2,-5,-6,-7,8,9]
# print("positive elements are")
# for i in l:
#     if i>=0:
#         print(i)
# print("NEGATIVE ELEMENTS ARE ")
# for i in l:
#     if i<0:
#         print(i)
#q Q write a program to find the mean of the list
# l=[1,2,3,4,5,6,22,11,37,19,36,17]
# sum=0
# for i in l:
#     sum+=i
# mean=sum/len(l)
# print(mean)
#Q write a program to print the largest number of the list
# l=[1,2,3,4,5,6,22,11,37,19,36,17]
# largest=l[0]
# index=0
# for i in range(len(l)):
#     if l[i]>largest:
#          largest=l[i]
#          index=i
# print(f"the largest number is {largest} with index {index} ")   
# write a program to print the second largest number of a listt
# l=[1,2,3,4,5,6,22,11,37,19,36,17]
# largest=l[0]
# secondlargest=l[0]
# for i in l:
#     if i>largest:
#         secondlargest=largest
#         largest=i
#     elif i>secondlargest:
#         secondlargest=i
# print(f"Second largest number is {secondlargest}")
# a = [12,13,15,16]
# for i in range(len(a)-1):
#      if a[i] < a[i+1]:
#          continue
#      else:
#          print("your list is not sorted")
#          break
# else:
#     print("your list is sorted")
"""""deep copy"""""
# a=[1,2,3,4,5]
# b=a
# b[0]=10
# print(a) note though you made change in b only but it affected a also this is called deep copy
"""shallow copy"""
# a=[1,2,3,4,5]
# b=a.copy()
# b[0]=10
# print(a)#now it will not affect a and this is called shallow copy


"""""tuple"""""
#IT IS JUST LIKE LIST BUT IMUTABLE
#THERE ARE ONLY 2 METHODS
# a=(1,2,3,5,5,5,9,9,8)
# index=a.index(5)
# print(index)#it will print the tindex of first of occurance of 5
# a=(1,2,3,5,5,5,9,9,8)
# count=a.count(5)
# print(count)#will print the occurance of 5
"""sets"""
#you cannot have duplicate items in a set
#you cannot access elemen of set using index value
#it cannot store everything
# a,b,c={1,2,3}
# print(b)#output will be 2 , this is called unpacking of string
# b=hash("jatin")
# print(b)
# a={1,5,9,11,3,4}
# print(a)#IT WILLL AAUTOMATICALLLY BE IN ASCENDING ORDER
#you cannt use "for i in range"you can only use for i in a because set does not have index values
# a={1,5,9,11,3,4}
# for i in a:
#     print(i)
#jee wala set in python
# a={1,3,4,9,6,7,8}
# b={1,5,11,13,9,6,8}
# c=a.union(b)
# print(c)
# #if you dont want to type union you can use shortcut
# a={1,3,4,9,6,7,8}
# b={1,5,11,13,9,6,8}
# c=a|b
# print(c)
# a={1,3,4,9,6,7,8}
# b={1,5,11,13,9,6,8}
# c=a.intersection(b)
# print(c)
# a={1,3,4,9,6,7,8}
# b={1,5,11,13,9,6,8}
# c=a&(b)
# print(c)
# a={1,3,4,9,6,7,8}
# b={1,5,11,13,9,6,8}
# c=a.difference(b)
# print(c)
# a={1,3,4,9,6,7,8}
# b={1,5,11,13,9,6,8}
# c=b.difference(a)
# print(c)
# a={1,3,4,9,6,7,8}
# b={1,5,11,13,9,6,8}
# c=a-b
# print(c)
# a={1,3,4,9,6,7,8}
# b={1,5,11,13,9,6,8}
# c=a.symmetric_difference(b)#uncommon elements ko print krna
# print(c)
# a={1,3,4,9,6,7,8}
# b={1,5,11,13,9,6,8}
# c=a^b
# print(c)
"""dictionaries"""
# d={10:100,20:200,30:300}
# print(d[20])
# d={10:100,20:200,30:300}
# d[10]=6969
# print(d)
# d={10:100,20:200,30:300}
# for i in d:
#     print(i)
# d={10:100,20:200,30:300}
# for i in d:
#     print(d[i])
# d={10:100,20:200,30:300}
# for i in d.values():
#     print(i)
# # help(dict)
# d={10:100,20:200,30:300}
# d.update({50:500})#creating method 1
#  print(d)
# d={10:100,20:200,30:300}
# for i in d.values():
#      print(i)
# d={10:100,20:200,30:300}
# d[50]=500#creating method 2
# print(d)
# d={10:100,20:200,30:300}
# del d[30]#deleting
# print(d)
# help(dict)
# d={10:100,20:200,30:300}
# d1=d.copy()
# d1[10]=69
# print(d)
# print(d1)
# d={10:100,20:200,30:300}
# d1=d.get(20)
# print(d1)
# d={10:100,20:200,30:300}
# print(d.items())
#write a python program to merge 2 pyhton dictionaries
# d1={10:100,20:200,30:300}
# d2={40:400,50:500,60:600}
# for i in d2:
#     d1[i]=d2[i]
# print(d1)
#write a python program to print the sum of elements of a dictionary
# d1={10:100,20:200,30:300}
# sum=0
# for i in d1:
#     sum=sum+d1[i]
# print(sum)
#write a python program to find the frequency of eACH ELEMENT in a list
# a=[1,1,1,1,2,2,2,2,3,3,3,4,4,4,5,5,5,]
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
# def update(values):
#  result = []
#  for x in values:
#       if x % 3 == 0:
#           result.append(x // 3)
#       elif x % 2 == 0:
#            result.append(x + 4)
#       else:
#            result.append(x - 1)
#  return result
# numbers = [7, 12, 5, 8, 15]
# print(update(numbers))


# def analyse(text):
#     vowels = 0
#     consonants = 0

#     for ch in text:
#         if ch in "AEIOU":
#             vowels += 1
#         elif ch.isalpha()  and ch.islower() and ch not in "aeiou":
#             consonants += 1

#     return vowels, consonants


# print(analyse("Python Is FUN"))
# def process_list(numbers):
   # result = []

#     for x in numbers:
#         if x < 0:
#             result.append(-x)
#         elif x == 0:
#             result.append(0)
#         elif x % 2 == 0:
#             result.append(x // 2)
#         else:
#             result.append(x * 3)

#     return result


# # Test 1
# numbers1 = [-4, 0, 8, 5, -7]
# print("Input:", numbers1)
# print("Result:", process_list(numbers1))



# a = [12,13,18,15,16]
# flag = 0 
# for i in range(len(a)-1):
#      if a[i] >a[i+1]:
#          flag = 1 

# if(flag ==1) : print("unsorted")
# else :print("sorted")
# username = input("Enter username: ")

# valid = True

# # Check length
# if len(username) < 6 or len(username) > 10:
#     valid = False

# # Check first character is a letter
# elif not username[0].isalpha():
#     valid = False

# # Check for digit and spaces
# has_digit = False

# for ch in username:
#     if ch.isdigit():
#         has_digit = True
#     if ch == " ":
#         valid = False

# # Check at least one digit
# if not has_digit:
#     valid = False

# if valid:
#     print("Valid username")
# else:
#     print("Invalid username")
# num=5678
# a= (num / 10) % 1000
# print(a)
#Write a Python program to swap two variables without a temp variable
# Initialize variables
# a = 10
# b = 20
# a, b = b, a
# print(f"a = {a}")
# print(f"b = {b}")
# c=0
# a=input("enter a number")
# while c<= len(a):
#     c+=1
# print(c)
# • Write a program to count the total number of digits in a number
# using a while loop.
# • For example, the number is 75869, so the output should be 5.

# c = 0
# a = int(input("enter a number"))
#   # Handles negative numbers

# if a == 0:
#     c = 1
# else:
#     while a > 0:
#         a = a // 10
#         c += 1

# print(c)
#mwthod 2
# num = input("Enter a number: ")

# count = 0
# for a in num:
#     if a.isdigit():  # Ensures negative sign ('-') is not counted
#         count += 1

# print(f"Total number of digits: {count}")
# Write a program to find the sum of the digits of a given number
# For example: if a user enters 123
# Sum of digits is 6 (1+2+3)
# num = input("Enter a number: ")

# sum_of_digits = 0

# for a in num:
#     if a.isdigit():        # Ignore negative sign '-' or non-digit characters
#         sum_of_digits += int(a)

# print(f"Sum of digits is: {sum_of_digits}")
# Write a program to display the reverse of the number
# For example:
# INPUT: 12345
# OUTPUT: 54321

# num = input("Enter a number: ")

# reversed_num = ""

# # Loop backwards using range(start, stop, step)
# for i in range(len(num) - 1, -1, -1):
#     reversed_num += num[i]

# print(f"Reversed number: {reversed_num}")


# Write a program to print the factorial of a number
# For example:
# INPUT: 6
# OUTPUT: 720
# Program to calculate factorial using a for loop
# num = int(input("Enter a number: "))

# factorial = 1


# for i in range(1, num + 1):
#     factorial = factorial * i

# print(f"The factorial of {num} is {factorial}")


# Write a program to check whether the number entered is an Armstrong
# number or not
# For example:
# 153 = 13+53+33
#  =1+125+27
# = 153
# Program to check Armstrong number using a for loop
# num = int(input("Enter a number: "))

# # Convert to string to count total digits and iterate through each digit
# num_str = str(num)
# power = len(num_str)

# armstrong_sum = 0

# # Loop through each digit character
# for digit in num_str:
#     armstrong_sum += int(digit) ** power

# # Check if sum matches original number
# if num == armstrong_sum:
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")
# a=12
# if (a%2==6 and a>10):
#     print("true")
# else :
#     print("false")
# c=input("enter a char")
# if c in "a,e,i,o,u,A,E,I,O,U":
#     print("yes")
# else :
# #     print("no")
# n=int(input("enter a number"))
# for i in range (1,n+1,2):
#     print(i)
# s1=input("enter string s1")
# s2=input("enter string s2")
# for i in s1:
#     if i in s2:
#         count+=1
#         print("yes it can be made")
#     else:
#         print("sorry cant be made")
# d={}
# print(type(d))#DICT
# d={a556,130}
# print,(type(d))#SET
"""exception handling"""
# a=int(input("please enter a number"))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"sorry the was an error{err}")
# print("ok i have done the division")

# a=int(input("please enter a number"))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"sorry the was an error{err}")
# else:
#     print("wow ther was no error")
# a=int(input("please enter a number"))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"sorry the was an error{err}")
# else:
#     print("wow ther was no error")
# finally:
#     print("i will run no matter what")
# age = int(input("tell your age :- "))

# try:
#     if age < 10 or age > 18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")
# except Exception as err:
#     print(f"an error occured as {err}")

# print("the club will start soon")
"""file handling"""
# p=open(r'C:\Users\jatin\OneDrive\Desktop\PYTHON\main.py')
# print(p.read())
# r=open("superman.txt",'w')
# r.write("hello my name is and im learning python")
# r.close()
# r=open("superman.txt",'a')
# r.write("and i m doing my btech from geu")
# r.close()
#refer to new window after this
# """OOPS"""
# class Factory:
#      a=15#IT is a attribute inside class


#      def hello(self):#it became a method inside class
#          print("hello world")

#      print("hello how are you i am getting initialised")


# print(Factory().a)
# print(Factory().helloworld())



# obj=Factory()
# print(obj.a)
# obj.hello()

# class Factory:
#      def __init__(self, material, zips, pockets):
#          self.material = material
#          self.zips = zips

#          self.pockets = pockets
#      def show(self):
#          print(f"your object details are{self.material},{self.zips},{self.pockets}")


# reebok = Factory("leather", 3, 2)

# campus = Factory("nylon", 3, 3)

# print(campus.pockets)
# print(reebok.material)
# reebok.show()


# class Animal:
#     name="lion"#class attribute
#     def __init__(self,age):
#         self.age=age#instance variable
#     def show(self):#instant method
#         print(f"your age is {self.age}")

#     @classmethod
#     def hello(cls):
#         print("how are you brother")


#     @staticmethod
#     def static():
#         print("how are you")

# obj=Animal(12)

# obj.show()

# obj.hello()

# obj.static()

"""inheritance"""
# class Factorymumbai:#PARENT CLASS
#     a="hello i am an attribute mentioned inside a factory"
#     def hello(self):
#         print("hello i am a method present inside this factory")

# class Factorypune(Factorymumbai):#child class
#     pass
    
    
    
    
# obj1=Factorymumbai()
# obj2=Factorypune()

# print(obj2.hello())
"""singlelevel inheritance"""

# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def show(self):
#         print(f"your name is {self.name}")

# class Human(Animal):
#     def __init__(self,name,age):
#         super.__init__(name)#can only store attributed of super class ie "name" hence we have to make a seperate 
#                              #instant variable for age
#         self.age=age
#     def show(self):                                                                                             
#                 print(f"your name is {self.name},{self.age}")#------------------------------------------------------|



# animal1=Animal("lion")
# person1=Human("Jatin")
# person1.show()
# animal1.show()

#all the things in super class can be accessed by sub class but not all the things of sub class can be accessed by super class

"""multiple inheritance"""
# class Animal:
#     def __init__(self,name):
#         pass

# class   Human:
#     def __init__(self,name,age):
#         pass

# class Robot(Animal,Human):
#     pass

# obj=Robot()#will ask for name only as Animal is inherited first



# class Animal:
#     def __init__(self,name):
#         pass

# class   Human:
#     def __init__(self,name,age):
#         pass

# class Robot(Human,Animal):
#     pass

# obj=Robot()#will ask for name age both as Human is inherited first


"""Multilevel inheritance"""

# class Factory:
#     def __init__(self, material, zips):
#         self.material = material
#         self.zips = zips


# class BhopalFactory(Factory):
#     def __init__(self, material, zips, color):
#         super().__init__(material, zips)
#         self.color = color


# class PuneFactory(BhopalFactory):
#     def __init__(self, material, zips, color, pockets):
#         super().__init__(material, zips, color)
#         self.pockets = pockets

# obj=PuneFactory()#it is asking for all ,material zip color pockets


"""polymorphism"""

# def show():
#     print("hello")

# def show():
#     print("jatin")

# print(show())#it will print jatin and not hello as python overrides

# class Animal:
#     def show(self):
#         print("hello")

# class Human(Animal):
#     def show(self):
#         print("jatin")

# obj=Human()
# obj.show()#it will print jatin and not hello as it is an object of human class


# class Animal:
#     def show(self):
#         print("I am showing")

# class Human:
#     def show(self):
#         print("hello I am also showing")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.s
"""encapsulation"""



# class Factory:
#     _a="pune"#note _ means protected in other languages but it python there is no such thing exits it is only for ,if you have to convert
#              #the code to other languange ,then you can use _ to protect  it 

#     def show(self):
#         print("hello i am pune factory")

# class Bhopal(Factory):

#     def show2(self):
#         print(super()._a)

# obj=Bhopal()
# obj.show2()




# class Factory:
#     __a="pune"#double under score means private now this thing cannot be acceswd by other classes or object
             

#     def show(self):
#         print("hello i am pune factory")

# class Bhopal(Factory):

#     def show2(self):
#         print(super().__a)

# obj=Bhopal()
# obj.show2()


"""ABSTRACTION"""

# from abc import ABC, abstractmethod

# class Abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass


#     @abstractmethod
#     def area(self):
#         pass

# class Square(Abstract):
#     def __init__(self,side):
#         self.side=side

# class Circle(Abstract):
#     def __init__(self,radius):
#         self.radius=radius

# obj=Circle(7)#the program will not run as now creation of perimeter and area is compulsary



# from abc import ABC, abstractmethod

# class Abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass


#     @abstractmethod
#     def area(self):
#         pass

# class Square(Abstract):
#     def __init__(self,side):
#         self.side=side


#     def perimeter(self):
#         print("i have created")

#     def area(self):
#         print("yes i have created")



# class Circle(Abstract):
#     def __init__(self,radius):
#         self.radius=radius

        
#     def perimeter(self):
#         print("i have created")

#     def area(self):
#         print("yes i have created")

# obj1=Circle(7)#now it will show no error as we have created area and perimeter
# obj2=Square(10)


"""dunder method"""

# class Animal:
#     def __init__(self, name,age):
#         self.name = name
#         self.age=age

#     def __str__(self):
#         return f"hello how are you and your name is {self.name}"

#     def __add__(self,other):
#         return f"sum of your ages are{self.age + other.age}"

# obj1 = Animal("lion",12)
# obj2= Animal("dolphin",14)

# print(obj1)
# print(obj2)
# print(obj1+obj2)



# class Animal:
#     def __init__(self, name,age):
#         self.name = name
#         self.age=age

#     def __str__(self):
#         return f"hello how are you and your name is {self.name}"

#     def __add__(self,other,other2):
#         return f"sum of your ages are{self.age + other.age+other2.age}"

# obj1 = Animal("lion",12)
# obj2= Animal("dolphin",14)
# obj3=Animal("tiger",16)

# print(obj1)
# print(obj2)
# print(obj1+obj2+obj3)#this will give no output for more than 2 we have to use args and keyargs#



#or we can convert it into tuple





# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"hello how are you and your name is {self.name}"

#     def __add__(self, other):
#         sum = 0
#         for i in other:
#             sum = sum + i.age
        
#         return f"your sum of ages are {self.age + sum}"

# obj = Animal("lion", 12)
# obj2 = Animal("dolphin", 14)
# obj3 = Animal("tiger", 34)

# print(obj + (obj2, obj3))


"""Advance programming"""
"""decorator"""
# class Animal:
#     def show(self):
#         print("hello how are you")

# obj=Animal
# obj.show()#here we have to use bracket



# class Animal:
#     @property
#     def show(self):
#         print("hello how are you")

# obj=Animal
# obj.show  #here we dont have to use bracket



#creating a decorator



# def decorate(func):
#     def wrapper():
#         print("I will print myself before the function hello ")
#         func()
#         print("I will print after the function")
#     return wrapper

# @decorate
# def hello():
#     print("hello I am akarsh vyas ")

# hello()





# def decorate(func):
#     def wrapper(a,b):
#         print("the addition to your numbers are ")
#         func(a,b)
#         print("thankyou I hope you liked it ")
#     return wrapper

# @decorate
# def addition(a, b):
#     print(f"your total is {a + b} ")

# addition(12, 67)


"""args &kwargs"""



# def addition(*args):#this creates a tuple as we dont know how many variabes to creates cuz user can input as my number as he wants
#     sum = 0
#     for i in args:
#         sum = sum + i

#     print(sum)


# addition(12,12,23,56)



# def information(**kwargs):
#     print("your information is\n ")
#     for i in kwargs:
#         print(f"{i} : {kwargs[i]}")

# information(name = "Akarsh", age = 23, designation = "AI/ML")




# def decorate(func):
#     def wrapper(*args,**kwargs):
#         print("the addition to your numbers are ")
#         func(*args,**kwargs)
#         print("thankyou I hope you liked it ")
#     return wrapper

# @decorate
# def addition(a,b,c,d,e):
#     print(f"your total is {a + b + c + d + e} ")

# addition(12,67,79,67,88)



"""list dictionary set comprehensoion"""

#list
l=[i for i in range(1,20) if i%2==0]
print(l)

#dictionary
l={i:i**2    for i in range(1,10)}
print(l)