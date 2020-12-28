

SENTENCE_ONE = ['I', 'am', 'in', 'the', 'park']
SENTENCE_TWO = ['In', 'the', 'park']
SENTENCE_THREE = ['I', 'am', 'in', 'love', 'with', 'being', 'in', 'the', 'park', 'in', 'my', 'new', 'shoes']


def example_to_help(input_list):
    """
    using SENTENCE_ONE this will create a new list exactly the same as the input list, but everything will be uppercase
    and this will return this as the output of the function

    so the output should look like this
    ['I', 'AM', 'IN', 'THE', 'PARK']

    """

    output_list = []

    for item in input_list:
        output_list.append(item.upper())

    return output_list

def exercise_one(input_list):
    """
    using SENTENCE_ONE replace the word 'in' and output a new list of words, exactly the same as the original
    but with 'in' replaced with '__' (a string containing two underscores)

    so the output should look like this
    ['I', 'am', '__', 'the', 'park']

    """
    # remove PASS and write your code here
    pass

def exercise_two(input_list):
    """
    using SENTENCE_TWO replace the word 'in' and output a new list of words, exactly the same as the original
    but with 'in' replaced with '__' (a string containing two underscores)

    so the output should look like this
    ['__', 'the', 'park']
    """
    #remove PASS and write your code here
    pass

def exercise_three(input_list):
    """
    using SENTENCE_THREE replace ONLY the second word 'in' and output a new list of words, exactly the same as the original
    but with 'in' replaced with '__' (a string containing two underscores),

    so the output should look like this:
    ['I', 'am', 'in', 'love', 'with', 'being', '__', 'the', 'park', 'in', 'my', 'new', 'shoes']
    """
    # remove PASS and write your code here
    pass


if __name__ == '__main__':
    print("OUTPUT OF FUNCTIONS:")
    print(' ')
    print('example_to_help output = ', example_to_help(SENTENCE_ONE))
    print(' ')
    print('exercise_one output = ', exercise_one(SENTENCE_ONE))
    print(' ')
    print('exercise_two output = ', exercise_two(SENTENCE_TWO))
    print(' ')
    print('exercise_three output = ', exercise_three(SENTENCE_THREE))
    print(' ')
