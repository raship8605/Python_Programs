#map() to find square of each number in a list
li=[10,20,30,40,50]
square=map(lambda num:num**2,li)
print(list(square))

#map() to convert all strings in a list to uppercase
students = ["rashi", "ram", "shiv", "radha"]
uppercase = list(map(lambda text: text.upper(), students))
print(uppercase)

#map() to add 10 to each element in a list
li=[10,20,30,40,50]
adding=list(map(lambda num:num+10,li))
print(adding)

#map() to multiply two lists element-wise
li1=[2,4,6,8,10]
li2=[1,2,3,4,5]
multiply=list(map(lambda x,y :x*y,li1,li2))
print(multiply)

#map() to calculate cube of even numbers in a list.
li=[1,2,3,4,5,6,7,8]
cubeofeven=list(map(lambda num: num**3 if num%2==0 else num,li))
print(cubeofeven)