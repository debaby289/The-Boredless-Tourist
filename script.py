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
print(get_destination_index("Los Angeles,USA"))
print(get_destination_index("Paris,France"))

#Error testing - Invalid
print(get_destination_index("hyderabad,India"))

#Traveler Function
