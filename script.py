#Step 4 - List
destinations = ['Paris,France','Shanghai,China','Los Angeles,USA','Sao Paulo,Brazil','Cairo,Egypt']

#Step 5 - List
test_traveler = ['Erin Wilkes', 'Shangi,China',['historical site','art']]

#Step 8 - get destination function
def get_destination_index(destination):
  #Function details
  destination_index = destinations.index(destination)
  return destination_index

#Destination Testing
#print(get_destination_index("Los Angeles,USA"))
#print(get_destination_index("Paris,France"))

#Error testing - Invalid
#print(get_destination_index("hyderabad,India"))

#Traveler Function
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

# test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)

# first methos: declare a List of emty lists:
# attractions = [[], [], [], [], []]

# second method: Foor loop
# attractions = []
# for destination in destinations:
#   attractions.append([])

# third method: using List comprehentions:
attractions = [ [] for destination in destinations ]
#print(attractions)

def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
  except SyntaxError: 
    return

add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
#print(attractions)

add_attraction("Los Angeles, USA", ['Griffith Observatory', ['Park']])
# print(attractions)
  
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]

    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

la_arts = find_attractions('Los Angeles, USA', ['art'])
print(la_arts)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ":"
  
  # for attraction_place in traveler_attractions:
  #   interests_string += " the " + attraction_place + ","
  #   return interests_string
  
  for attraction_place in range(len(traveler_attractions)):
    if traveler_attractions[-1] == traveler_attractions[attraction_place]:
      interests_string += " the " + traveler_attractions[attraction_place] + "."
    else:
      interests_string += " the " + traveler_attractions[attraction_place] + ","
    return interests_string

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)