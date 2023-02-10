print("Hello, World!") #This is a comment

#variable
x = 5
y = "John"
print(x)
print(y)

#numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#string
a = "Hello"
print(a)

#list
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#tuples
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#set
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  
}
print(thisdict)

#If ... Else
a = 33
b = 200
if b > a:
  print("b is greater than a")

#While Loops
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
    
 #functions
def my_function():
  print("Hello from a function")
