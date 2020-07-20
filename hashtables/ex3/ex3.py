def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    # get the inner array from the 2D array passed in
    for array in arrays:
        # get the value from the inner array
        for item in array:
            if item in cache:
                # if the item is in the cache increment the value
                cache[item] += 1
            else:
                # else set the value == 1
                cache[item] = 1

    for key, value in cache.items():
        # for each value in the cache
        # if the value is equal to the amount of inner arrays,
        # append the result to the array
        if value == len(arrays):
            result.append(key)

    # if we get here, the array is set,
    # return it

    return result

# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))

    
if __name__ == "__main__":
    result = intersection([
            [1,2,3],
            [1,4,5],
            [1,6,7]
    ])
    print(result == [1])
