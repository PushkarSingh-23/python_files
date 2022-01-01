"""in this program we will use various methods which we can perform on strings example
 length = len
 count = count
 upper case = upper
 lower case = lower 
 replace a keyword or char = replace 
 find word or element in string = find
 split string uing key element = split 
 strip method removes white blank spaces from begining and end =  strip ()
 using format we can insert integer values in string = format()
 
"""
import linecache as lc

string = str(input())
print(string)
print(len(string))
print((string).upper())
print(string.upper())
print("enter two elments which you would like to replace with: ")
element1 = str(input())
element2 = str(input())
print(string.replace(element1, element2))
print("enter two elments which you would like to count: ")
count_element = str(input())
print(string.count(count_element))
print("enter two elments which you would like to find in the string: ")
find_element = str(input())
print(string.find(find_element))
print("Enter a char with you would like to split this string: ")
split_element = str(input())
print(string.split("split_element"))
