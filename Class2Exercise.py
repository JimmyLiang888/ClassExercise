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
average = float(sum(prices))/len(data)

# Step 4: Use a for loop to make a list of the away teams.
# Hint: Use the string method 'find' to locate the end of the away team name,
#       and then slice the string up to that point.

away_teams = []
for row in data:
    away_team = row[0].split("at",1)[0]
    away_teams.append(away_team)
print away_teams


# Step 5: Use a for loop to make a list of the home teams.
# Hint: Use the string method 'find' to locate the start and end of the home team
#       name, and then slice the string.


# Step 6: Create a list of prices for Ravens (or 49ers or whatever) home games.
# Hint: Use the zip function to pair home teams and prices, use a for loop to
#       iterate through both home teams and prices at once, and then add a condition
#       to only save the price if the team is the Ravens.


# Step 7: Create a list of prices for Ravens away games.


# Step 8: Calculate the average of each of the price lists.

