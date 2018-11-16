''' I am making git repos now'''
#now we are gonna make tuples
#tuples are just like list but they are immutable i.e they cannot be modified once made
#tuples are denoted by '()' i.e

t=tuple(range(1,6)) 	# Making a tuple of first five natural no.s
print("your tuple t = ",t )	#accessing tuple


print("first elment",t[0]) 	#accessing individual
print("3rd elment",t[2])	#elements
print("5th elment",t[4])	#of tuple


t=1,2,43,5,6
print("New tuple =",t)


l=list(t)
print(l)
t=tuple(l)
print(t)

#trying to modify the tuple
t[0]=250

#so it gives an error 
#so we cannot modify tuple got it
#now please go to tuple2.py for more info
