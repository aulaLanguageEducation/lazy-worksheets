import random
import spacy
import utils

class Manipulator:

    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def reorder_paragraphs(self, paragraph_list, random_seed=3142):

        random.seed(random_seed)

        paragraph_nested_list = []

        for this_paragraph in paragraph_list:
            paragraph_nested_list.append([this_paragraph])

        random.shuffle(paragraph_nested_list)

        return paragraph_nested_list

    def print_nested_list(self, input_list):

        for this_item in input_list:
            print(this_item[0])
            print(" ")

    def print_list(self, input_list):

        for this_item in input_list:
            print(this_item)
            print(" ")

    #def swap_two_sentences(self, sentences_list):

     #   idx = range(len(sentences_list))
     #  i1, i2 = random.sample(idx, 2)
     # sentences_list[i1], sentences_list[i2] = sentences_list[i2], sentences_list[i1]

     #return sentences_list


    def find_spelling_mistake(self, sentences_list):
       # Selects the first sentence in the paragraph and converts it into string
        first_sentence = str(sentences_list[0])
        print(first_sentence)
       # Splits the first sentence into words
        words_in_first_sentence = first_sentence.split()
       # Converts fist sentence into a list
        list_of_first_sentence = list(words_in_first_sentence)
        print(words_in_first_sentence)
        print("----------")
        for x in sentences_list:
            str(x)
            print(x)
        print(len(x))


   # def reorder_sentences(self, sentences_list):
        # the below function takes a random sentence in a paragraph and replaces it a random different point

        # the line below finds the length of the paragraph
       # length_of_paragraph = len(sentences_list)

        # the line below creates a copy of the original list of text
       # copy_sentences_list = sentences_list.copy()

        # the below takes a random sentence from the length of the paragraph list
       # rand_idx = random.randrange(length_of_paragraph)
       # random_sentence = sentences_list[rand_idx]

        # the line below takes random sentence and indexes it to show the position of the random sentence was within the paragraph, it calls this variable 'index_random_sentence'
       # index_random_sentence = sentences_list.index(random_sentence)

        # the line below takes the copy of the original paragraph and removes the random sentence, creating a new shorter list
       # copy_sentences_list.remove(random_sentence)

        # the below is creating a copy of the index of the random sentence and calling it 'copy_index_random_sentence'
       # copy_index_random_sentence = index_random_sentence

        # the below then ensures the new copy of the index of the random sentence is a different number to the old index (limited to the size of the paragraph)
       # while copy_index_random_sentence == index_random_sentence:
       #     copy_index_random_sentence = random.randrange(length_of_paragraph)

      #  copy_sentences_list.insert(copy_index_random_sentence,random_sentence)
      #  print(copy_sentences_list)

        # the below gives the answers
      #  print("--------------------------------------------------------------------------------------------------")
      #  print("ANSWERS")
      #  print("The sentence in the incorrect place was: " + random_sentence)
      #  correct_sentence_number = str(index_random_sentence+1)
      #  print("This should have been sentence number: " + correct_sentence_number)
      #  print("The paragraph should read:")
      #  print(sentences_list)



def main():

    TEST_URL = 'https://www.bbc.co.uk/news/uk-50929543'
    TEST_URL_GUARDIAN = 'https://www.theguardian.com/uk-news/2019/dec/28/government-exposes-addresses-of-new-year-honours-recipients'

   # paragraphs_from_article = utils.get_paragraphs(TEST_URL_GUARDIAN)

    this_manipulator = Manipulator()

   # output_reordered_paragraphs = this_manipulator.reorder_paragraphs(paragraphs_from_article)

   # this_manipulator.print_nested_list(output_reordered_paragraphs)

  #  print("-------------------------------------------------------------------------------")

   # this_manipulator.print_list(paragraphs_from_article)


    #article_text = utils.get_body(TEST_URL_GUARDIAN)
    article_text = "Good morning, are you aware? Gilbert is addicted to chocolate. It's not great for him. He should eat less chocolate, but he won't."
    sentences_list = utils.get_sentences(article_text)
    output_sentences = this_manipulator.find_spelling_mistake(sentences_list)
    return output_sentences

if __name__ == "__main__":
    sentences_new_order = main()

