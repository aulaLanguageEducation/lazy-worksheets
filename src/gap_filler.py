import random
import spacy
from src import utils

class GapFinder:

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    
    
    def find_gaps(self, txt, removal_proportion=7, random_seed=3142):

        doc = self.nlp(txt)

        random.seed(random_seed)

        tags_of_interest = {"NN",
                            "NNS",
                            "JJ",
                            "JJR",
                            "JJS"}
        list_of_words = []

        for token in doc:
            if token.tag_ in tags_of_interest:
                if random.randrange(1, 100) <= removal_proportion:
                    txt = txt.replace(token.text, "_______________", 1)
                    list_of_words.append(token.text)

        print("\nRead the first few sentences of the text. What is the general topic of the article?\n")

        print(txt)

        print("\nCan you fill the gaps in the text with the below ", (len(list_of_words)), " words? \n")

        list_of_words.sort(key=str.lower)

        for x in list_of_words:
            print(x, '\n')
            
      
        
        
        
        
    def multiple_choice_gapfiller(self, txt, removal_proportion=5, distractor_removal_proportion=99):
    
        doc = self.nlp(txt)
    
        text_with_gaps = []
        
        tags_of_interest = {"NN",
                            "NNS",
                            "JJ"}
    
        list_of_words = []
        
        question_counter = 1

        for token in doc:
            if token.tag_ in tags_of_interest:
                if random.randrange(1,100) <= removal_proportion:
                    text_with_gaps.append(f'({question_counter}) _______________')
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
   
        for x in list_of_words:
            print(f'({answer_key_counter})', x, '\n', )
            answer_key_counter +=1
            







    def function_word_filler(self, txt, removal_proportion=15):
     
        doc = self.nlp(txt)
     
        text_with_gaps = []
     
        list_of_words = []
    
        question_counter = 1
        
        tags_of_interest = {"EX",
                            "IN",
                            "PDT",
                            "RP",
                            "TO",
                            "WDT",
                            "WP",
                            "WP$"}

        for token in doc:
            if token.tag_ in tags_of_interest:
                if random.randrange(1,100) <= removal_proportion:
                    text_with_gaps.append(f'({question_counter}) ______________')
                    list_of_words.append(token.text)
                    question_counter +=1
                else:
                    text_with_gaps.append(token.text)                  
            else:
                text_with_gaps.append(token.text)

        print("\nRead the first few sentences of the text. What is the general topic of the article?\n")
    
        print(" ".join(text_with_gaps))
    
        print("\nCan you fill the gaps in the text with a suitable word?")
    
        answer_key_counter = 1
    
        print('\nAnswer key:\n')
   
        for x in list_of_words:
            print(f'({answer_key_counter})', x, '\n', )
            answer_key_counter +=1
            
            
            
            
            
            
            

def main():

    TEST_URL = 'https://www.bbc.co.uk/news/uk-50929543'
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

    text_output = utils.get_body(TEST_URL_GUARDIAN)

    this_gap_finder = GapFinder()
    
    this_gap_finder.multiple_choice_gapfiller(text_output)
    
    print("------------------------------------------------------------------")
    print(" ")
    
    this_gap_finder.function_word_filler(text_output)
    
    print("------------------------------------------------------------------")
    print(" ")

    this_gap_finder.find_gaps(text_output)

    print('\nThis news article can be found via the below link:\n\n', TEST_URL_GUARDIAN)

if __name__ == "__main__":
    main()
