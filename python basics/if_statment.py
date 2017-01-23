# if condition/statement
a = 5 
b = 6
c = 3
x = 5
y = 4 
z = 100

#checking conditions
if b > a:
	print('b is greater tha a')
	pass
if z > a + b + c + x + y:
	print('z is the greatest')
	pass
if a == x:
	print('same value')
	pass
if y!=a:
	print('value not equal')
	pass
#using else condition

if a == y:
	print('the values are same')
	pass
else:
	print('the values are not same')

#adding elif statement

if x<y:
	print('x > y')
elif x==y:
	print('x = y')
elif y>x:
	print('y > x')
else:
	print('break out')