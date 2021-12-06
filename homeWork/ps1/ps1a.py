###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: lcsm29
# Collaborators: None
# Time spent (hh:mm): 01:05

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {l.split(',')[0]: int(l.split(',')[1].strip('\n'))
             for l in open(filename, 'r').readlines()}
    return cows


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    desc_weight = {k: v for k, v in reversed(sorted(cows.items(), key=lambda x: x[1]))}
    trips = []
    while len(desc_weight) > 0:
        remaining_capa = limit
        trip = []
        for cow in desc_weight.copy().keys():
            if remaining_capa - cows[cow] >= 0 and cow not in (trips, trip):
                trip.append(cow)
                remaining_capa -= cows[cow]
                del desc_weight[cow]
        trips.append(trip)
    return trips


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    best_trip = []
    for partition in get_partitions(cows):
        valid_trip = True
        for trip in partition:
            weight = 0
            for cow in trip:
                weight += cows[cow]
                if weight > limit:
                    valid_trip = False
        if valid_trip:
            if len(best_trip) == 0:
                best_trip.append(partition)
            else:
                if len(partition) < len(best_trip):
                    best_trip = partition
    return best_trip


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows('ps1_cow_data.txt')
    print("Time Elapsed:")
    start = time.perf_counter_ns()
    greedy_cow_transport(cows)
    print(f"greedy_cow_transport(): {time.perf_counter_ns() - start:,} nanoseconds")
    start = time.perf_counter_ns()
    brute_force_cow_transport(cows)
    print(f"brute_force_cow_transport(): {time.perf_counter_ns() - start:,} nanoseconds")


compare_cow_transport_algorithms()
