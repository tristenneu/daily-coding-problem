'''
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.
'''

# SOLUTION

def get_itinerary(flights, starting_point, current_itinerary):
    # print('flights', flights)
    # print('starting_point', starting_point)
    # print('current_itinerary', current_itinerary)

    if not flights:
        return current_itinerary + [starting_point]

    updated_itinerary = None
    for index, (city_1, city_2) in enumerate(flights):
        if starting_point == city_1:
            child_itinerary = get_itinerary(
                flights[:index] + flights[index + 1:], city_2, current_itinerary + [city_1])
            if child_itinerary:
                if not updated_itinerary or ''.join(child_itinerary) < ''.join(updated_itinerary):
                    updated_itinerary = child_itinerary

    # print(updated_itinerary)

    return updated_itinerary


print(get_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL', [])) # ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
print(get_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'YUL', []))
print(get_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A', [])) # ['A', 'B', 'C', 'A', 'C']