import random

# Display intro to app and how to play game
print('''Welcome to Hogwarts School of Witchcraft and Wizardry

Motto: Draco Dormiens Nunquam Titillandus 

Enter your details to get sorted into a house in hogwarts by the sorting hat.\n''')

# store houses in a list
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

# get details from users
name = input("Enter your full name: ")
location = input("Enter your location: ").lower()

# loop through the list and select a random house
sorting_hat = random.choice(houses)

# display the details of the user and the house that the user has been selected by the hat
print(f"\n{name} from {location}, you have been added to {sorting_hat}!")