def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # set up empty cache
    cache = {}

    # iterate over length of weights list
    for index in range(length):
        #calculate store value by subtracting the value at the current index from the limit
        store = limit - weights[index]

        # check the cache 
        if store in cache:
            # if store value is in cache, 
            # extract it from the cache & assign it to a new variable
            value_cache = cache[store] # 1
            # create a new list from the results
            # the original index and the needed value 
            new_list = [index, value_cache] # [3, 1]
            # sort the list so that the greatest number is at position 0
            new_list.sort(reverse = True) # [3, 1]
            # return the list
            return new_list
        else:
            # if the value is not present in the cache, 
            # grab the value from the weights list,
            # and assign it to the cache
            cache[weights[index]] = index #cache[weight[value]] = index // dict {4: 0, 6: 1, 10: 2, }       

    return None

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))