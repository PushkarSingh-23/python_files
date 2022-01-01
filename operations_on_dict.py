'''' it iis a unordered collection data set with no multiple elements
and is represented by curly brackets {} and we can perform various operations on the
 such as append , remove  and the data will stored randomly in the dictonory
 and there will be no indexing of data in the dictonory'''
 
dictonary = {"hello" : 1, "world" : 2, "This":3 , "is":4 , "PUSHKAR":5 ,"Singh":6}
print(dictonary)
print(dictonary.keys())
print(dictonary.values())
print(dictonary.get("PUSHKAR"))
x = dictonary.items()
print(x)
if "Singh" in dictonary:
    print("Yes it is in the dictonory")
else:
    print("No it is not in the dictonory")
dictonary.pop("PUSHKAR")
dictonary.update({"pushkar":1})
print(dictonary)
dictonary["pushkar"] = 3
print(dictonary)
dictonary.pop("hello")
print(dictonary)
dictonary.clear()
print(dictonary)