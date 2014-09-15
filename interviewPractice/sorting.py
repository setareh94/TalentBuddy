#Sorting


# Sort names
# Take an array of first and last names, sort them into alphabetical order by last name, and then print them to the standard output (stdout) one per line.

def sort_names(names):
    n = len(names)
    for i in range(n-1):
        for j in range(i+1, n):
            if names[i].split(" ")[1][0] > names[j].split(" ")[1][0]:
                aux = names[i]
                names[i] = names[j]
                names[j] = aux
    for name in names:
        print name


#Alternative Solution 

def sort_names(names):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    names = sorted(names, key=lambda x: x.split()[1])
    
    for i in names:
        print i



# Sorted merge
# Given 2 sorted arrays, merge them into one single sorted array and print its elements to standard output.

def merge_arrays(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1            
    result += a[i:]
    result += b[j:]
    for i in result:
        print i,




# Given an array of integer numbers your task is to print to the standard output (stdout) the majority number.
# One number is considered majority if it occurs more than N / 2 times in an array of size N.
# Note: If no number is majority then print "None"




def majority(v):
    sol = -1
    k = 0
    for x in v:
        if k == 0:
            sol = x
            k = 1
        elif x == sol:
            k += 1
        else:
            k -= 1
    cnt = 0
    for x in v:
        if x == sol:
            cnt += 1
    if cnt > len(v) / 2:
        print sol
    else:
        print 'None'                