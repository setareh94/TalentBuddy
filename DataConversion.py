a_list = [1,1,2,3,5]
a_list.remove(1)
print a_list

def convert_to_binary(n):
    s = ''
    while(n):
        s = str(n % 2) + s;
        n = n / 2
    print s

convert_to_binary(2)


def convert_seconds(seconds):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    h = int(seconds/3600)
    m = int((seconds%3600)/60)
    s = int((seconds%3600)%60)
    h = "%02d" % h
    m = "%02d" % m
    s = "%02d" % s

    
    print ("{}:{}:{}".format(h,m,s))
    
# Caesar shift
# Create a function that takes an input string and encrypts it using a caesar shift of +1.
# Please print the shifted string to the standard output (stdout)
def caesar_shift(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    d = s.lower()
    list_shift = list(d)
    new_list = []
    stringer = ""
    for i in list_shift:
        aa = chr(ord(i)+1)
        new_list.append(aa)
    for i in new_list:
        stringer+=i.upper()
    stringer = stringer.replace("!"," ")
    stringer = stringer.replace("{","A")    
    print stringer

# Count ones
# Given an integer N
# Your task is to
# write a function that prints to the standard output (stdout) the number of 1's present in its binary representation

    def count_one(a):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    s=''
    count = 0
    while(a):
        s = str(a%2) + s
        a = a/2
    for i in s:
        if i == '1':
            count+=1
    print count        


# Binary float
# Given a binary string containing a fractional part your task is to print to the standard output (stdout) its numeric value (as a float).            
def print_float(s):
    # Write your code here
    # To print results to the standard output you can use print
    # Example: print "Hello world!"
    n = s.index(".") # number of positions before the decimal point
    r = 0 # result
    for digit in s.replace(".", ""): 
        # iterate through each digit ommiting the point '.'
        r += int(digit) * 2 ** (n-1) 
        # multiplicate the digit by the respective power of 2
        n -= 1

    print r # 4.1875

     