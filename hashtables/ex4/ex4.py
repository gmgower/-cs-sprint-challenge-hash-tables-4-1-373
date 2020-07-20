def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    # iterate through all items in the list
    for (index, item) in enumerate(a):
        # cache the items as they are accessed
        cache[index] = item

    # check item in a again
    for item in a:
        # if the item multiplied by -1 is in the cache
        if (item * -1) in cache:
            # if the item is 0,
            # ignore the value because zero doesn't have a negative
            if item == 0:
                continue
            # else append the opposite of the item in the result list
            result.append(-item)   
    # return the list 
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
