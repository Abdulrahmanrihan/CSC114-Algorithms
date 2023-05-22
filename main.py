import pandas as pd

# used to display all columns not just a few
pd.set_option('display.max_columns', None)

flights = pd.read_csv('flights.csv')
hotels = pd.read_csv('hotels.csv')
users = pd.read_csv('users.csv')


# Just a helper function to show a part of the data when I need to.
def showData():
  print("Flight columns data")
  print(flights.head())
  print("\n")

  print("Hotel columns data")
  print(hotels.head())
  print("\n")

  print("User columns data")
  print(users.head())
  print("\n")

# another helper function
def compare(list1, list2):
  equal = True
  if len(list1) == len(list2):
    for x in list1:
      if x in list2:
        continue
      else:
        equal = False
  else:
    equal = False
  return equal 

unique_cities = []
visited_cities = []
unvisited_cities = [x for x in unique_cities if x not in visited_cities]


# looping all the data to get a list of all the cities in the database
def getAllCities(flights):
  for i in range(len(flights)):
    if flights['to'][i] in unique_cities:
      continue
    else:
      unique_cities.append(flights['to'][i])


# looping over all visited cities by a user using his usercode to calculate the unvisited ones
def getUnvisitedCities(userCode, flights):
  for i in range(len(flights)):
    if flights['userCode'][i] == userCode and flights['to'][
        i] not in visited_cities:
      visited_cities.append(flights['to'][i])


# The main part
def recommendation(userCode, n, budget):

  getAllCities(flights)
  getUnvisitedCities(userCode, flights)
  
  recommendations = []
  
  if compare(visited_cities, unique_cities):
    print("You have visited all the cities already")
    return 1
    
  if(n > len(unvisited_cities)):
      print("You only have ", len(unvisited_cities), " cities left to visit")
      return 1
    
  else:
    for i in range(1, n + 1):
      min = 99999
      index = 0
      for j in range(len(hotels)):
        if hotels['place'][j] in unvisited_cities and hotels['place'][
            j] not in recommendations and hotels['price'][j] < budget:
          if hotels['price'][j] < min:
            min = hotels['price'][j]
            index = j
          else:
            continue
      recommendations.append(hotels['place'][index])
      budget -= hotels['price'][index]

  print(recommendations)


# each city that appears in this list is recommended by default to be visited for only one night

#sample test case 1
recommendation(12, 2, 6000)

#sample test case 2
recommendation(2, 4, 10000)

#sample test case 3
recommendation(6, 1, 2000)