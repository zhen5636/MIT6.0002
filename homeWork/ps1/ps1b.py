###########################
# 6.0002 Problem Set 1b: Space Change
# Name: lcsm29
# Collaborators: None
# Time spent (hh:mm): 01:46
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
# memoization (top-down)
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    least_num_eggs = float('inf')
    if target_weight not in memo:
        if target_weight in egg_weights:
            memo[target_weight] = 1
        else:
            for weight in egg_weights:
                if weight < target_weight:
                    least_num_eggs = min(least_num_eggs, dp_make_weight(egg_weights, target_weight - weight, memo))
            memo[target_weight] = least_num_eggs + 1
    return memo.get(target_weight)


# tabular (bottom-up)
def tabular_dp_make_weight(egg_weights, target_weights, memo = {}):
    pass


# lru_cache
from functools import lru_cache
def lru_cache_dp_make_weight(egg_weights, target_weight, memo = {}):
    @lru_cache
    def recursive_dp_make_weight(egg_weights, target_weight, memo = {}):
        least_num_eggs = float('inf')
        if target_weight == 0:
            return 0
        elif target_weight > 0:
            for weight in egg_weights:
                least_num_eggs = min(least_num_eggs, recursive_dp_make_weight(egg_weights, target_weight - weight))
        return least_num_eggs + 1
    return recursive_dp_make_weight(egg_weights, target_weight)


# greedy
def greedy_dp_make_weight(egg_weights, target_weight, memo = {}):
    num_eggs = 0
    for egg in reversed(egg_weights):
        if egg <= target_weight:
            num_eggs += target_weight // egg
            target_weight -= egg * (target_weight // egg)
    return num_eggs if num_eggs > 0 else float('inf')


# brute-force
import itertools
def bf_dp_make_weight(egg_weights, target_weight, memo = {}):
    max_egg_counts = {egg_weight: target_weight // egg_weight for egg_weight in reversed(egg_weights)}
    possible_counts = [[i for i in range(count + 1)] for count in max_egg_counts.values()]
    index_to_egg = {i: egg for i, egg in enumerate(max_egg_counts.keys())}
    all_possibility = list(itertools.product(*possible_counts))
    least_num_eggs = float('inf')
    for combo in all_possibility:
        sum_weight, sum_count = 0, 0
        for i, count in enumerate(combo):
            sum_weight += index_to_egg[i] * count
            sum_count += count
        if sum_weight == target_weight:
            least_num_eggs = min(least_num_eggs, sum_count)
    return least_num_eggs


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    import time
    funcs_to_call = {fn_name: fn_obj for fn_name, fn_obj in globals().items()
                     if 'dp_make_weight' in fn_name and not fn_name.startswith('__')}

    def output_printer():
        print(f"Egg weights = {egg_weights}")
        print(f"n = {n}")
        print(f"Expected ouput: {expected} {explanation}")
        print(f"Actual output:")
        time_elapsed, results = {}, {}
        for fn_name, fn in funcs_to_call.items():
            incorrect = ''
            start = time.perf_counter_ns()
            results[fn_name] = fn(egg_weights, n, {})
            time_elapsed[fn_name] = time.perf_counter_ns() - start
            if results[fn_name] != expected:
                incorrect = ' (incorrect)'
            print(f"{fn_name}: {results[fn_name]}{incorrect}, time_elapsed: {time_elapsed[fn_name]:,} nanoseconds")
        print()

    egg_weights = (1, 5, 10, 25)
    n = 99
    expected = 9
    explanation = '(3 * 25 + 2 * 10 + 0 * 5 + 4 * 1 = 99)'
    output_printer()

    egg_weights = (1, 33, 48)
    n = 100
    expected = 4
    explanation = '(3 * 25 + 2 * 10 + 0 * 5 + 4 * 1 = 99)'
    output_printer()

    egg_weights = (1, 7, 11)
    n = 49
    expected = 7
    explanation = '(0 * 11 + 7 * 7 + 0 * 1)'
    output_printer()

    egg_weights = (3, 5)
    n = 7
    expected = float('inf')
    explanation = '(impossible to hit 7 with 3 and 5)'
    output_printer()

    egg_weights = (2, 7, 8, 33, 42)
    n = 109
    expected = 5
    explanation = '(0 * 42 + 3 * 33 + 1 * 8 + 0 * 7 + 1 * 2 = 109)'
    output_printer()
