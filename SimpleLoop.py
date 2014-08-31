# Vowel count
# Given a string
# Your task is to
# write a function that prints to the standard output (stdout) the number of vowels it contains
# Note that your function will receive the following argument:
# s
# which is the string described above

def count_vowels(s):
    print sum(1 for c in s if c in 'aeiouAEIOU')

#Classic FizzBuzz
def fizzbuzz(n):
    result = []
    for x in range(1, n+1):
        if x % 3 == 0 and x % 5 == 0:
            result.append("FizzBuzz")
        elif x % 3 == 0:
            result.append('Fizz')
        elif x % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(x))
    for i in result:
        print i


    #Count Digits

    def count_digits(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    	print sum(1 for i in s if i in "123456789")



#oddSquare
def odd_square_sum(x, y):
    print sum(x ** 2 for x in range(x, y + 1) if x % 2 == 1)

odd_square_sum(1, 10)    


# Sqrt
# Given an integer number N, compute its square root without using any math library functions and print the result to standard output. Please round the result downwards to the nearest integer (e.g both 7.1 and 7.9 are rounded to 7)
# Expected complexity: O(logN), O(1)

def compute_sqrt(n):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    print x


#Another Solution to compute_sqrt

def compute_sqrt(n):
    i = 0
    while i * i < n-1:
        i+=1
    print (i)

# Longest palindrome
# Given a string S, find the longest substring in S that is the same in reverse and print it to the standard output. 

def longest_palind(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    s = s.lower()
    results = []

    for i in range(len(s)):
        for j in range(0, i):
            chunk = s[j:i + 1]

            if chunk == chunk[::-1]:
                results.append(chunk)
    print max(results, key=len)             
       
