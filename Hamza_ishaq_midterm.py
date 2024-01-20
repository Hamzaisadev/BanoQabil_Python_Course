#Hamza_ishaq_03343149433

#Question Number 1
#Write a Python program to do arithmetical operations addition and division.
#1.1

number1 = int(input("Enter Your First Number Here"))
number2 = int(input("Enter Your Second Number Here"))
Total = number1 + number2

print ("The Sum of",number1,"+",number2,"is",Total)

#1.2

dividend = int(input("Enter Dividend For Division"))
divisor = int(input("Enter Divisor For Division"))
result = dividend / divisor

print ("The Division of",dividend,"/",divisor,"is",result)

#1.3

num = int(input("Enter Number"))
power = int(input("Enter Power"))
result = num**power

print("value of", num, "to power of", power, "is", result)

#1.4

Divident = int(input("Enter Divident"))
Divider = int(input("Enter Divider"))
result = Divident//Divider

print("Floor Division Of", Divident, "//" ,Divider, "is", result)

#Question number2

#Write a Python program to find the area of a triangle.
#The formula to the area of a triangle is b*h/2 as done in 30 line

base = int(input("Enter the length of the base of the triangle"))
height = int(input("Enter the height of the triangle"))
area = base*height/2
print ("the area of the triangle is",area)

#Question number 3
#Write a Python program to convert Celsius to Fahrenheit.
#formula to convert Celsius into Fahrenheit is F = (C * 9/5) + 32

Celsius = int(input("Enter temprature in Celsius"))
result = Celsius*9/5+32
print (Celsius,"degrees Celsius is equal to", result, "degrees Fahrenheit")

#Question Number 4
#Write a Python program that return all datatypes that we discussed in the class.

a = 10
b = 10.8
c = "hello world"
d = True
e = [1,2,3,4]
f = (1,2,3,4)
g = {1,2,3,4,}
print ("the data type of", a , "is",type(a))
print ("the data type of", b , "is",type(b))
print ("the data type of", c , "is",type(c))
print ("the data type of" ,d, "is",type(d))
print ("the data type of", e , "is",type(e))
print ("the data type of", f , "is",type(f))
print ("the data type of", g , "is",type(g))
