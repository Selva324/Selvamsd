#dictionary
dic={'name':'selva' ,id : 777}
print (dic)
print (type(dic))
#replace
dic['name']='dhoni'
print(dic)
#update
dic.update({'degree':'bca','role':'director'})
print(dic)
#length


#set operators
s1={56,72,92,88,96}
s2={100,102,104,106,108}
print(s1.union(s2))

print(s1|s2)
print(s1.intersection(s2))
print(s1&s2)
print(s1.difference(s2))
print(s1-s2)
print(s1.symmetric_difference(s2))
print(s1^s2)
#subset
print(s1.issubset(s2))
print(s2.issubset(s1))
print(s1.issuperset(s2))
print(s2.issuperset(s1))
print(s1.issubset(s2))
print(s2.isdisjoint(s1))
print(s1.isdisjoint(s2))
#tuple
x=(1,2,3,4,5,6)
y=list(x)
print(list(x))
print(y)
print(tuple(y))


tv=(88,45,23,87,89,90)
print(tv)
print(type(tv))

t1=tv+(40,55,80)
print(t1)

#tv[0]=100
print(len(t1))
print(tv.count(23,))
print(sum(tv))









      




      
