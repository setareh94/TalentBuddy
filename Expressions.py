# Balanced brackets
# Given a string of open and closed brackets output "Balanced" if the brackets are balanced or "Unbalanced" otherwise.
# A string is balanced if it consists entirely of pairs of opening/closing brackets (in that order), none of which mis-nest.
# Expected complexity: O(N)



def balanced_brackets(s):
    stack = []
    balanced = True
    index = 0
    while index < len(s) and balanced:
        symbol = s[index]
        if symbol == "(":
            stack.append(symbol)
        else:
            if len(stack)==0:
                balanced = False
            else:
                stack.pop()

        index = index + 1

    if balanced and len(stack)==0:
        print "Balanced"
    else:
        print "Unbalanced"