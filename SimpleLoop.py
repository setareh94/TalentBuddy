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

def reverse_string(s):
	a = len(s)
	m = ""
	while (a==0):
		m += s(a-1)
	print m
reverse_string("Setareh")		    	