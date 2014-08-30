# Vowel count
# Given a string
# Your task is to
# write a function that prints to the standard output (stdout) the number of vowels it contains
# Note that your function will receive the following argument:
# s
# which is the string described above

def count_vowels(s):
    print sum(1 for c in s if c in 'aeiouAEIOU')