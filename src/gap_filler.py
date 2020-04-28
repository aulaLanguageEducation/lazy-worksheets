import math as maths
import random
import spacy
from src import utils


class GapFinder:

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')




    def find_gaps(self, txt, removal_proportion=7, random_seed=None):

        doc = self.nlp(txt)

        if random_seed is not None:
            random.seed(random_seed)

        text_with_gaps = []

        tags_of_interest = {"NN",
                            "NNS",
                            "JJ",
                            "JJR",
                            "JJS"}

        # This is the list of words which have been removed
        list_of_words = []

        # This is the total number of words in the document whose token.tag_ is in tags_of_interest
        target_words = 0

        # Using the 'balls in a bag' analogy, this list represents those balls on which is written the word "remove"
        remove_words_list = []

        # Using the 'balls in a bag' analogy, this list represents those balls on which is written the word "leave"
        leave_words_list = []


        for token in doc:
            if token.tag_ in tags_of_interest:
                target_words +=1

        # Please note, the removal_proportion parameter is currently redundant. In this example, the removal...
        # ...proportion is 10% and has been entered manually as a decimal (0.1) as seen at the end of...
        # ...line 50, below. This can of course be changed if this system is workable.
        for i in range(maths.ceil(target_words * 0.1)):
            remove_words_list.append("remove")

        for i in range(target_words - len(remove_words_list)):
            leave_words_list.append("leave")

        # Using the 'balls in a bag' analogy, this list called 'decider' is the bag.
        decider = remove_words_list + leave_words_list

        for token in doc:
            if token.tag_ in tags_of_interest:
                for ball_from_bag in random.sample(decider, 1):
                    if ball_from_bag == "remove":
                        text_with_gaps.append("_______________")
                        list_of_words.append(token.text)
                        decider.remove("remove")
                    elif ball_from_bag == "leave":
                        text_with_gaps.append(token.text)
                        decider.remove("leave")
            else:
                text_with_gaps.append(token.text)

        print("\n--------> GAP FILLER <--------\n")

        # The below stats are only included for ease of reviewing, during manual testing.
        print("--------------------Useful stats below:--------------------")

        print("The total number of target words is ", target_words)

        print("The number of target words to remove is ", len(remove_words_list))

        print("The number of target words to leave is ", len(leave_words_list))

        print("The length of the decider list after running the code is: ", len(decider))

        print("*Please note, the length of the decider list after running the code should be ZERO.*")

        print("-----------------------------------------------------------")

        print("\nRead the first few sentences of the text. What is the general topic of the article?\n")

        print(" ".join(text_with_gaps))

        print("\nCan you fill the gaps in the text with the below ", (len(list_of_words)), " words? \n")

        list_of_words.sort(key=str.lower)

        for word in list_of_words:
            print(word, '\n')

        return text_with_gaps, list_of_words
            
      
        
        
        
        
    def multiple_choice_gapfiller(self, txt, removal_proportion=5, distractor_removal_proportion=99):
    
        doc = self.nlp(txt)
    
        text_with_gaps = []
        
        tags_of_interest = {"NN",
                            "NNS",
                            "JJ"}

        # This is the list of words which have been removed
        list_of_words = []
        
        question_counter = 1

        for token in doc:
            if token.tag_ in tags_of_interest:
                if random.randrange(1,100) <= removal_proportion:
                    text_with_gaps.append(f'({question_counter}) _______________ ')
                    list_of_words.append(token.text)
                    question_counter +=1
                else:
                    text_with_gaps.append(token.text)     
            else:
                text_with_gaps.append(token.text)
    
        # A 'distractor' refers to a possible answer option which is incorrect
        noun_distractor_list = []
    
        adjective_distractor_list = []
    
        # This 'for loop' adds words from the text to the above lists, which can act as 'distractors'
        for token in doc:
            if token.text in list_of_words:
                pass
            elif token.text not in list_of_words:
                # this checks for nouns, singular or mass
                if token.tag_ == "NN":
                    if random.randrange(1,100) <= distractor_removal_proportion:
                            noun_distractor_list.append(token.text)
                # this checks for nouns, plural
                elif token.tag_ == "NNS":
                    if random.randrange(1,100) <= distractor_removal_proportion:
                        noun_distractor_list.append(token.text)  
                # this checks for adjectives
                elif token.tag_ == "JJ":
                    if random.randrange(1,100) <= distractor_removal_proportion:
                        adjective_distractor_list.append(token.text)    
                else:
                    pass
            else:
                pass

        print("\n--------> MULTIPLE CHOICE GAP FILLER <--------")

        print("\nRead the first few sentences of the text. What is the general topic of the article?\n")
    
        print(" ".join(text_with_gaps))
    
        print("\nChoose the correct words below to fill each gap in the text.\n")
    
        answer_counter = 1

        tokenized_list_of_words = self.nlp(" ".join(list_of_words))
             
        # This 'for loop' prints the multiple choice questions: the correct word with two distractors, in a random order
        for token in tokenized_list_of_words:
            print(f'({answer_counter})')
            if token.tag_ == "NN":
                if random.randrange(1,100) <= 33:
                    print(token.text, '/', (random.choice(noun_distractor_list)), '/', (random.choice(noun_distractor_list)),  '\n', )
                elif random.randrange(1,100) <= 66:
                    print((random.choice(noun_distractor_list)), '/', token.text, '/', (random.choice(noun_distractor_list)),  '\n', )
                else:
                    print((random.choice(noun_distractor_list)), '/', (random.choice(noun_distractor_list)), '/', token.text,  '\n', )
            elif token.tag_ == "NNS":
                if random.randrange(1,100) <= 33:
                    print(token.text, '/', (random.choice(noun_distractor_list)), '/', (random.choice(noun_distractor_list)),  '\n', )
                elif random.randrange(1,100) <= 66:
                    print((random.choice(noun_distractor_list)), '/', token.text, '/', (random.choice(noun_distractor_list)),  '\n', )
                else:
                    print((random.choice(noun_distractor_list)), '/', (random.choice(noun_distractor_list)), '/', token.text,  '\n', )
            else:
                if random.randrange(1,100) <= 33:
                    print(token.text, '/', (random.choice(adjective_distractor_list)), '/', (random.choice(adjective_distractor_list)),  '\n', )
                elif random.randrange(1,100) <= 66:
                    print((random.choice(adjective_distractor_list)), '/', token.text, '/', (random.choice(adjective_distractor_list)),  '\n', )
                else:
                    print((random.choice(adjective_distractor_list)), '/', (random.choice(adjective_distractor_list)), '/', token.text,  '\n', )
            answer_counter +=1
                
        answer_key_counter = 1
        
        print('\nAnswer key:\n')
   
        for word in list_of_words:
            print(f'({answer_key_counter})', word, '\n', )
            answer_key_counter +=1
            







    def function_word_filler(self, txt, removal_proportion=15):
     
        doc = self.nlp(txt)
     
        text_with_gaps = []
        
        tags_of_interest = {"EX",
                            "IN",
                            "PDT",
                            "RP",
                            "TO",
                            "WDT",
                            "WP",
                            "WP$"}

        # This is the list of words which have been removed
        list_of_words = []

        question_counter = 1

        for token in doc:
            if token.tag_ in tags_of_interest:
                if random.randrange(1,100) <= removal_proportion:
                    text_with_gaps.append(f'({question_counter})______________')
                    list_of_words.append(token.text)
                    question_counter +=1
                else:
                    text_with_gaps.append(token.text)                  
            else:
                text_with_gaps.append(token.text)

        print("\n--------> FUNCTION WORD GAP FILLER <--------")

        print("\nRead the first few sentences of the text. What is the general topic of the article?\n")
    
        print(" ".join(text_with_gaps))
    
        print("\nCan you fill the gaps in the text with a suitable word?")
    
        answer_key_counter = 1
    
        print('\nAnswer key:\n')
   
        for word in list_of_words:
            print(f'({answer_key_counter})', word, '\n', )
            answer_key_counter +=1

            
            
    def skim_reader(self, txt):

        doc = self.nlp(txt)

        text_with_gaps = []

        for token in doc:
            if token.is_stop == False:
                text_with_gaps.append(token.text)
            else:
                text_with_gaps.append("_" * len(token.text))

        print("\n--------> SKIM READER <--------")

        print("\nPractise your skim reading. Read the below text - some words have been removed! What is the general topic of the article?\n")

        print(" ".join(text_with_gaps))

        print("\n")



    def lemmatizer(self, txt):

        doc = self.nlp(txt)

        text_with_gaps = []

        tags_of_interest = {"VBD",
                            "VBG",
                            "VBN",
                            "VBP",
                            "VBZ"}

        # This is the list of words which have been removed
        list_of_words = []

        question_counter = 1

        for token in doc:
            if token.tag_ in tags_of_interest:
                list_of_words.append(token.text)
                text_with_gaps.append(f"({question_counter}) _______________")
                text_with_gaps.append("( ")
                text_with_gaps.append(token.lemma_)
                text_with_gaps.append(" )")
                question_counter += 1
            else:
                text_with_gaps.append(token.text)

        print("\n--------> VERB LEMMATIZER <--------")

        print("\nRead the below text and fill each gap with the correct form of the verb in brackets.\n")

        print(" ".join(text_with_gaps))

        answer_key_counter = 1

        print("\nAnswer key:\n")

        for word in list_of_words:
            print(f"{answer_key_counter}", word, "\n")
            answer_key_counter +=1
            
            

def main():

    TEST_URL = 'https://www.bbc.co.uk/news/uk-50929543'
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

    text_output = utils.get_body(TEST_URL_GUARDIAN)

    this_gap_finder = GapFinder()

    this_gap_finder.find_gaps(text_output)

    print("------------------------------------------------------------------")
    print(" ")
    
    this_gap_finder.multiple_choice_gapfiller(text_output)
    
    print("------------------------------------------------------------------")
    print(" ")
    
    this_gap_finder.function_word_filler(text_output)
    
    print("------------------------------------------------------------------")
    print(" ")

    this_gap_finder.skim_reader(text_output)

    print("------------------------------------------------------------------")
    print(" ")

    this_gap_finder.lemmatizer(text_output)

    print('\nThis news article can be found via the below link:\n\n', TEST_URL_GUARDIAN)

if __name__ == "__main__":
    main()