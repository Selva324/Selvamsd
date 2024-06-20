'''#list
s=[10,20,30]
print('list of:',s )
print(type(s))
s.append(40)
print(s)
print(s[1])
x=(10+20)
print(x)
print(len(s))

#sets
s1={10,20,30,40}
s2={10,20,30,40,50,60}
print(s1.union(s2))
print(s1|s2)
print(s1.intersection(s2))
s1.add(70)
print(s1)
#dictionary
dic={'name':'selva','age':'27','grade':'a'}
print(dic)

dic.update({'grade':'b'})
print(dic)
dic['subject']='maths'
print(dic)

#string
s="Full stock development"
print(len(s))
print(s.upper())
print(s.lower())
print(s.title())
for i in range(7777):
    print(i)

#slicing
s="Full stock development"
print(ord('f'))
print(ord('u'))
print(ord('l'))
print(ord('t'))
print(ord('n'))
print(ord('m'))

#srting formating
name=input('enter your name:')
role=input('enter your role:')
print('my name is:',name,'my role as:',role )

#f
name=input('enter your name:')
role=input('enter your role')
print(f'my name is{name} my role as{role}')

#.format
x=int(input('enter your number1='))
y=int(input('enter your number2='))
print('the value of {} and {}'.format(x,y))

#operator
 #arithmatic
x=int(input('enter your number1='))
y=int(input('enter your number2='))
print(f'addition of {x} and {y} is {x+y}')

x=int(input('enter your number1='))
y=int(input('enter your number2='))
print(f'substraction of {x} and {y} is {x-y}')'''

'''x=int(input('enter your number1='))
y=int(input('enter your number2='))
print('the value of {x} and {y}'.format{x+y})

x=int(input('enter your number1='))
y=int(input('enter your number2='))
print('multiplication of :' , x*y)
print('exponentiol of:',x**y)
print(f'division of{x} and {y} is {x/y}')
print(f'floor division of{x} and {y} is {x//y}')
print(f'modulus of{x} and {y} is {x%y}')


#assignment

x= int(input('enter the number1='))
y= int(input('enter the number2='))
z=x+y
print('the value of z is:',z)
z+=x
print('the addition value is:',z)
z-=x
print('the substraction value is:',z)
z*=x
print('the multiplication value is:',z)
z/=x
print('the division value is:',z)'''

#Ascii value

s='mahindra singh dhoni'
print(ord('o'))
print(ord('d'))
print(chr(100))
print(s[ :3])
print(s[4:])
print(s[ :-1])
print(s[ :-3])
print(s.find('i'))
print(s.replace('mahindra singh'
'suresh raina'))


