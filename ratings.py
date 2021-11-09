"""Restaurant rating lister."""



# put your code here
def get_restaurant_dict(restaurant_file):
    opened_file = open(restaurant_file)

    restaurant_dict = {}


    for line in opened_file:
        line = line.rstrip()
        rest_list = line.split(':')
        
        restaurant_dict[rest_list[0]] = int(rest_list[1])
    
    opened_file.close()
    return restaurant_dict
    

def readable_list(dictionary):
    sentences = []
    for restaurant in dictionary.items():
        sentences.append(f"{restaurant[0]} is rated at {restaurant[1]}")
        
    return sentences
    #     print(f"{restaurant_dict[restaurant]}")
    

def input_restaurant(dict):

    name = input("Enter restaurant name: ")
    rating = int(input("Enter rating: "))

    dict[name] = rating

    return dict


def print_rest_list(restaurant_list):

    for sentence in restaurant_list:
        print(sentence)


rest_dict = get_restaurant_dict("scores.txt")

read_list = readable_list(rest_dict)

print_rest_list(read_list)

read_list = readable_list(input_restaurant(rest_dict))

print_rest_list(read_list)