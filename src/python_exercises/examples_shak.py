


""""
example 1 - declaring a list and looping through
"""

# I have declared my own list now
my_list = ['I', 'am', 'in', 'the', 'park']

# now we're going to loop through the list and print out every element to the console

for item in my_list:
    print('item = ', item)


# this just prints a new line so we can separate the output of the two examples in the console
print(' ')


""""
example 2 - looping through a list and testing a condition 
"""

# now we're going to loop through the list and test a condition,
# the condition in this case is if the element in the list is the string 'in'
# I will then print it to the screen if the word exists

for item in my_list:
    if item == 'in':
        print("the string contain the word 'in'")


# this just prints a new line so we can separate the output of the two examples in the console
print(' ')


""""
example 3 - looping through a list and creating a new list only with the things we want 
"""

# lets say we want to produce an exercise for our students where we remove the first word of every sentence
# there are many ways of doing this but one simple way is that we know that all sentences start with a capital letter
# so out goal here is to create a new list of all of the words which do not contain a capital letter
# in the original list

# decalre empty list to build in the loop
new_list = []

for item in my_list:
    if item == item.lower(): # what do you think this does?
        new_list.append(item)
    else:
        new_list.append('__')


# now print both lists and see
print('original list = ', my_list)
print('new list = ', new_list)
