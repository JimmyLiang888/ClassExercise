'''
WORKING WITH PUBLIC DATA

FiveThirtyEight: http://fivethirtyeight.com/
FiveThirtyEight data: https://github.com/fivethirtyeight/data
NFL ticket prices data: https://github.com/fivethirtyeight/data/tree/master/nfl-ticket-prices

Question: What is the average ticket price for Ravens' home vs away games, and
how do those prices compare to the overall average ticket price?
'''

# open a CSV file from a URL (ignore any warnings) and store in a list of lists
import csv
import requests     # import module (make its functions available)
r = requests.get('https://raw.githubusercontent.com/fivethirtyeight/data/master/nfl-ticket-prices/2014-average-ticket-price.csv')
data = [row for row in csv.reader(r.iter_lines())]

data


# examine the data
type(data)      # list
len(data)       # every list represents a row in the CSV file
data[0]         # header row (list)
data[1]         # first row of data (list)

# only save the data we want
data = data[1:97]

# step 1: create a list that only contains events
events = [row[0] for row in data]       # grab the first element of each row

# step 2: create a list that only contains prices (stored as integers)
prices = [int(row[2]) for row in data]  # cast to an int before storing the price

# Step 3: Calculate the overall average ticket price.
# Hint: Calculate the sum of the list and divide by the length, and keep in mind
#       that one of the numbers must be a float in order to perform "real" division.

# Solution with average price in whole number
average = (sum(prices))/len(data)
average

# Solution with average price in float number
averagef = float(sum(prices))/len(data)
averagef

# Step 4: Use a for loop to make a list of the away teams.
# Hint: Use the string method 'find' to locate the end of the away team name,
#       and then slice the string up to that point.

# Solution 1
away_teams = []
for event in events:
    away_teams.append(event[:event.find(' at')])
print away_teams


# Solution 2
away_teams = []
for row in data:
    away_team = row[0].split(" at",1)[0]
    away_teams.append(away_team)
print away_teams


# Step 5: Use a for loop to make a list of the home teams.
# Hint: Use the string method 'find' to locate the start and end of the home team
#       name, and then slice the string.

# Solution 1
home_teams = []
for event in events:
    home_teams.append(event[event.find(' at ')+4:event.find(' Tickets on' )])
print home_teams

# Solution 2
home_teams = []
for row in data:
    filterhome_team = row[0].split(" Tickets",1)[0]
    home_team = filterhome_team.split(" at ",1)[1]    
    home_teams.append(home_team)
print home_teams

# Step 6: Create a list of prices for Ravens (or 49ers or whatever) home games.
# Hint: Use the zip function to pair home teams and prices, use a for loop to
#       iterate through both home teams and prices at once, and then add a condition
#       to only save the price if the team is the Ravens.

ravens_home_prices = []
for home_team, price in zip(home_teams, prices):
    if home_team == "Baltimore Ravens":
        ravens_home_prices.append(price)
print ravens_home_prices
        
# Zip Function example:
from itertools import izip, count
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, a, b in izip(count(), alist, blist):
    print i, a, b

# Step 7: Create a list of prices for Ravens away games.

ravens_away_prices = []
for away_team, price in zip(away_teams, prices):
    if away_team == "Baltimore Ravens":
        ravens_away_prices.append(price)
print ravens_away_prices

# Step 8: Calculate the average of each of the price lists.

avg_ravens_home_price = sum(ravens_home_prices) / len(ravens_home_prices)
avg_ravens_away_price = sum(ravens_away_prices) / len(ravens_away_prices)
print avg_ravens_home_price
print avg_ravens_away_price


# Print out data in organized list 
for x in data:
    print x

# Print out away teams in organzied list
for y in away_teams:
    print y
    
# Print out home teams in organized list
for x in home_teams:
    print x
