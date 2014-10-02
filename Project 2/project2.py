def exhaustive_knapsack(package_list, W):
    best = None
    for candidate in subsets(package_list):
        if verify_knapsack(candiate, W):
            if compare_knapsack(candidate, best):
                best = candidate
    return best