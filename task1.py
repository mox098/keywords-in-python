# 1) Take a word input from the user and store it in `a`.
a=input("enter a word").upper()
# 2) Use a `for` loop to iterate through each character `i` in the word `a`.
for i in a:

# 3) For each character, check if it is equal to 'A':
    if i=="A":
# a) If `i == 'A'`, print "A is found".
        print("a is found")
        break
# b) Use `break` to stop the loop immediately after finding 'A'.

# 4) If the current character is not 'A', print "A not found".
    else:
        print("a isnt found")
# (This message prints for each character until 'A' is found or the loop ends.)