"""Restaurant rating lister."""
import sys
from random import choice


def get_restaurant_dict(restaurant_file):
    """Opens a file and turns information into dictionary"""
    opened_file = open(restaurant_file)

    restaurant_dict = {}


    for line in opened_file:
        line = line.rstrip()
        rest_list = line.split(':')
        
        restaurant_dict[rest_list[0]] = int(rest_list[1])
    
    opened_file.close()
    
    return restaurant_dict
    

def readable_list(dictionary):
    """Return a readable list using a dictionary as parameter"""
    sentences = []
    for restaurant in dictionary.items():
        sentences.append(f"{restaurant[0]} is rated at {restaurant[1]}")
        
    return sentences
    

def input_restaurant(dict):
    """Prompts user for restaurant name and rating"""
    
    name = input("Enter restaurant name: ")
    rating = int(input("Enter rating: "))
    while rating > 5 or rating < 1:
        rating = int(input("Enter rating between 1 and 5: "))
    dict[name] = rating

    return dict


def main_menu():
    """Main menu for ratings app"""
    print("Main Menu:\n1. Restaurant ratings \n2. Add a new restaurant\
            \n3. Rate a random restaurant\n4. Rate a specific restaurant\
            \n5. Quit\n")
    user_choice = int(input("What do you want to do(1, 2, 3, 4, or 5)?"))
    while user_choice > 5 or user_choice < 1:
        user_choice = int(input("Please input 1, 2, 3, 4, or 5:"))
    
    return user_choice

def print_rest_list(restaurant_list):
    """DocStrings"""
    for sentence in restaurant_list:
        print(sentence)

decision = main_menu()
if decision == 1:
    rest_dict = get_restaurant_dict("scores.txt")

    read_list = readable_list(rest_dict)

    print_rest_list(read_list)
elif decision == 2:
    rest_dict = get_restaurant_dict("scores.txt")
    read_list = readable_list(input_restaurant(rest_dict))
    print_rest_list(read_list)
elif decision == 3:
    rest_dict = get_restaurant_dict("scores.txt")
    restaurants = list(rest_dict.keys())
    
    random_place = choice(restaurants)
    
    rating = int(input(f"How do you feel about {random_place} (1 - 5) "))
    while rating > 5 or rating < 1:
        rating = int(input("Enter rating between 1 and 5: "))
    rest_dict[random_place] = rating
    read_list = readable_list(rest_dict)
    print_rest_list(read_list)
elif decision == 4:
    rest_dict = get_restaurant_dict("scores.txt") # dictionary
    sorted_list = sorted(list(rest_dict.keys())) # names rest.
    # sorted_dict = sorted(rest_dict) 
    ndx_sorted = 0 # new way 
    for name in sorted_list:
        ndx_sorted += 1
        print(f"#{ndx_sorted}.{name}")
    chosen_rest = int(input("Which restaurant do you want to rate? Please use number."))
    while chosen_rest > len(sorted_list) or chosen_rest < 1:
        chosen_rest = int(input("Please choose a listed number."))
    
    rest_key = sorted_list[chosen_rest - 1]
    print(f"You chose {sorted_list[chosen_rest - 1]}.")
    new_rating = int(input("What do you want to rate it?"))
    
    while new_rating > 5 or new_rating < 1:
        new_rating = int(input("Enter rating between 1 and 5: "))
        
    rest_dict[rest_key] = new_rating
    read_list = readable_list(rest_dict)
    print_rest_list(read_list)
else:
    print("Seeya!")
    quit()

# rest_dict = get_restaurant_dict("scores.txt")

# read_list = readable_list(rest_dict)

# print_rest_list(read_list)

# read_list = readable_list(input_restaurant(rest_dict))

# print_rest_list(read_list)