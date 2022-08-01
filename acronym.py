# user inputs a phrase that will be turned into an acronym
# the input is turned into a string
user_input = str(input("Enter a Phrase: "))

# split the string and returns a list
text = user_input.split()

# intialize an empty string
a = " "

# a for loop that takes each words in the inputed list,
# indexes the first letter,
# changes everything to uppercase
# and returns a string
for i in text:
    a = a+str(i[0]).upper()

# print the results
print(a)
