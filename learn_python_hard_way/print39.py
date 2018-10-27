#!/usr/bin/python
# -*- coding: UTF-8 -*-

# dictionary

# things = ['a','b','c','d']

# print things

# things[1] = 'z'

# print things[1]
# print things


# print '========================'


# stuff = {
#     'name': 'Zed',
#     'age': 36,
#     'height': 6*12+2
# }


# print(stuff['name'])
# print(stuff['age'])
# print(stuff['height'])


# stuff['city'] = 'new zland'

# stuff[1] = '1231'

# del stuff[1]
# print(stuff)




# create a mapping of state to abbreviation
states = {
    'Oregon': "OR",
    "Florida": "FL",
    "California": 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}


# create a basic set of states and some cities in them
cities = {
    'CA': "San Francisco",
    'MI': "Detroit",
    'FL': "Jacksonville",
}

# add some more cities
cities['MY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 30
print "NY State has: ",cities['MY']
print "OR state has: ",cities['OR']


# print some states
print '-' * 30
print "Michigan's abbreviation is: " , states['Michigan']
print "Florida's abbreviation is: " , states['Florida']

# do it by using the state then cities dict
print '-' * 30
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]


# print every state abbreviation
print '-' * 30
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state,abbrev)


# print every city in state
print '-' * 30
for abbrev,city in cities.items():
    print "%s has the city %s" % (state, city)


# now do both at the same time
print '-' * 30
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state,abbrev,cities
    )

print '-' * 30
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."


# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city



a= {'a':1,'b':2,'b':3,1:1,2:2}


print a

for s in a.items():
    print s