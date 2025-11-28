# since using *args groups arguements as tuples
#we can use **kwargs to group arguements as dictionaries

#function defined here
def countires_and_capitals(**kwargs):
    for key, value in kwargs.items():
        print("Country: "+ key.capitalize() + " and it's Capital is: " + value.capitalize())

#calling function
countires_and_capitals(
    usa = "washington dc",
    china = "beijeing",
    germany = "berlin",
    pakistan = "islamabad"
)

