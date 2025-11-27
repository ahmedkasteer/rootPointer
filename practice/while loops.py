#while loop: executes block of code as long as cond it true. 
#unlike for loop it can run for infinite no. of times.

# while 1 == 1:
#     print("Help! I'm stuck in a loop")

name = None

# while len(name) == 0:
#     name = input("Enter ur name")
# print("Hello "  + name)

while not name:
    name = input("Enter ur name: ")
print("Hello ", name, "it was that simple.")

count = None
count = int(input("\nPlease enter count you want to print to"))
#takes user input for count 
#repeats loop until count reaches 10
while (count <= 10):
    print(count)
    count = count + 1
print("\nThank you for ur time")

