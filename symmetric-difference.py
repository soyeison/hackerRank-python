# If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in 
# the form of a list

""" if __name__ == '__main__':
    a = input().split()
    print(a)
    # => ['5', '4', '3', '2']

    # If the list values are all integer types, use the map() method to convert all the strings to integers

    newlis = list(map(int, a))
    # => [5, 4, 3, 2]

    # CREATING SETS
    myset = {1, 2} # Directly assigning values to a set
    myset = set()  # Initializing a set
    myset = set(['a', 'b']) # Creating a set from a list
    print(myset)
    # => {'a', 'b'}

    # MODIFYING SETS
    # Using the add() function
    myset.add('c')
    print(myset)
    # => {'a', 'c', 'b'}
    myset.add('a') # As 'a' already exists in the set, nothing happens
    myset.add((5, 4))
    print(myset)
    # => {'a', 'c', 'b', (5, 4)}

    # Using the update() function
    myset.update([1, 2, 3, 4]) # update() only works for iterable objects
    print(myset)
    # => {'a', 1, 'c', 'b', 4, 2, (5, 4), 3}
    myset.update({1, 7, 8})
    print(myset)
    # => {'a', 1, 'c', 'b', 4, 7, 8, 2, (5, 4), 3}
    myset.update({1, 6}, [5, 13])
    print(myset)
    # => {'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}

    # REMOVING ITEMS
    # Both the discard() and remove() functions take a single value as an argument and removes that value 
    # from the set. If that value is not present, discard() does nothing, but remove() will raise a KeyError exception
    myset.discard(10)
    print(myset)
    # => {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
    myset.remove(13)
    print(myset)
    # => {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}

    # COMMON SET OPERATIONS 
    # Using union(), intersection() and difference() functions
    a = {2, 4, 5, 9}
    b = {2, 4, 11, 12}
    a.union(b) # Values which exist in a or b
    # => {2, 4, 5, 9, 11, 12}
    a.intersection(b) # Values which exist in a and b
    # => {2, 4}
    a.difference(b) # Values which exist in a but not in b
    # => {9, 5}

    # The union() and intersection() functions are symmetric methods
    a.union(b) == b.union(a)
    # => True
    a.intersection(b) == b.intersection(a)
    # => True
    a.difference(b) == b.difference(a)
    # => False """


    # Solution of problem
if __name__ == '__main__':
    m = int(input())
    mData = set(list(map(int, input().split())))
    n = int(input())
    nData = set(list(map(int, input().split())))

    # Difference in M
    differences = list((mData.union(nData)).difference(mData.intersection(nData)))

    differencesOrdered = sorted(differences)

    for i in differencesOrdered:
        print(i)

    
