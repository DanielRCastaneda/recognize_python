num1 = 42  # Variable, number
num2 = 2.3 #Variable , float
boolean = True # Boolean
string = 'Hello World' # String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Object
fruit = ('blueberry', 'strawberry', 'banana') # Tuple
print(type(fruit)) # Prints to the Console
print(pizza_toppings[1]) # Prints the 2nd element on the array "pizza_toppings"
pizza_toppings.append('Mushrooms') # pushes 'mushrooms' to the end of the array
print(person['name']) #prints the value of the key 'name'
person['name'] = 'George' # It updates the value to 'George'
person['eye_color'] = 'blue' # It adds the key and value pair of "eye_color" : 'blue' to the object
print(fruit[2]) # Prints 'banana' to the console

if num1 > 45: # if/else statement
    print("It's greater") # prints to the console if statement is true
else:
    print("It's lower") # prints to the console if statement is false 

if len(string) < 5: # if the length of the string is less then 5 
    print("It's a short word!") # Prints to console if statement if true
elif len(string) > 15: # if else statement if string is longer than 15
    print("It's a long word!") # it will Print if statement is true
else:
    print("Just right!") # Will print if the statement is false

for x in range(5): # A for loop
    print(x) #will print the values of x to the console
for x in range(2,5): #a for loop , starting condition of 2, and ending condition of 5
    print(x) # prints x to console
for x in range(2,10,3): #  A for loop with a starting condition of 2, an ending condition of 10 , and it will add 3 to the starting condition
    print(x) # Will print to console
x = 0
while(x < 5): # A while loop, starting condition of 0, ending condition of 5, 
    print(x)
    x += 1 # will add 1 each time the loop is run until the ending condition is met 

pizza_toppings.pop() # Will remove the last element of the array
pizza_toppings.pop(1) # Will remove the 2nd element of the array "Jalepenos"

print(person) # Prints object to console
person.pop('eye_color') # Removes value from the objct
print(person) # Prints to console

for topping in pizza_toppings: # function
    if topping == 'Pepperoni': # if statement
        continue
    print('After 1st if statement')
    if topping == 'Olives': # If statement
        break # Makes the if statement stop

def print_hello_ten_times(): # Function
    for num in range(10): # For loop
        print('Hello') # prints to console

print_hello_ten_times() # Calls the function

def print_hello_x_times(x): # Function
    for num in range(x): # for loop
        print('Hello') # Prints to console

print_hello_x_times(4) # call the function with an argument of 4

def print_hello_x_or_ten_times(x = 10): # Function
    for num in range(x): # For loop
        print('Hello') # Prints to the console

print_hello_x_or_ten_times()  # Calls the function
print_hello_x_or_ten_times(4) # Calls the function with an argument of 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)