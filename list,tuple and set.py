tuple1 = ("harry",12,1,4.5)
print(tuple1[0:3])
print(tuple1[3:4])  
list1 = ["a",1,1.2,4,"avast"]
print(list1[0:2])
list1.append([2,"west",1.2,3])
print(list1)

#list and tuple nesting

t1 = ("harry",90,45)
t2 = (2.3,3,4,t1)
print(t2[3])

#sets in python

set1 = {12,23,34,45,56,67,78,89,90,100}
set1.add(2.3)
print(set1)
set1.remove(100)
print(set1)
set2 = {12,5,6,7,8,9,10}
set3 = set1 & set2
print(set3)

set4 = set1.union(set2)
print(set4) 
