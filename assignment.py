def check_lasts(lists):             #this method does all the work
    for i in lists:
        x = find_max(i)             #return INDEX of max element inside the sub list
        if x == len(i) - 1:         #check if found element is the last element
            tmp = factorial(i[x])   #if yes... find factorial value and replace it with original
            i[x] = tmp


def factorial(x):                   #finds factorial of a number where the number is NOT 0
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


def find_max(subl):                #finds the max element of a sublist
    sam = 0
    for i in range(0, len(subl)):   #using range cause we need INDEX not its value
        if subl[i] > subl[sam]:
            sam = i

    return sam


the_set = [[1, 12, 3], [14, 5, 16], [7, 8, 9], [10, 11, 12], [13, 14, 15]]

check_lasts(the_set)

print (*the_set)
